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


class LeaveRequestWorkflowModelManager(models.Manager):

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


class LeaveRequestWorkflowModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('LeaveRequestWorkflow Entity'))
    leave_request = models.ForeignKey('aix.LeaveRequestModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('LeaveRequest'))
    workflow_status = models.ForeignKey('aix.WorkFlowStatusModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('WorkFlowStatus'))
    workflow = models.ForeignKey('aix.WorkFlowModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('WorkFlow'))

    objects = LeaveRequestWorkflowModelManager()

    class Meta:
        verbose_name = _('LeaveRequestWorkflow')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
        ]
        unique_together = [
            ('entity', 'workflow', 'workflow_status', 'leave_request')
        ]

    def __str__(self):
        return f'LeaveRequestWorkflow: {self.leave_request.name}'
