"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from datetime import date
from random import choices
from uuid import uuid4
from string import ascii_uppercase, digits
from typing import Tuple, List, Union

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404
from django.urls import reverse

from aix.models.mixins import SlugNameMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q, Sum, Count, QuerySet
from aix.models import EntityModel, ItemFawThroughModel, LazyLoader
from aix.models.mixins import CreateUpdateMixIn, MarkdownNotesMixIn

lazy_loader = LazyLoader()
UserModel = get_user_model()
CODE_NUMBER_CHARS = ascii_uppercase + digits

def generate_code(length: int = 10, prefix: bool = True) -> str:
    code = ''.join(choices(CODE_NUMBER_CHARS, k=length))
    if prefix:
        code = 'FAW' + code
    return code

class EmployeeFawModelManager(models.Manager):

    def for_entity(self, entity_slug: str, user_model):
        qs = self.get_queryset()
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            # Q(active=True) &
            (
                    Q(entity__admin=user_model) |
                    Q(entity__managers__in=[user_model])
            )
        )

    def for_user(self, user_model):
        qs = self.get_queryset()
        return qs.filter(
            #Q(entity__admin=user_model) |
            Q(entity__managers__in=[user_model])
        )
    
    def for_wo(self, entity_slug, user_model, work_order):
        qs = self.get_queryset()
        if isinstance(entity_slug, EntityModel):
            qs = qs.filter(entity=entity_slug)
        elif isinstance(entity_slug, str):
            qs = qs.filter(entity__slug__exact=entity_slug)
        qs = qs.filter(
            #Q(entity__admin=user_model) |
            Q(entity__managers__in=[user_model])
        )
        
        qs = qs.filter(work_order=work_order)
        return qs
    
    def for_faws(self, entity_slug, user_model):
        qs = self.get_queryset()
        if isinstance(entity_slug, EntityModel):
            qs = qs.filter(entity=entity_slug)
        elif isinstance(entity_slug, str):
            qs = qs.filter(entity__slug__exact=entity_slug)
        return qs.filter(
            #Q(entity__admin=user_model) |
            Q(entity__managers__in=[user_model])
        )
    
    def for_customer(self, entity_slug, customer):
        qs = self.get_queryset()
        if isinstance(entity_slug, EntityModel):
            qs = qs.filter(entity=entity_slug)
        elif isinstance(entity_slug, str):
            qs = qs.filter(entity__slug__exact=entity_slug)
        qs = qs.filter(work_order__customer=customer)
        return qs


