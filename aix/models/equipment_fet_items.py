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

class ItemFetModelQuerySet(models.QuerySet):

    def active(self):
        return self.filter(active=True)


class ItemFetModelManager(models.Manager):

    def get_queryset(self):
        return ItemFetModelQuerySet(self.model, using=self._db)

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

    def for_fet(self, entity_slug: str, user_model):
        qs = self.for_entity_active(entity_slug=entity_slug, user_model=user_model)
        return qs

class ItemFetModelAbstract(CreateUpdateMixIn):
    REL_NAME_PREFIX = 'item'

    OPERATIONAL_CODE = 'H'
    STANDBY_CODE = 'S'
    OH_CODE = 'OH'
    REPAIR_CODE = 'R'
    MOB_CODE = 'MOB'
    DMB_CODE = 'DMB'
    NOS_CODE = 'NOS'
    OPS_CODE = 'OPS'
    ES_CODE = 'ES'


    ITEM_CHOICES = [
        (OPERATIONAL_CODE, _('Machine operational')),
        (STANDBY_CODE, _('Machine on Standby')),
        (OH_CODE, _('Machine off Hire')),
        (REPAIR_CODE, _('Machine Under Repair')),
        (MOB_CODE, _('Mobilization')),
        (DMB_CODE, _('De-Mobilization')),
        (NOS_CODE, _('Not/ Nolonger on  site')),
        (OPS_CODE, _('Operational, at TWS Cost')),
        (ES_CODE, _('Equipment Serviced'))
    ]

    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=100, verbose_name=_('ItemFet Name'))
    attendance_code = models.CharField(max_length=10, choices=ITEM_CHOICES, null=True, blank=True)
    attendance_date = models.DateField(null=False, blank=False)
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))

    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               related_name='items_fet',
                               on_delete=models.CASCADE,
                               verbose_name=_('ItemFet Entity'))

    objects = ItemFetModelManager()

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['is_active']),
            models.Index(fields=['attendance_code']),
            models.Index(fields=['entity', 'attendance_code'])
        ]

    def __str__(self):
        return f'ItemFet: {self.attendance_code}  | {self.equipment} | {self.attendance_date}'


class ItemFetThroughModelQueryset(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

class ItemFetThroughModelManager(models.Manager):

    def get_queryset(self):
        return ItemFetThroughModelQueryset(self.model, using=self._db)

    def for_entity(self, user_model, entity_slug):
        qs = self.get_queryset()
        return qs.filter(
            Q(equipment_model__entity__slug__exact=entity_slug) &
            (
                    Q(equipment_model__entity__admin=user_model) |
                    Q(equipment_model__entity__managers__in=[user_model])
            )
        )

    def for_equipment(self, entity_slug, user_model, equipment_pk):
        qs = self.for_entity(entity_slug=entity_slug, user_model=user_model)
        return qs.filter(equipment_model__uuid__exact=equipment_pk)

    def for_fet(self, entity_slug, user_model, fet_pk):
        qs = self.for_entity(entity_slug=entity_slug, user_model=user_model)
        return qs.filter(fet_model__uuid__exact=fet_pk)

class ItemFetThroughModelAbstract(ParentChildMixIn, CreateUpdateMixIn):
    OPERATIONAL_CODE = 'H'
    STANDBY_CODE = 'S'
    OH_CODE = 'OH'
    REPAIR_CODE = 'R'
    MOB_CODE = 'MOB'
    DMB_CODE = 'DMB'
    NOS_CODE = 'NOS'
    OPS_CODE = 'OPS'
    ES_CODE = 'ES'

    STATUS_DRAFT = 'draft'
    STATUS_COMPLETED = 'completed'
    STATUS_CANCELED = 'canceled'

    ITEM_CHOICES = [
        (OPERATIONAL_CODE, _('Machine operational')),
        (STANDBY_CODE, _('Machine on Standby')),
        (OH_CODE, _('Machine off Hire')),
        (REPAIR_CODE, _('Machine Under Repair')),
        (MOB_CODE, _('Mobilization')),
        (DMB_CODE, _('De-Mobilization')),
        (NOS_CODE, _('Not/ Nolonger on  site')),
        (OPS_CODE, _('Operational, at TWS Cost')),
        (ES_CODE, _('Equipment Serviced'))
    ]

    FET_ITEM_STATUS = [
        (STATUS_DRAFT, _('Draft')),
        (STATUS_COMPLETED, _('Completed')),
        (STATUS_CANCELED, _('Canceled')),
    ]

    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    entity_unit = models.ForeignKey('aix.EntityUnitModel',
                                    on_delete=models.PROTECT,
                                    blank=True,
                                    null=True,
                                    verbose_name=_('Associated Branch'))
    attendance_code = models.CharField(max_length=10, choices=ITEM_CHOICES, default=REPAIR_CODE, null=True, blank=True)
    attendance_date = models.DateField(null=True, blank=True)
    fet_item_status = models.CharField(max_length=15,
                                      choices=FET_ITEM_STATUS,
                                      blank=True,
                                      null=True,
                                      default=STATUS_DRAFT,
                                      verbose_name=_('FET Item Status'))

    # FET fields...
    fet_model = models.ForeignKey('aix.EquipmentFetModel',
                                 on_delete=models.PROTECT,
                                 null=True,
                                 blank=True,
                                 verbose_name=_('FET Model'))
    
    equipment_model = models.ForeignKey('aix.EquipmentModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Equipment'))

    objects = ItemFetThroughModelManager()

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['fet_model', 'equipment_model']),
            models.Index(fields=['fet_item_status']),
        ]

    # def __str__(self):
        # pylint: disable=no-member

    def is_fet_completed(self):
        return self.fet_item_status == self.STATUS_COMPLETED

    def is_fet_canceled(self):
        return self.fet_item_status == self.STATUS_CANCELED

    def html_id(self):
        return f'djl-item-{self.uuid}'

    def is_cancelled(self):
        return self.fet_item_status == self.STATUS_CANCELED

    def is_fet_cancelled(self):
        return self.fet_item_status == self.STATUS_CANCELED


    def get_status_css_class(self):
        if self.fet_item_status == self.STATUS_RECEIVED:
            return ' is-success'
        elif self.fet_item_status == self.STATUS_CANCELED:
            return ' is-danger'
        elif self.fet_item_status == self.STATUS_ORDERED:
            return ' is-info'
        return ' is-warning'

    def get_fet_status_css_class(self):
        if self.fet_item_status == self.STATUS_RECEIVED:
            return ' is-success'
        elif self.fet_item_status == self.STATUS_CANCELED:
            return ' is-danger'
        elif self.fet_item_status == self.STATUS_ORDERED:
            return ' is-info'
        return ' is-warning'


class ItemFetThroughModel(ItemFetThroughModelAbstract):
    """
    Base ItemFet Model Through Model for Many to Many Relationships
    """


class ItemFetModel(ItemFetModelAbstract):
    """
    Base ItemFet Model from Abstract.
    """
