"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""
from datetime import datetime
from uuid import uuid4

from random import choices
from string import ascii_uppercase, digits
from django.utils.dateparse import parse_datetime
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from aix.models.mixins import SlugNameMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q
from aix.models import EntityModel

WORK_CODES = (('OPS-TR', 'OPERATIONAL - TRANSPORTATION'), ('OPS-REP', 'OPERATIONAL - REPOSITIONING'), 
            ('OPS-LF', 'OPERATIONAL - LIFTING'), ('STB', 'STANDBY'), ('BRKD', 'BREAKDOWN') , 
            ('OFF-HIRE', 'OFF-HIRE')) 
STATUSES = (('New',"New"), ('Mobilizing',"Mobilizing"), ('Progress',"In Progress"), ('Completed',"Completed"), )

CODE_NUMBER_CHARS = ascii_uppercase + digits

def generate_code(length: int = 10, prefix: bool = True) -> str:
    serial_code = ''.join(choices(CODE_NUMBER_CHARS, k=length))
    if prefix:
        serial_code = 'OPS' + serial_code
    return serial_code

class WorkOrderActivityModelManager(models.Manager):

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
    
    def for_wo(self, entity_slug, user_model, work_order):
        qs = self.get_queryset()
        qs = qs.filter(
                Q(entity__slug__exact=entity_slug) &
                #Q(active=True) &
                (
                        #Q(entity__admin=user_model) |
                        Q(entity__managers__in=[user_model])
                ))
        qs = qs.filter(task__work_order=work_order)
        return qs

    def for_task(self, entity_slug, user_model, task):
        qs = self.get_queryset()
        qs = qs.filter(
                Q(entity__slug__exact=entity_slug) &
                #Q(active=True) &
                (
                        #Q(entity__admin=user_model) |
                        Q(entity__managers__in=[user_model])
                ))
        
        qs = qs.filter(task_id=task.uuid)
        return qs


class WorkOrderActivityModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    activity_date = models.DateField(blank=True, null=True)
    activity_description = models.TextField(blank=True, null=True)
    work_code = models.CharField(choices=WORK_CODES, max_length=255, blank=True, null=True)
    etd = models.CharField(max_length=255, blank=True, null=True)
    eta = models.CharField(max_length=255, blank=True, null=True)
    atd = models.CharField(max_length=255, blank=True, null=True)
    ata = models.CharField(max_length=255, blank=True, null=True)
    etp = models.FloatField(default=0.00,blank=True, null=True)
    atp = models.FloatField(default=0.00,blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(choices=STATUSES, default="New", max_length=255, blank=True, null=True)
    is_work_location = models.BooleanField(default=True)

    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('WorkOrderActivity Entity'),
                               related_name='activities')

    from_location = models.ForeignKey('aix.CustomerLocationModel', 
                                db_column='FromLocation', 
                                related_name='activity_from_location', 
                                on_delete=models.CASCADE,
                                blank=True, null=True)  # Field name made lowercase.
    to_location = models.ForeignKey('aix.CustomerLocationModel', 
                                db_column='ToLocation', 
                                related_name='activity_to_location', 
                                on_delete=models.CASCADE,
                                blank=True, null=True)  # Field name made lowercase.
    task = models.ForeignKey('aix.WorkOrderTaskModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Task'))

    objects = WorkOrderActivityModelManager()

    class Meta:
        verbose_name = _('WorkOrderActivity')
        indexes = [
            models.Index(fields=['activity_date']),
            models.Index(fields=['activity_description']),
            models.Index(fields=['comments']),
            models.Index(fields=['status']),
        ]
        unique_together = [
            ('entity', 'activity_date', 'from_location', 'to_location', 'task')
        ]

    def __str__(self):
        return f'Work Order Activity: {self.code} on {self.activity_date} for {self.task}'

    def configure(self, entity_slug: str or EntityModel, user_model,):
        self.code = generate_code()
        return self
    
    def configure_times(self, entity_slug: str or EntityModel, user_model,):
        date_format = "%m/%d/%Y %HH:%MM:%SS"
        eta = f'{self.activity_date} {self.eta}'
        etd = f'{self.activity_date} {self.etd}'
        atd = f'{self.activity_date} {self.atd}'
        ata = f'{self.activity_date} {self.ata}'
        # etp = datetime.strftime(eta, '%d-%M-%Y %H:%M:%S')
        # atp = datetime.strftime(eta, '%d-%M-%Y %H:%M:%S')
        etat = parse_datetime(eta)
        etdt = parse_datetime(etd)
        atdt = parse_datetime(atd)
        atat = parse_datetime(ata)
        # a = datetime.strptime(str(etat), date_format)
        # b = datetime.strptime(str(etdt), date_format)
        # print(etat, etdt, atdt, atat)
        etp = etdt - etat
        atp = atdt - atat
        self.etp = etp.seconds
        self.atp = atp.seconds
        # self.etp = b - a
        # self.atp = atp
        return self