class EmployeeFawModel(CreateUpdateMixIn, MarkdownNotesMixIn):
    FAW_STATUS_DRAFT = 'draft'
    FAW_STATUS_REVIEW = 'in_review'
    FAW_STATUS_APPROVED = 'approved'
    FAW_STATUS_FULFILLED = 'fulfilled'
    FAW_STATUS_PAID = 'paid'
    FAW_STATUS_VOID = 'void'
    FAW_STATUS_CANCELED = 'canceled'

    FAW_STATUS = [
        (FAW_STATUS_DRAFT, _('Draft')),
        (FAW_STATUS_REVIEW, _('In Review')),
        (FAW_STATUS_APPROVED, _('Approved')),
        (FAW_STATUS_FULFILLED, _('fulfilled')),
        (FAW_STATUS_PAID, _('Paid')),
        (FAW_STATUS_CANCELED, _('Canceled')),
        (FAW_STATUS_VOID, _('Void'))
    ]

    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)    
    code = models.CharField(blank=False, null=False, max_length=50)
    faw_date = models.DateField(blank=True, null=True)
    faw_status = models.CharField(max_length=15,
                                      choices=FAW_STATUS,
                                      blank=True,
                                      null=True,
                                      default=FAW_STATUS_DRAFT,
                                      verbose_name=_('FAW Item Status'))
    
    draft_date = models.DateField(null=True, blank=True, verbose_name=_('Draft Date'))
    in_review_date = models.DateField(null=True, blank=True, verbose_name=_('In Review Date'))
    approved_date = models.DateField(null=True, blank=True, verbose_name=_('Approved Date'))
    void_date = models.DateField(blank=True, null=True, verbose_name=_('Void Date'))
    fulfillment_date = models.DateField(blank=True, null=True, verbose_name=_('Fulfillment Date'))
    canceled_date = models.DateField(null=True, blank=True, verbose_name=_('Canceled Date'))
    
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('EmployeeFaw Entity'))
    location = models.ForeignKey('aix.CustomerLocationModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('Customer Location'))
    work_order = models.ForeignKey('aix.WorkOrderModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Work Order'))
    faw_items = models.ManyToManyField('aix.EmployeeModel',
                                      through='aix.ItemFawThroughModel',
                                      through_fields=('faw_model', 'employee_model'),
                                      verbose_name=_('FAW Items'))

    objects = EmployeeFawModelManager()

    class Meta:
        verbose_name = _('EmployeeFaw')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
        ]
        unique_together = [
            ('entity', 'faw_date', 'location', 'work_order')
        ]

    def __str__(self):
        return f'{self.faw_date} - {self.faw_date} - {self.work_order}'
    
    # Configuration...
    def configure(self,
                  entity_slug: str or EntityModel,
                  user_model,
                  faw_date: date = None):
        if isinstance(entity_slug, str):
            entity_qs = EntityModel.objects.for_user(
                user_model=user_model)
            entity_model: EntityModel = get_object_or_404(entity_qs, slug__exact=entity_slug)
        elif isinstance(entity_slug, EntityModel):
            entity_model = entity_slug
        else:
            raise ValidationError('entity_slug must be an instance of str or EntityModel')

        self.code = generate_code()
        if faw_date:
            self.faw_date = faw_date
        self.entity = entity_model
        return self

    # State Update...
    def get_faw_item_data(self, queryset: QuerySet = None) -> Tuple:
        if not queryset:
            # pylint: disable=no-member
            queryset = self.itemfawthroughmodel_set.all().select_related('faw_model')

        return queryset, queryset.aggregate(
            total_items=Count('uuid')
        )

    def get_faw_staff_data(self, queryset: QuerySet = None) -> Tuple:
        if not queryset:
            # pylint: disable=no-member
            # queryset = EmployeeModel.objects.all().select_related('entity')
            queryset = None

        return queryset, queryset.aggregate(
            total_items=Count('uuid')
        )

