"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""
from decimal import Decimal
from string import ascii_lowercase, digits
from uuid import uuid4

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q, Sum, F, ExpressionWrapper, DecimalField, Value, Case, When
from django.db.models.functions import Coalesce
from django.utils.translation import gettext_lazy as _

from aix.models.mixins import CreateUpdateMixIn, ParentChildMixIn
from aix.settings import (MANDO_CURRENCY_SYMBOL as currency_symbol,
                                    MANDO_TRANSACTION_MAX_TOLERANCE)

ITEM_LIST_RANDOM_SLUG_SUFFIX = ascii_lowercase + digits

class ItemFawModelQuerySet(models.QuerySet):

    def active(self):
        return self.filter(active=True)


class ItemFawModelManager(models.Manager):

    def get_queryset(self):
        return ItemFawModelQuerySet(self.model, using=self._db)

    def for_entity(self, entity_slug: str, user_model):
        qs = self.get_queryset()
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            (
                    Q(entity__managers__in=[user_model]) |
                    Q(entity__admin=user_model)
            )
        )

    def for_entity_active(self, entity_slug: str, user_model):
        qs = self.for_entity(entity_slug=entity_slug, user_model=user_model)
        return qs.filter(is_active=True)

    def for_faw(self, entity_slug: str, user_model):
        qs = self.for_entity_active(entity_slug=entity_slug, user_model=user_model)
        return qs

class ItemFawModelAbstract(CreateUpdateMixIn):
    REL_NAME_PREFIX = 'item'

    PRESENT_CODE = 'P'
    SICK_CODE = 'S'
    LEAVE_CODE = 'L'
    ABSENT_CODE = 'A'
    MOB_CODE = 'MOB'
    DMB_CODE = 'DMB'

    ITEM_CHOICES = [
        (PRESENT_CODE, _('PRESENT')),
        (SICK_CODE, _('SICK')),
        (LEAVE_CODE, _('LEAVE')),
        (ABSENT_CODE, _('ABSENT')),
        (MOB_CODE, _('Move To Work Site')),
        (DMB_CODE, _('DEMMOBED')),
    ]

    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=100, verbose_name=_('ItemFaw Name'))
    attendance_code = models.CharField(max_length=10, choices=ITEM_CHOICES, null=True, blank=True)
    attendance_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))

    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               related_name='items_faw',
                               on_delete=models.CASCADE,
                               verbose_name=_('ItemFaw Entity'))

    objects = ItemFawModelManager()

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['is_active']),
            models.Index(fields=['attendance_code']),
            models.Index(fields=['entity', 'attendance_code'])
        ]

    def __str__(self):
        return f'ItemFaw: {self.attendance_code}  | {self.employee} | {self.attendance_date}'


