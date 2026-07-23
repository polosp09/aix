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


class ReceivedEmailDocumentModelManager(models.Manager):

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


class ReceivedEmailDocumentModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    doc_from = models.TextField() 
    doc_subject = models.TextField()
    doc_body = models.TextField()
    processed = models.IntegerField(default=0)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('ReceivedEmailDocument Entity'))

    objects = ReceivedEmailDocumentModelManager()

    class Meta:
        verbose_name = _('ReceivedEmailDocument')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['doc_from']),
            models.Index(fields=['doc_subject']),
        ]
        unique_together = [
            ('entity', 'doc_from')
        ]

    def __str__(self):
        return f'ReceivedEmailDocument: {self.doc_from}'
