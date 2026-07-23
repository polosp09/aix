"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from uuid import uuid4

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from aix.models.mixins import SlugNameMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q


class IncomingDocumentModelManager(models.Manager):

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


class IncomingDocumentModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    doc_from = models.CharField(max_length=255) 
    subject = models.CharField(max_length=255, blank=True, null=True)
    delivered_by = models.CharField(max_length=255, blank=True, null=True)
    date_written = models.DateField(blank=True, null=True)
    date_received = models.DateField()
    comment = models.TextField(blank=True, null=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('IncomingDocument Entity'))
    doc_type = models.ForeignKey('aix.IncomingDocumentTypeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('IncomingDocumentType'))
    received_by = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Recieved-By'))
                               
    objects = IncomingDocumentModelManager()

    class Meta:
        verbose_name = _('IncomingDocument')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['doc_from']),
            models.Index(fields=['subject']),
        ]
        unique_together = [
            ('entity', 'doc_from')
        ]

    def __str__(self):
        return f'IncomingDocument: {self.subject}'
