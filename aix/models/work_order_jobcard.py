"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""
from datetime import date
from random import choices
from string import ascii_uppercase, digits
from typing import Tuple, List, Union
from uuid import uuid4

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import Q, Sum, Count, QuerySet
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.timezone import localdate
from django.utils.translation import gettext_lazy as _

from aix.models import EntityModel, ItemThroughModel, LazyLoader, InvoiceModel
from aix.models.mixins import CreateUpdateMixIn, MarkdownNotesMixIn

lazy_loader = LazyLoader()
UserModel = get_user_model()

JCD_NUMBER_CHARS = ascii_uppercase + digits

def generate_jcd_number(length: int = 10, prefix: bool = True) -> str:
    jcd_number = ''.join(choices(JCD_NUMBER_CHARS, k=length))
    if prefix:
        jcd_number = 'JCD' + jcd_number
    return jcd_number

class WorkOrderJobcardModelManager(models.Manager):

    def for_entity(self, entity_slug, user_model):
        qs = self.get_queryset()
        if isinstance(entity_slug, EntityModel):
            qs = qs.filter(entity=entity_slug)
        elif isinstance(entity_slug, str):
            qs = qs.filter(entity__slug__exact=entity_slug)
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
    
    def for_jcds(self, entity_slug, user_model):
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


