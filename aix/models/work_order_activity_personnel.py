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
STATUSES = (("ACTIVE","ACTIVE"), ("DISABLED", "DISABLED"))

def generate_code(length: int = 10, prefix: bool = True) -> str:
    serial_code = ''.join(choices(CODE_NUMBER_CHARS, k=length))
    if prefix:
        serial_code = '' + serial_code
    return serial_code

class WorkOrderActivityPersonnelModelManager(models.Manager):

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
            Q(activity__task__work_order=work_order)
        )

    def for_activity(self, entity_slug: str, work_order_activity):
        qs = self.get_queryset()
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            Q(activity=work_order_activity)
        )


class WorkOrderActivityPersonnelModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=100, default='NA')
    start_date = models.DateField(blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateField(blank=True, null=True)  # Field name made lowercase.
    wostatus = models.CharField(max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True, null=True, choices=STATUSES, default='ACTIVE')
    deploy_date = models.DateField()  # Field name made lowercase.
    relieve_date = models.DateField()  # Field name made lowercase.
    duties = models.TextField(blank=True, null=True)
    
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('Work Order Personnel Entity'))
    activity = models.ForeignKey('aix.WorkOrderActivityModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Activity'))
    employee = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Employee'))

    objects = WorkOrderActivityPersonnelModelManager()

    class Meta:
        verbose_name = _('Work Order Personnel')
        indexes = [
            models.Index(fields=['start_date']),
            models.Index(fields=['end_date']),
            models.Index(fields=['status']),
        ]
        unique_together = [
            ('entity', 'start_date', 'end_date', 'activity', 'employee')
        ]

    def __str__(self):
        return f'Activity Personnel: {self.code} from {self.start_date} to {self.end_date} for {self.activity}'

    def configure(self, entity_slug: str or EntityModel, user_model,):
        self.code = generate_code()
        return self