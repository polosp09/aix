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


class LeaveRequestWorkflowActionModelManager(models.Manager):

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


class LeaveRequestWorkflowActionModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    is_processed = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True, null=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('LeaveRequestWorkflowAction Entity'))
    leave_request_action = models.ForeignKey('aix.LeaveRequestActionModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('LeaveRequestAction'))
    workflow_action = models.ForeignKey('aix.WorkFlowActionModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('WorkFlowAction'))
    workflow = models.ForeignKey('aix.WorkFlowModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('WorkFlow'))

    objects = LeaveRequestWorkflowActionModelManager()

    class Meta:
        verbose_name = _('LeaveRequestWorkflowAction')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['name']),
        ]
        unique_together = [
            ('entity', 'name')
        ]

    def __str__(self):
        return f'LeaveRequestWorkflowAction: {self.name}'