# State...
    def is_draft(self) -> bool:
        return self.faw_status == self.FAW_STATUS_DRAFT

    def is_review(self) -> bool:
        return self.faw_status == self.FAW_STATUS_REVIEW

    def is_approved(self) -> bool:
        return self.faw_status == self.FAW_STATUS_APPROVED

    def is_fulfilled(self) -> bool:
        return self.faw_status == self.FAW_STATUS_FULFILLED

    def is_canceled(self) -> bool:
        return self.faw_status == self.FAW_STATUS_CANCELED

    def is_void(self) -> bool:
        return self.faw_status == self.FAW_STATUS_VOID

    # Permissions...
    def can_draft(self) -> bool:
        return self.is_review()

    def can_review(self) -> bool:
        return self.is_draft()

    def can_approve(self) -> bool:
        return self.is_review()

    def can_fulfill(self) -> bool:
        return self.is_approved()

    def can_cancel(self) -> bool:
        return any([
            self.is_draft(),
            self.is_review()
        ])

    def can_void(self) -> bool:
        return self.is_approved()

    def can_delete(self) -> bool:
        return any([
            self.is_draft(),
            self.is_review()
        ])

    def can_edit_items(self) -> bool:
        return self.is_draft()

    def can_bind_estimate(self, estimate_model, raise_exception: bool = False) -> bool:
        if self.ce_model_id:
            if raise_exception:
                raise ValidationError(f'JOBCARD {self.code} already bound to Estimate {self.ce_model.estimate_number}')
            return False
        # check if estimate_model is passed and raise exception if needed...
        is_approved = estimate_model.is_approved()
        if not is_approved and raise_exception:
            raise ValidationError(f'Cannot bind estimate that is not approved.')
        return all([
            is_approved
        ])

    # Actions...
    def action_bind_estimate(self, estimate_model, commit: bool = False):
        try:
            self.can_bind_estimate(estimate_model, raise_exception=True)
        except ValueError as e:
            raise e
        self.ce_model = estimate_model
        self.clean()
        if commit:
            self.save(update_fields=[
                'ce_model',
                'updated'
            ])

    # DRAFT...
    def mark_as_draft(self, commit: bool = False, **kwargs):
        if not self.can_draft():
            raise ValidationError(message=f'Jobcard {self.code} cannot be marked as draft.')
        self.faw_status = self.FAW_STATUS_DRAFT
        self.clean()
        if commit:
            self.save(update_fields=[
                'faw_status',
                'updated'
            ])

    def get_mark_as_draft_html_id(self):
        return f'djl-{self.uuid}-jcd-mark-as-draft'

    def get_mark_as_draft_url(self):
        return reverse('aix:jcd-action-mark-as-draft',
                       kwargs={
                           'entity_slug': self.entity.slug,
                           'jcd_pk': self.uuid
                       })

    def get_mark_as_draft_message(self):
        return _('Do you want to mark Jobcard %s as Draft?') % self.code

    # REVIEW...
    def mark_as_review(self, date_review: date = None, commit: bool = False, **kwargs):
        if not self.can_review():
            raise ValidationError(message=f'Jobcard {self.code} cannot be marked as in review.')
        itemthrough_qs = self.itemthroughmodel_set.all()
        if not itemthrough_qs.count():
            raise ValidationError(message='Cannot review a JOBCARD without items...')
        if not self.jcd_amount:
            raise ValidationError(message='JOBCARD amount is zero.')

        self.in_review_date = localdate() if not date_review else date_review
        self.faw_status = self.FAW_STATUS_REVIEW
        self.clean()
        if commit:
            self.save(update_fields=[
                'faw_status',
                'in_review_date',
                'updated'
            ])

    def get_mark_as_review_html_id(self):
        return f'djl-{self.uuid}-jcd-mark-as-review'

    def get_mark_as_review_url(self):
        return reverse('aix:jcd-action-mark-as-review',
                       kwargs={
                           'entity_slug': self.entity.slug,
                           'jcd_pk': self.uuid
                       })

    def get_mark_as_review_message(self):
        return _('Do you want to mark Jobcard %s as In Review?') % self.code

    # APPROVED...
    def mark_as_approved(self, commit: bool = False, date_approved: date = None, **kwargs):
        if not self.can_approve():
            raise ValidationError(message=f'Jobcard {self.code} cannot be marked as approved.')
        self.approved_date = localdate() if not date_approved else date_approved
        self.faw_status = self.FAW_STATUS_APPROVED
        self.clean()
        if commit:
            self.itemthroughmodel_set.all().update(jcd_item_status=ItemFawThroughModel.STATUS_ORDERED)
            self.save(update_fields=[
                'approved_date',
                'faw_status',
                'updated'
            ])

    def get_mark_as_approved_html_id(self):
        return f'djl-{self.uuid}-jcd-mark-as-approved'

    def get_mark_as_approved_url(self):
        return reverse('aix:jcd-action-mark-as-approved',
                       kwargs={
                           'entity_slug': self.entity.slug,
                           'jcd_pk': self.uuid
                       })

    def get_mark_as_approved_message(self):
        return _('Do you want to mark Jobcard %s as Approved?') % self.code

    # CANCEL...
    def mark_as_canceled(self, commit: bool = False, date_canceled: date = None, **kwargs):
        if not self.can_cancel():
            raise ValidationError(message=f'Jobcard {self.code} cannot be marked as canceled.')
        self.canceled_date = localdate() if not date_canceled else date_canceled
        self.faw_status = self.FAW_STATUS_CANCELED
        self.clean()
        if commit:
            self.save(update_fields=[
                'faw_status',
                'canceled_date',
                'updated'
            ])

    def get_mark_as_canceled_html_id(self):
        return f'djl-{self.uuid}-jcd-mark-as-canceled'

    def get_mark_as_canceled_url(self):
        return reverse('aix:jcd-action-mark-as-canceled',
                       kwargs={
                           'entity_slug': self.entity.slug,
                           'jcd_pk': self.uuid
                       })

    def get_mark_as_canceled_message(self):
        return _('Do you want to mark Jobcard %s as Canceled?') % self.code

    # FULFILL...
    def mark_as_fulfilled(self,
                          date_fulfilled: date = None,
                          jcd_items: Union[QuerySet, List[ItemFawThroughModel]] = None,
                          commit=False,
                          **kwargs):
        if not self.can_fulfill():
            raise ValidationError(message=f'Jobcard {self.code} cannot be marked as fulfilled.')
        self.fulfillment_date = localdate() if not date_fulfilled else date_fulfilled

        if not jcd_items:
            jcd_items = self.itemthroughmodel_set.all().select_related('invoice_model')

        invoice_models = [i.invoice_model for i in jcd_items]
        all_items_invoiced = all(invoice_models)
        if not all_items_invoiced:
            raise ValidationError('All items must be invoiced xbefore JOBCARD can be fulfilled.')

        all_invoices_paid = all(b.is_paid() for b in invoice_models)
        if not all_invoices_paid:
            raise ValidationError('All Bills must be paid before JOBCARD can be fulfilled.')

        all_items_received = all(i.is_jcd_delivered() for i in jcd_items)
        if not all_items_received:
            raise ValidationError('All items must be received before JOBCARD is fulfilled.')

        self.fulfillment_date = date_fulfilled
        self.faw_status = self.FAW_STATUS_FULFILLED
        self.clean()

        if commit:
            jcd_items.update(jcd_item_status=ItemFawThroughModel.STATUS_RECEIVED)
            self.save(update_fields=[
                'fulfillment_date',
                'faw_status',
                'updated'
            ])

    def get_mark_as_fulfilled_html_id(self):
        return f'djl-{self.uuid}-jcd-mark-as-fulfilled'

    def get_mark_as_fulfilled_url(self):
        return reverse('aix:jcd-action-mark-as-fulfilled',
                       kwargs={
                           'entity_slug': self.entity.slug,
                           'jcd_pk': self.uuid
                       })

    def get_mark_as_fulfilled_message(self):
        return _('Do you want to mark Jobcard %s as Fulfilled?') % self.code

    # VOID...
    def mark_as_void(self,
                     entity_slug: str,
                     user_model,
                     void_date: date = None,
                     commit=False,
                     **kwargs):
        if not self.can_void():
            raise ValidationError(message=f'Jobcard {self.code} cannot be marked as void.')

        # all invoices associated with this JOBCARD ...
        invoice_model_qs = self.get_jcd_invoice_queryset(
            entity_slug=entity_slug,
            user_model=user_model
        )
        invoice_model_qs = invoice_model_qs.only('invoice_status')

        if not all(b.is_void() for b in invoice_model_qs):
            raise ValidationError('Must void all JOBCARD invoices before JOBCARD can be voided.')

        self.void_date = localdate() if not void_date else void_date
        self.faw_status = self.FAW_STATUS_VOID
        self.clean()

        if commit:
            self.save(update_fields=[
                'void_date',
                'faw_status',
                'updated'
            ])

    def get_mark_as_void_html_id(self):
        return f'djl-{self.uuid}-jcd-mark-as-void'

    def get_mark_as_void_url(self):
        return reverse('aix:jcd-action-mark-as-void',
                       kwargs={
                           'entity_slug': self.entity.slug,
                           'jcd_pk': self.uuid
                       })

    def get_mark_as_void_message(self):
        return _('Do you want to mark Jobcard %s as Void?') % self.code