class WorkOrderJobcardModelAbstract(CreateUpdateMixIn, MarkdownNotesMixIn):
    # todo: having a fulfilled field is not necessary if JOBCARD can have a JCD_STATUS_FULFILLED.

    JCD_STATUS_DRAFT = 'draft'
    JCD_STATUS_REVIEW = 'in_review'
    JCD_STATUS_APPROVED = 'approved'
    JCD_STATUS_FULFILLED = 'fulfilled'
    JCD_STATUS_VOID = 'void'
    JCD_STATUS_CANCELED = 'canceled'

    JCD_STATUS = [
        (JCD_STATUS_DRAFT, _('Draft')),
        (JCD_STATUS_REVIEW, _('In Review')),
        (JCD_STATUS_APPROVED, _('Approved')),
        (JCD_STATUS_FULFILLED, _('Fulfilled')),
        (JCD_STATUS_CANCELED, _('Canceled')),
        (JCD_STATUS_VOID, _('Void')),
    ]

    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    jcd_number = models.SlugField(max_length=20, unique=True, verbose_name=_('Jobcard Number'))
    # todo: remove JOBCARD date from model in favor of state dates... (draft)...
    jcd_date = models.DateField(verbose_name=_('Jobcard Date'), null=True, blank=True)
    jcd_title = models.CharField(max_length=250,
                                verbose_name=_('Jobcard Title'),
                                validators=[
                                    MinLengthValidator(limit_value=5,
                                                       message=_(
                                                           f'JCD Title must be greater than 5'))
                                ])

    current_status = models.CharField(max_length=255, blank=True, null=True)
    weight = models.CharField(max_length=255, blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    fuel = models.FloatField(blank=True, null=True)
    start_mileage = models.IntegerField(blank=True, null=True)
    end_mileage = models.IntegerField(blank=True, null=True)
    scheduled_start_date = models.DateField(blank=True, null=True)
    actual_start_date = models.DateField(blank=True, null=True)
    scheduled_start_time = models.TimeField(blank=True, null=True)
    actual_start_time = models.TimeField(blank=True, null=True)

    jcd_status = models.CharField(max_length=10, choices=JCD_STATUS, default=JCD_STATUS[0][0])
    jcd_amount = models.DecimalField(default=0, decimal_places=2, max_digits=20, verbose_name=_('Jobcard Amount'))
    jcd_amount_received = models.DecimalField(default=0,
                                             decimal_places=2,
                                             max_digits=20,
                                             verbose_name=_('Received Amount'))
    entity = models.ForeignKey('aix.EntityModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('Entity'))

    draft_date = models.DateField(null=True, blank=True, verbose_name=_('Draft Date'))
    in_review_date = models.DateField(null=True, blank=True, verbose_name=_('In Review Date'))
    approved_date = models.DateField(null=True, blank=True, verbose_name=_('Approved Date'))
    void_date = models.DateField(blank=True, null=True, verbose_name=_('Void Date'))
    fulfillment_date = models.DateField(blank=True, null=True, verbose_name=_('Fulfillment Date'))
    canceled_date = models.DateField(null=True, blank=True, verbose_name=_('Canceled Date'))

    jcd_items = models.ManyToManyField('aix.ItemModel',
                                      through='aix.ItemThroughModel',
                                      through_fields=('jcd_model', 'item_model'),
                                      verbose_name=_('Jobcard Items'))
    
    work_order = models.ForeignKey('aix.WorkOrderModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Work Order'))
    handler = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True,
                                 verbose_name=_('Employee'))

    objects = WorkOrderJobcardModelManager()

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['entity']),
            models.Index(fields=['jcd_status']),
            #models.Index(fields=['ce_model']),
            models.Index(fields=['draft_date']),
            models.Index(fields=['in_review_date']),
            models.Index(fields=['approved_date']),
            models.Index(fields=['fulfillment_date']),
            models.Index(fields=['canceled_date']),
            models.Index(fields=['void_date']),
        ]
        unique_together = [
            ('entity', 'jcd_number')
        ]

    def __str__(self):
        # pylint: disable=no-member
        return f'JCD: {self.jcd_number} | {self.get_jcd_status_display()}'

    # Configuration...
    def configure(self,
                  entity_slug: str or EntityModel,
                  user_model,
                  jcd_date: date = None):
        if isinstance(entity_slug, str):
            entity_qs = EntityModel.objects.for_user(
                user_model=user_model)
            entity_model: EntityModel = get_object_or_404(entity_qs, slug__exact=entity_slug)
        elif isinstance(entity_slug, EntityModel):
            entity_model = entity_slug
        else:
            raise ValidationError('entity_slug must be an instance of str or EntityModel')

        self.jcd_number = generate_jcd_number()
        if jcd_date:
            self.jcd_date = jcd_date
        self.entity = entity_model
        return self

    # State Update...
    def get_jcd_item_data(self, queryset: QuerySet = None) -> Tuple:
        if not queryset:
            # pylint: disable=no-member
            queryset = self.itemthroughmodel_set.all().select_related('invoice_model')

        return queryset, queryset.aggregate(
            amount_due=Sum('jcd_total_amount'),
            total_paid=Sum('invoice_model__amount_paid'),
            total_items=Count('uuid')
        )

    # todo: check if all update ste methods can accept a queryset only...
    def update_jcd_state(self,
                        item_queryset: QuerySet = None,
                        item_list: List[ItemThroughModel] = None) -> Union[Tuple, None]:
        if item_queryset and item_list:
            raise ValidationError('Either queryset or list can be used.')

        if item_list:
            self.jcd_amount = round(sum(
                a.jcd_total_amount for a in item_list if a.jcd_item_status != ItemThroughModel.STATUS_CANCELED), 2)
            self.jcd_amount_received = round(sum(
                a.jcd_total_amount for a in item_list if a.is_jcd_delivered()), 2)
        else:
            item_queryset, item_data = self.get_jcd_item_data(queryset=item_queryset)
            total_jcd_amount = round(sum(i.jcd_total_amount for i in item_queryset if not i.is_jcd_canceled()), 2)
            total_received = round(sum(i.jcd_total_amount for i in item_queryset if i.is_jcd_delivered()), 2)
            self.jcd_amount = total_jcd_amount
            self.jcd_amount_received = total_received
            return item_queryset, item_data

    # State...
    def is_draft(self) -> bool:
        return self.jcd_status == self.JCD_STATUS_DRAFT

    def is_review(self) -> bool:
        return self.jcd_status == self.JCD_STATUS_REVIEW

    def is_approved(self) -> bool:
        return self.jcd_status == self.JCD_STATUS_APPROVED

    def is_fulfilled(self) -> bool:
        return self.jcd_status == self.JCD_STATUS_FULFILLED

    def is_canceled(self) -> bool:
        return self.jcd_status == self.JCD_STATUS_CANCELED

    def is_void(self) -> bool:
        return self.jcd_status == self.JCD_STATUS_VOID

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
                raise ValidationError(f'JOBCARD {self.jcd_number} already bound to Estimate {self.ce_model.estimate_number}')
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
            raise ValidationError(message=f'Jobcard {self.jcd_number} cannot be marked as draft.')
        self.jcd_status = self.JCD_STATUS_DRAFT
        self.clean()
        if commit:
            self.save(update_fields=[
                'jcd_status',
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
        return _('Do you want to mark Jobcard %s as Draft?') % self.jcd_number

    # REVIEW...
    def mark_as_review(self, date_review: date = None, commit: bool = False, **kwargs):
        if not self.can_review():
            raise ValidationError(message=f'Jobcard {self.jcd_number} cannot be marked as in review.')
        itemthrough_qs = self.itemthroughmodel_set.all()
        if not itemthrough_qs.count():
            raise ValidationError(message='Cannot review a JOBCARD without items...')
        if not self.jcd_amount:
            raise ValidationError(message='JOBCARD amount is zero.')

        self.in_review_date = localdate() if not date_review else date_review
        self.jcd_status = self.JCD_STATUS_REVIEW
        self.clean()
        if commit:
            self.save(update_fields=[
                'jcd_status',
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
        return _('Do you want to mark Jobcard %s as In Review?') % self.jcd_number

    # APPROVED...
    def mark_as_approved(self, commit: bool = False, date_approved: date = None, **kwargs):
        if not self.can_approve():
            raise ValidationError(message=f'Jobcard {self.jcd_number} cannot be marked as approved.')
        self.approved_date = localdate() if not date_approved else date_approved
        self.jcd_status = self.JCD_STATUS_APPROVED
        self.clean()
        if commit:
            self.itemthroughmodel_set.all().update(jcd_item_status=ItemThroughModel.STATUS_ORDERED)
            self.save(update_fields=[
                'approved_date',
                'jcd_status',
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
        return _('Do you want to mark Jobcard %s as Approved?') % self.jcd_number

    # CANCEL...
    def mark_as_canceled(self, commit: bool = False, date_canceled: date = None, **kwargs):
        if not self.can_cancel():
            raise ValidationError(message=f'Jobcard {self.jcd_number} cannot be marked as canceled.')
        self.canceled_date = localdate() if not date_canceled else date_canceled
        self.jcd_status = self.JCD_STATUS_CANCELED
        self.clean()
        if commit:
            self.save(update_fields=[
                'jcd_status',
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
        return _('Do you want to mark Jobcard %s as Canceled?') % self.jcd_number

    # FULFILL...
    def mark_as_fulfilled(self,
                          date_fulfilled: date = None,
                          jcd_items: Union[QuerySet, List[ItemThroughModel]] = None,
                          commit=False,
                          **kwargs):
        if not self.can_fulfill():
            raise ValidationError(message=f'Jobcard {self.jcd_number} cannot be marked as fulfilled.')
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
        self.jcd_status = self.JCD_STATUS_FULFILLED
        self.clean()

        if commit:
            jcd_items.update(jcd_item_status=ItemThroughModel.STATUS_RECEIVED)
            self.save(update_fields=[
                'fulfillment_date',
                'jcd_status',
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
        return _('Do you want to mark Jobcard %s as Fulfilled?') % self.jcd_number

    # VOID...
    def mark_as_void(self,
                     entity_slug: str,
                     user_model,
                     void_date: date = None,
                     commit=False,
                     **kwargs):
        if not self.can_void():
            raise ValidationError(message=f'Jobcard {self.jcd_number} cannot be marked as void.')

        # all invoices associated with this JOBCARD ...
        invoice_model_qs = self.get_jcd_invoice_queryset(
            entity_slug=entity_slug,
            user_model=user_model
        )
        invoice_model_qs = invoice_model_qs.only('invoice_status')

        if not all(b.is_void() for b in invoice_model_qs):
            raise ValidationError('Must void all JOBCARD invoices before JOBCARD can be voided.')

        self.void_date = localdate() if not void_date else void_date
        self.jcd_status = self.JCD_STATUS_VOID
        self.clean()

        if commit:
            self.save(update_fields=[
                'void_date',
                'jcd_status',
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
        return _('Do you want to mark Jobcard %s as Void?') % self.jcd_number

    # Conevience Methods...

    def get_jcd_invoice_queryset(self, user_model, entity_slug):
        return InvoiceModel.objects.for_entity(
            user_model=user_model,
            entity_slug=entity_slug
        ).filter(invoice_items__workorderjobcardmodel__uuid__exact=self.uuid)

    def get_status_action_date(self):
        if self.is_fulfilled():
            return self.fulfillment_date
        return getattr(self, f'{self.jcd_status}_date')

    def clean(self):
        if not self.jcd_number:
            self.jcd_number = generate_jcd_number()
        if self.is_fulfilled():
            self.jcd_amount_received = self.jcd_amount
        if self.is_fulfilled() and not self.fulfillment_date:
            self.fulfillment_date = localdate()


class WorkOrderJobcardModel(WorkOrderJobcardModelAbstract):
    """
    Jobcard Base Model
    """
