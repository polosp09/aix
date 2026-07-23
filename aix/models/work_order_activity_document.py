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

STATUSES = (("DRAFT", "DRAFT"), ("APPROVED","APPROVED"), ("DISABLED","DISABLED"), ("REJECTED","REJECTED"), ("SIGNED","SIGNED"))
CODE_NUMBER_CHARS = ascii_uppercase + digits

def generate_code(length: int = 10, prefix: bool = True) -> str:
    serial_code = ''.join(choices(CODE_NUMBER_CHARS, k=length))
    if prefix:
        serial_code = '' + serial_code
    return serial_code

class WorkOrderActivityDocumentModelManager(models.Manager):

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


class WorkOrderActivityDocumentModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=100, default='NA')
    doc_date = models.DateField(blank=True, null=True) 
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True, choices=STATUSES, default='ACTIVE')
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))
    
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('WorkOrder Type Entity'))

    activity = models.ForeignKey('aix.WorkOrderActivityModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Activity Document'))
    document = models.ForeignKey('aix.DocumentModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Activity Document'),
                                 blank=False, null=False)

    objects = WorkOrderActivityDocumentModelManager()

    class Meta:
        verbose_name = _('Work Order Document')
        indexes = [
            models.Index(fields=['doc_date']),
            models.Index(fields=['description']),
            models.Index(fields=['status']),
        ]
        unique_together = [
            ('entity', 'doc_date', 'activity', 'document', 'status')
        ]

    def __str__(self):
        return f'Activity Document: {self.code}'

    def configure(self, entity_slug: str or EntityModel, user_model,):
        self.code = generate_code()
        return self