class ItemFawThroughModelQueryset(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

class ItemFawThroughModelManager(models.Manager):

    def get_queryset(self):
        return ItemFawThroughModelQueryset(self.model, using=self._db)

    def for_entity(self, user_model, entity_slug):
        qs = self.get_queryset()
        return qs.filter(
            Q(employee_model__entity__slug__exact=entity_slug) &
            (
                    Q(employee_model__entity__admin=user_model) |
                    Q(employee_model__entity__managers__in=[user_model])
            )
        )

    def for_employee(self, entity_slug, user_model, employee_pk):
        qs = self.for_entity(entity_slug=entity_slug, user_model=user_model)
        return qs.filter(employee_model__uuid__exact=employee_pk)

    def for_faw(self, entity_slug, user_model, faw_pk):
        qs = self.for_entity(entity_slug=entity_slug, user_model=user_model)
        return qs.filter(faw_model__uuid__exact=faw_pk)

class ItemFawThroughModelAbstract(ParentChildMixIn, CreateUpdateMixIn):
    PRESENT_CODE = 'P'
    SICK_CODE = 'S'
    LEAVE_CODE = 'L'
    ABSENT_CODE = 'A'
    MOB_CODE = 'MOB'
    DMB_CODE = 'DMB'
    STATUS_DRAFT = 'draft'
    STATUS_COMPLETED = 'completed'
    STATUS_CANCELED = 'canceled'

    ITEM_CHOICES = [
        (PRESENT_CODE, _('PRESENT')),
        (SICK_CODE, _('SICK')),
        (LEAVE_CODE, _('LEAVE')),
        (ABSENT_CODE, _('ABSENT')),
        (MOB_CODE, _('Move To Work Site')),
        (DMB_CODE, _('DEMMOBED')),
    ]

    FAW_ITEM_STATUS = [
        (STATUS_DRAFT, _('Completed')),
        (STATUS_COMPLETED, _('Completed')),
        (STATUS_CANCELED, _('Canceled')),
    ]
    
    PRESENT_CODE = 'P'
    SICK_CODE = 'S'
    LEAVE_CODE = 'L'
    ABSENT_CODE = 'A'
    MOB_CODE = 'MOB'
    DMB_CODE = 'DMB'

    ITEM_CHOICES = [
        (PRESENT_CODE, _('PRESENT')),
        (SICK_CODE, _('SICK')),
        (LEAVE_CODE, _('LEAVE')),
        (ABSENT_CODE, _('ABSENT')),
        (MOB_CODE, _('Move To Work Site')),
        (DMB_CODE, _('DEMMOBED')),
    ]

    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    entity_unit = models.ForeignKey('aix.EntityUnitModel',
                                    on_delete=models.PROTECT,
                                    blank=True,
                                    null=True,
                                    verbose_name=_('Associated Branch'))
    attendance_code = models.CharField(max_length=10, choices=ITEM_CHOICES, default=ABSENT_CODE, null=True, blank=True)
    attendance_date = models.DateField(null=True, blank=True)
    faw_item_status = models.CharField(max_length=15,
                                      choices=FAW_ITEM_STATUS,
                                      blank=True,
                                      null=True,
                                      default=STATUS_DRAFT,
                                      verbose_name=_('FAW Item Status'))

    # FAW fields...
    faw_model = models.ForeignKey('aix.EmployeeFawModel',
                                 on_delete=models.PROTECT,
                                 null=True,
                                 blank=True,
                                 verbose_name=_('FAW Model'))
    
    employee_model = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Employee'))

    objects = ItemFawThroughModelManager()

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['faw_model', 'employee_model']),
            models.Index(fields=['faw_item_status']),
        ]

    # def __str__(self):
        # pylint: disable=no-member

    def is_faw_completed(self):
        return self.faw_item_status == self.STATUS_COMPLETED

    def is_faw_canceled(self):
        return self.faw_item_status == self.STATUS_CANCELED

    def html_id(self):
        return f'djl-item-{self.uuid}'

    def is_cancelled(self):
        return self.faw_item_status == self.STATUS_CANCELED

    def is_faw_cancelled(self):
        return self.faw_item_status == self.STATUS_CANCELED


    def get_status_css_class(self):
        if self.faw_item_status == self.STATUS_RECEIVED:
            return ' is-success'
        elif self.faw_item_status == self.STATUS_CANCELED:
            return ' is-danger'
        elif self.faw_item_status == self.STATUS_ORDERED:
            return ' is-info'
        return ' is-warning'

    def get_faw_status_css_class(self):
        if self.faw_item_status == self.STATUS_RECEIVED:
            return ' is-success'
        elif self.faw_item_status == self.STATUS_CANCELED:
            return ' is-danger'
        elif self.faw_item_status == self.STATUS_ORDERED:
            return ' is-info'
        return ' is-warning'


class ItemFawThroughModel(ItemFawThroughModelAbstract):
    """
    Base ItemFaw Model Through Model for Many to Many Relationships
    """


class ItemFawModel(ItemFawModelAbstract):
    """
    Base ItemFaw Model from Abstract.
    """
