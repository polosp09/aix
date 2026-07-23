"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from uuid import uuid4

from random import choices
from string import ascii_uppercase, digits
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from aix.models.mixins import SlugNameMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q

MAINTENANCE = (('5000 kms','5000 kms'), ('10000 kms','10000 kms'), ('200hrs','200hrs'), ('250hrs','250hrs'), ('Daily','Daily'), )
ALLOCATIONS = (('SN', "SN"), ('NN', "NN"), )
STATUSES = (('New',"New"), ('Mobilizing',"Mobilizing"), ('Progress',"In Progress"), ('Completed',"Completed"), )
CODE_NUMBER_CHARS = ascii_uppercase + digits

def generate_code(length: int = 10, prefix: bool = True) -> str:
    serial_code = ''.join(choices(CODE_NUMBER_CHARS, k=length))
    if prefix:
        serial_code = 'OFE' + serial_code
    return serial_code

class KpiOnOffModelManager(models.Manager):

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
        qs = qs.filter(
            Q(entity__slug__exact=entity_slug) &
            #Q(active=True) &
            (
                    #Q(entity__admin=user_model) |
                    Q(entity__managers__in=[user_model])
            )
        )
        return qs.filter(task__work_order=work_order)

    def for_task(self, entity_slug, user_model, task):
        qs = self.get_queryset()
        qs = qs.filter(
            Q(entity__slug__exact=entity_slug) &
            #Q(active=True) &
            (
                    #Q(entity__admin=user_model) |
                    Q(entity__managers__in=[user_model])
            )
        )
        return qs.filter(task=task)

class KpiOnOffModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    activity_date = models.DateField(blank=True, null=True)
    activity_description = models.TextField(blank=True, null=True)
    on_hire = models.CharField(max_length=255, blank=True, null=True)
    off_hire = models.CharField(max_length=255, blank=True, null=True)
    maintenance = models.CharField(choices=MAINTENANCE, max_length=255, blank=True, null=True)
    allocation = models.CharField(choices=ALLOCATIONS, max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    status = models.CharField(choices=STATUSES, default="New", max_length=255, blank=True, null=True)

    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('KpiOnOff Entity'),
                               related_name='kpionoffs')
    task = models.ForeignKey('aix.WorkOrderTaskModel',
                                 on_delete=models.RESTRICT,
                                 blank=True, 
                                 null=True,
                                 verbose_name=_('Work Order Task'))
    asset = models.ForeignKey('aix.AssetModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Asset'))
    location = models.ForeignKey('aix.CustomerLocationModel',
                               on_delete=models.RESTRICT,
                               verbose_name=_('Customer Location'))

    objects = KpiOnOffModelManager()

    class Meta:
        verbose_name = _('KpiOnOff')
        indexes = [
            models.Index(fields=['activity_date']),
            models.Index(fields=['activity_description']),
            models.Index(fields=['status']),
        ]
        unique_together = [
            ('entity', 'code')
        ]

    def __str__(self):
        return f'KpiOnOff: {self.code}'

    def configure(self, entity_slug: str or EntityModel, user_model,):
        self.code = generate_code()
        return self