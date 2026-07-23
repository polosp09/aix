"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from uuid import uuid4

from random import choices
from string import ascii_uppercase, digits
from django.utils.dateparse import parse_datetime
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from aix.models.mixins import SlugNameMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q

STATUSES = (('new',"New"), ('mobilizing',"Mobilizing"), ('progress',"In Progress"), ('completed',"Completed"), )
CODE_NUMBER_CHARS = ascii_uppercase + digits

def generate_code(length: int = 10, prefix: bool = True) -> str:
    serial_code = ''.join(choices(CODE_NUMBER_CHARS, k=length))
    if prefix:
        serial_code = 'HSE' + serial_code
    return serial_code

class KpiHseModelManager(models.Manager):

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


class KpiHseModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(unique=True, max_length=255)
    activity_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.FloatField(default=0.00,blank=True, null=True)
    fat = models.IntegerField(blank=True, null=True)
    lti = models.IntegerField(blank=True, null=True)
    rwdc = models.IntegerField(blank=True, null=True)
    mtc = models.IntegerField(blank=True, null=True)
    fac = models.IntegerField(blank=True, null=True)
    hipo = models.IntegerField(blank=True, null=True)
    envdam = models.IntegerField(blank=True, null=True)
    nmi = models.IntegerField(blank=True, null=True)
    matloss = models.IntegerField(blank=True, null=True)
    ptw = models.IntegerField(blank=True, null=True)
    ptw_description = models.TextField(blank=True, null=True)
    tbt = models.IntegerField(blank=True, null=True)
    tbt_description = models.TextField(blank=True, null=True)
    hht = models.IntegerField(blank=True, null=True)
    hht_description = models.TextField(blank=True, null=True)
    drills = models.IntegerField(blank=True, null=True)
    drills_description = models.TextField(blank=True, null=True)
    audit = models.IntegerField(blank=True, null=True)
    audit_description = models.TextField(blank=True, null=True)
    training_subject = models.CharField(max_length=255, blank=True, null=True)
    reporting_cards = models.IntegerField(blank=True, null=True)
    rc_description = models.CharField(max_length=255, blank=True, null=True)
    safety_initiative = models.IntegerField(blank=True, null=True)
    si_description = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(choices=STATUSES, max_length=255, blank=True, null=True)
    

    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('KpiHse Entity'),
                               related_name='kpihses')

    objects = KpiHseModelManager()

    class Meta:
        verbose_name = _('KpiHse')
        indexes = [
            models.Index(fields=['activity_date']),
            models.Index(fields=['status']),
        ]
        unique_together = [
            ('entity', 'code')
        ]

    def __str__(self):
        return f'KpiHse: {self.code}'

    def configure(self, entity_slug: str or EntityModel, user_model,):
        self.code = generate_code()
        return self
    
    def configure_times(self, entity_slug: str or EntityModel, user_model,):
        date_format = "%m/%d/%Y %HH:%MM:%SS"
        st = f'{self.activity_date} {self.start_time}'
        et = f'{self.activity_date} {self.end_time}'
        
        stt = parse_datetime(st)
        ett = parse_datetime(et)
        
        dur = ett - stt
        self.duration = dur.seconds
        return self