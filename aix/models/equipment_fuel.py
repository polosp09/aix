"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""
from random import choices
from uuid import uuid4
from string import ascii_uppercase, digits
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from aix.models.mixins import SlugNameMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q

CODE_NUMBER_CHARS = ascii_uppercase + digits

def generate_code(length: int = 10, prefix: bool = True) -> str:
    code = ''.join(choices(CODE_NUMBER_CHARS, k=length))
    if prefix:
        code = 'FL' + code
    return code


STATUSES = (('NEW', 'NEW'), ('IN PROGRESS','IN PROGRESS'), ('DELAYED','DELAYED'), ('POSTPONED','POSTPONED'), ('COMPLETED','COMPLETED'))


class EquipmentFuelModelManager(models.Manager):

    def for_entity(self, entity_slug: str, user_model):
        qs = self.get_queryset()
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            #Q(active=True) &
            (
                    #Q(entity__admin=user_model) |
                    Q(entity__managers__in=[user_model])
            )
        )

    def for_wo(self, entity_slug: str, user_model, work_order):
        qs = self.get_queryset()
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            Q(entity__admin=user_model) |
            Q(entity__managers__in=[user_model]) &
            Q(work_order=work_order)
        )

class EquipmentFuelModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(blank=False, null=False, max_length=50)
    fuel_date = models.DateField(blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)
    start_mileage = models.FloatField(blank=True, null=True)
    end_mileage = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    fuel_qty = models.FloatField(blank=True, null=True)
    fuel_price = models.FloatField(blank=True, null=True)
    fuel_cost = models.FloatField(blank=True, null=True)
    fuel_tank = models.FloatField(blank=True, null=True)
    kms_covered = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True, choices=STATUSES, default="NEW")  # Field name made lowercase.
    

    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('Equipment Fuel Entity'))
    work_order = models.ForeignKey('aix.WorkOrderModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Work Order'))
    equipment = models.ForeignKey('aix.EquipmentModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Equipment'))
    start_location = models.ForeignKey('aix.CustomerLocationModel', 
                                db_column='StartLocation', 
                                related_name='start_location_fuel', 
                                on_delete=models.CASCADE,
                                blank=True, null=True)  # Field name made lowercase.
    end_location = models.ForeignKey('aix.CustomerLocationModel', 
                                db_column='EndLocation', 
                                related_name='end_location_fuel', 
                                on_delete=models.CASCADE,
                                blank=True, null=True)  # Field name made lowercase.
    fuel_reciept = models.ForeignKey('aix.DocumentModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Fuel Receipt'),
                                 blank=True, null=True)

    objects = EquipmentFuelModelManager()

    class Meta:
        verbose_name = _('Equipment Fuel')
        indexes = [
            models.Index(fields=['fuel_date']),
            models.Index(fields=['equipment']),
            models.Index(fields=['start_location']),
            models.Index(fields=['end_location']),
            models.Index(fields=['status']),
        ]
        unique_together = [
            ('entity', 'fuel_date', 'equipment', 'work_order', 'start_location')
        ]

    def __str__(self):
        return f'{self.equipment} - {self.start_location} - {self.fuel_date} - {self.fuel_qty}ltrs'

    def configure(self, entity_slug: str or EntityModel, user_model,):
        self.code = generate_code()
        return self