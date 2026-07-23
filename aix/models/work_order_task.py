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

TRIP_NUMBER_CHARS = ascii_uppercase + digits

def generate_trip_number(length: int = 10, prefix: bool = True) -> str:
    trp_number = ''.join(choices(TRIP_NUMBER_CHARS, k=length))
    if prefix:
        trp_number = 'TRP' + trp_number
    return trp_number


STATUSES = (('NEW', 'NEW'), ('IN PROGRESS','IN PROGRESS'), ('DELAYED','DELAYED'), ('POSTPONED','POSTPONED'), ('COMPLETED','COMPLETED'))


class WorkOrderTaskModelManager(models.Manager):

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

    def for_wo(self, entity_slug: str, work_order):
        qs = self.get_queryset()
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            Q(work_order=work_order)
        )

class WorkOrderTaskModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    tripno = models.CharField(db_column='tripNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)
    currentstatus = models.CharField(db_column='currentStatus', max_length=255, blank=True, null=True, choices=STATUSES, default="NEW")  # Field name made lowercase.
    weight = models.FloatField(blank=True, null=True)
    tripdistance = models.FloatField(db_column='tripDistance', blank=True, null=True)  # Field name made lowercase.
    fuel = models.FloatField(blank=True, null=True)
    startmileage = models.IntegerField(db_column='startMileage', blank=True, null=True)  # Field name made lowercase.
    endmileage = models.IntegerField(db_column='endMileage', blank=True, null=True)  # Field name made lowercase.
    statusdate = models.DateTimeField(db_column='statusDate', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.

    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('Work Order Task Entity'))
    work_order = models.ForeignKey('aix.WorkOrderModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Work Order'))
    startlocation = models.ForeignKey('aix.CustomerLocationModel', 
                                db_column='StartLocation', 
                                related_name='start_location', 
                                on_delete=models.CASCADE,
                                blank=True, null=True)  # Field name made lowercase.
    endlocation = models.ForeignKey('aix.CustomerLocationModel', 
                                db_column='EndLocation', 
                                related_name='end_location', 
                                on_delete=models.CASCADE,
                                blank=True, null=True)  # Field name made lowercase.

    objects = WorkOrderTaskModelManager()

    class Meta:
        verbose_name = _('Work Order Task')
        indexes = [
            models.Index(fields=['startdate']),
            models.Index(fields=['enddate']),
            models.Index(fields=['currentstatus']),
        ]
        unique_together = [
            ('entity', 'startdate', 'enddate', 'work_order', 'startlocation', 'endlocation')
        ]

    def __str__(self):
        return f'{self.tripno}'

    def configure(self, entity_slug: str or EntityModel, user_model,):
        self.tripno = generate_trip_number()
        return self