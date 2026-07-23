"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""
from random import choices
from string import ascii_uppercase, digits
from typing import Tuple, List, Union
from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q, Sum, Count, QuerySet
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from aix.models.entity import EntityModel
from aix.models.mixins import ContactInfoMixIn, CreateUpdateMixIn

UserModel = get_user_model()
CODE_NUMBER_CHARS = ascii_uppercase + digits

def generate_code_number(length: int = 10, prefix: bool = True) -> str:
    code_number = ''.join(choices(CODE_NUMBER_CHARS, k=length))
    if prefix:
        code_number = 'WO' + code_number
    return code_number

STATUSES = (('NEW', 'NEW'), ('IN PROGRESS','IN PROGRESS'), ('DELAYED','DELAYED'), ('POSTPONED','POSTPONED'), ('COMPLETED','COMPLETED'))

SERVICETYPES = (('TRANSPORT AND LIFTING', 'TRANSPORT AND LIFTING'), ('LIFTING ONLY','LIFTING ONLY'), ('TRANSPORT ONLY','TRANSPORT ONLY'))

class WorkOrderModelManager(models.Manager):

    def for_entity(self, entity_slug: str, user_model):
        qs = self.get_queryset()
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            Q(entity__managers__in=[user_model])
            # Q(is_active=True) &
            # (
            #         #Q(entity__admin=user_model) |
            #         Q(entity__managers__in=[user_model])
            # )
        )

    def for_customer(self, entity_slug: str, customer):
        qs = self.get_queryset()
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            Q(customer=customer)
        )

    def for_wo(self, entity_slug: str, work_order):
        qs = self.get_queryset()
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            Q(work_order=work_order)
        )


class WorkOrderModel(ContactInfoMixIn, CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    order_no = models.CharField(unique=True, max_length=255) 
    remarks = models.CharField(max_length=255, blank=True, null=True)
    progress = models.IntegerField(default=0, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    truck_loads = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateField(blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateField(blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(choices=STATUSES, max_length=255, blank=True, null=True, default="NEW")
    price = models.IntegerField(blank=True, null=True)
    clientref = models.CharField(max_length=255, blank=True, null=True)
    service_type = models.CharField(max_length=255, blank=True, null=True, choices=SERVICETYPES)
    is_active = models.BooleanField(default=True)

    
    entity = models.ForeignKey('aix.EntityModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('WorkOrder Entity'),
                               related_name='work_order_entity')
    wo_type = models.ForeignKey('aix.WorkOrderTypeModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('WorkOrder Type'))
    customer = models.ForeignKey('aix.CustomerModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('Customer'))
    currency = models.ForeignKey('aix.CurrencyModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('Currency'))
    category = models.ForeignKey('aix.WorkCategoryModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('WorkCategory'))

    objects = WorkOrderModelManager()

    class Meta:
        verbose_name = _('WorkOrder')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['is_active']),
        ]
        unique_together = [
            ('entity', 'order_no')
        ]

    def __str__(self):
        return f'{self.order_no}'

    def configure(self,
                  entity_slug: str or EntityModel,
                  user_model: UserModel,
                  post_ledger: bool = False):

        if isinstance(entity_slug, str):
            entity_qs = EntityModel.objects.for_user(
                user_model=user_model)
            entity_model: EntityModel = get_object_or_404(entity_qs, slug__exact=entity_slug)
        elif isinstance(entity_slug, EntityModel):
            entity_model = entity_slug
        else:
            raise ValidationError('entity_slug must be an instance of str or EntityModel')

        if not self.order_no:
            self.order_no = generate_code_number()


        
    def get_total_invoiced(self, invoice_qs):        
        #tot_amt_owed = list ((inv['amount_due'], v) for inv, v in invoice_qs)
        tot_amt_invoiced = 0
        for inv in invoice_qs:
            tot_amt_invoiced += inv.amount_due
        return tot_amt_invoiced

    def get_total_paid(self, invoice_qs):
        tot_amt_paid = 0
        for inv in invoice_qs:
            tot_amt_paid += inv.amount_paid
        return tot_amt_paid

    def get_total_owed(self, amt_invoiced=0, amt_paid=0):
        return amt_invoiced - amt_paid

    def get_total_no_invoices(self, invoice_qs, invoice_state=None):
        tot_number = 0
        for inv in invoice_qs:
            if invoice_state == 'cleared' and (inv.amount_paid >= inv.amount_due):
                tot_number += 1
            if invoice_state == 'pending' and (inv.amount_due >= inv.amount_paid):
                tot_number += 1
        return tot_number

    # State Update...
    def get_jcd_item_data(self, queryset: QuerySet = None) -> Tuple:
        if not queryset:
            # pylint: disable=no-member
            queryset = self.itemthroughmodel_set.all().select_related('invoice_model')

        return queryset, queryset.aggregate(
            amount_due=Sum('jcd_total_amount'),
            total_paid=Sum('invoice_model__amount_paid'),
            total_items=Count('work_order__uuid')
        )

    def get_mark_as_approved_html_id(self):
        return f'djl-{self.uuid}-work-order-action-mark-as-approved'

    def get_mark_as_approved_url(self):
        return reverse('aix:work-order-action-mark-as-approved',
                       kwargs={
                           'entity_slug': self.entity.slug,
                           'work_order_pk': self.uuid
                       })

    def get_mark_as_approved_message(self):
        return _('Do you want to mark Work Order %s as Approved?') % self.order_no


    def get_mark_as_unapproved_html_id(self):
        return f'djl-{self.uuid}-work-order-action-mark-as-unapproved'


    def get_mark_as_unapproved_url(self):
        return reverse('aix:work-order-action-mark-as-unapproved',
                       kwargs={
                           'entity_slug': self.entity.slug,
                           'work_order_pk': self.uuid
                       })

    def get_mark_as_unapproved_message(self):
        return _('Do you want to mark Work Order %s as Un Approved?') % self.order_no

    # APPROVED...
    def mark_as_approved(self, **kwargs):
        # if not self.can_approve():
        #     raise ValidationError(f'Cannot mark PO {self.uuid} as Approved...')

        self.status = 'APPROVED'
        self.is_active = True
        # self.approved_date = localdate() if not date_approved else date_approved
        self.clean()
        self.save()

    # DISABLED...
    def mark_as_unapproved(self, **kwargs):
        # if not self.can_approve():
        #     raise ValidationError(f'Cannot mark PO {self.uuid} as Approved...')

        self.status = 'DISABLED'
        self.is_active = False
        # self.approved_date = localdate() if not date_approved else date_approved
        self.clean()
        self.save()
