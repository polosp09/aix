"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from uuid import uuid4
from random import choices
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from string import ascii_uppercase, digits

from aix.models.mixins import SlugNameMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q

UserModel = get_user_model()
CODE_NUMBER_CHARS = ascii_uppercase + digits

def generate_code(length: int = 10, prefix: bool = True) -> str:
    code = ''.join(choices(CODE_NUMBER_CHARS, k=length))
    if prefix:
        code = 'FET' + code
    return code

class DocumentModelManager(models.Manager):

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
            Q(work_order=work_order) &
            #Q(active=True) &
            (
                    #Q(entity__admin=user_model) |
                    Q(entity__managers__in=[user_model])
            )
        )
    
    def for_task(self, entity_slug: str, user_model, task):
        qs = self.get_queryset()
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            Q(task=task) &
            #Q(active=True) &
            (
                    #Q(entity__admin=user_model) |
                    Q(entity__managers__in=[user_model])
            )
        )
    def for_activity(self, entity_slug: str, user_model, work_order_activity):
        qs = self.get_queryset()
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            Q(activity=work_order_activity) &
            #Q(active=True) &
            (
                    #Q(entity__admin=user_model) |
                    Q(entity__managers__in=[user_model])
            )
        )

class DocumentModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    extension = models.CharField(max_length=255)
    name_on_file = models.CharField(max_length=255, blank=True, null=True)
    temp_key = models.CharField(max_length=255, blank=True, null=True)
    external_key = models.IntegerField(default=0, blank=True, null=True)
    mime_type = models.CharField(max_length=255, blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('Document Entity'))
    doc_status = models.ForeignKey('aix.DocumentStatusModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('DocumentStatus'))
    doc_type = models.ForeignKey('aix.DocumentTypeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('DocumentType'))
    
    work_order = models.ForeignKey('aix.WorkOrderModel',
                                 on_delete=models.RESTRICT,
                                 blank=True, null=True,
                                 verbose_name=_('Work Order'))
    task = models.ForeignKey('aix.WorkOrderTaskModel',
                                 on_delete=models.RESTRICT,
                                 blank=True, null=True,
                                 verbose_name=_('Task'))
    activity = models.ForeignKey('aix.WorkOrderActivityModel',
                                 on_delete=models.RESTRICT,
                                 blank=True, null=True,
                                 verbose_name=_('Activity'))

    objects = DocumentModelManager()

    class Meta:
        verbose_name = _('Document')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['name']),
            models.Index(fields=['name_on_file']),
        ]
        unique_together = [
            ('entity', 'name', 'updated')
        ]

    def __str__(self):
        return f'Document: {self.name} - {self.updated}'

    def configure(self, entity_slug: str or EntityModel, user_model,):
        self.code = generate_code()
        return self
