"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from uuid import uuid4

from string import ascii_uppercase, digits
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from aix.models.mixins import SlugNameMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q

CODE_NUMBER_CHARS = ascii_uppercase + digits

def generate_code(length: int = 10, prefix: bool = True) -> str:
    serial_code = ''.join(choices(CODE_NUMBER_CHARS, k=length))
    if prefix:
        serial_code = 'TRP' + serial_code
    return serial_code

class WorkOrderPersonnelModelManager(models.Manager):

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

class WorkOrderPersonnelModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=100, default='NA')
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    wostatus = models.CharField(db_column='woStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True, null=True)
    deploydate = models.DateField(db_column='deployDate')  # Field name made lowercase.
    relievedate = models.DateField(db_column='relieveDate')  # Field name made lowercase.
    duties = models.TextField(blank=True, null=True)
    
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('Work Order Personnel Entity'))
    work_order = models.ForeignKey('aix.WorkOrderModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Work Order'))
    employee = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Employee'))
    objects = WorkOrderPersonnelModelManager()

    class Meta:
        verbose_name = _('Work Order Personnel')
        indexes = [
            models.Index(fields=['startdate']),
            models.Index(fields=['enddate']),
            models.Index(fields=['status']),
            models.Index(fields=['wostatus']),
        ]
        unique_together = [
            ('entity', 'startdate', 'enddate', 'work_order', 'employee')
        ]

    def __str__(self):
        return f'{self.code}'

    def configure(self, entity_slug: str or EntityModel, user_model,):
        self.serial_code = generate_code()
        return self