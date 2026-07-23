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
TRIP_CODES = (('OPS-TR', 'OPERATIONAL - TRANSPORTATION'), ('OPS-REP', 'OPERATIONAL - REPOSITIONING'), 
            ('OPS-LF', 'OPERATIONAL - LIFTING'), ('STB', 'STANDBY'), ('BRKD', 'BREAKDOWN') , 
            ('OFF-HIRE', 'OFF-HIRE')) 
STATUSES = (('New',"New"), ('Mobilizing',"Mobilizing"), ('Progress',"In Progress"), ('Completed',"Completed"), )

def generate_code(length: int = 10, prefix: bool = True) -> str:
    serial_code = ''.join(choices(CODE_NUMBER_CHARS, k=length))
    if prefix:
        serial_code = '' + serial_code
    return serial_code

class WorkOrderActivityLiftingModelManager(models.Manager):

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


class WorkOrderActivityLiftingModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=100, default='NA')
    trip_code = models.CharField(choices=TRIP_CODES, max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True, choices=STATUSES, default='NEW')
    comments = models.TextField(blank=True, null=True)
    
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('Work Order Lifting Entity'))
    activity = models.ForeignKey('aix.WorkOrderActivityModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Activity'))
    from_location = models.ForeignKey('aix.CustomerLocationModel', 
                                db_column='FromLocation', 
                                related_name='from_location_lifting', 
                                on_delete=models.CASCADE,
                                blank=True, null=True)  # Field name made lowercase.
    to_location = models.ForeignKey('aix.CustomerLocationModel', 
                                db_column='ToLocation', 
                                related_name='to_location_lifting', 
                                on_delete=models.CASCADE,
                                blank=True, null=True)  # Field name made lowercase.
    operator = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 related_name='operator_lifting',
                                 verbose_name=_('Operator'))
    supervisor = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 related_name='supervisor_lifting',
                                 verbose_name=_('Supervisor'))
    equipment = models.ForeignKey('aix.AssetModel',
                                 on_delete=models.RESTRICT,
                                 related_name='equipment_lifting',
                                 verbose_name=_('Equipment'))
    operators = models.ManyToManyField('aix.EmployeeModel',
                                 related_name='operators_lifting',
                                 verbose_name=_('Operators'), 
                                 blank=True)
    # driver = models.ForeignKey('aix.EmployeeModel',

    objects = WorkOrderActivityLiftingModelManager()

    class Meta:
        verbose_name = _('Work Order Lifting')
        indexes = [
            models.Index(fields=['trip_code']),
            models.Index(fields=['comments']),
            models.Index(fields=['status']),
        ]
        unique_together = [
            ('entity', 'activity', 'trip_code', 'operator', 'equipment')
        ]

    def __str__(self):
        return f'Activity Lifting: {self.code} - {self.trip_code} - {self.operator} - {self.equipment} - {self.activity}`' 

    def configure(self, entity_slug: str or EntityModel, user_model,):
        self.code = generate_code()
        return self