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


class WorkflowActionModelManager(models.Manager):

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


class WorkflowActionModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=100)
    document_code = models.CharField(max_length=100, blank=True, null=True)
    form_name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    action_code = models.CharField(max_length=100, blank=True, null=True)
    is_visible = models.IntegerField(default=0)
    is_form = models.IntegerField(default=0)
    has_documents = models.IntegerField(default=0)
    stops_flow = models.IntegerField(default=0)
    permission = models.CharField(max_length=255, blank=True, null=True)
    value = models.IntegerField(default=0)
    parent_id = models.IntegerField(default=0, blank=True, null=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('WorkflowAction Entity'))
    workflow = models.ForeignKey('aix.WorkFlowModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('WorkFlow'))
    workflow_action_type = models.ForeignKey('aix.WorkFlowActionTypeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('WorkFlowActionType'))

    objects = WorkflowActionModelManager()

    class Meta:
        verbose_name = _('WorkflowAction')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['title']),
        ]
        unique_together = [
            ('entity', 'title')
        ]

    def __str__(self):
        return f'WorkflowAction: {self.title}'
