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


class PayrollAdvanceRequestWorkflowActionModelManager(models.Manager):

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


class PayrollAdvanceRequestWorkflowActionModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=100, default='NA')
    name = models.CharField(max_length=100)
    is_processed = models.BooleanField(default=False)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('PayrollAdvanceRequestWorkflowAction Entity'))
    par_action = models.ForeignKey('aix.PayrollAdvanceRequestActionModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('PayrollAdvanceRequestAction'))
    par_workflow = models.ForeignKey('aix.PayrollAdvanceRequestWorkFlowModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('PayrollAdvanceRequestWorkFlow'))
    workflow_action = models.ForeignKey('aix.WorkFlowActionModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('WorkFlowAction'))

    objects = PayrollAdvanceRequestWorkflowActionModelManager()

    class Meta:
        verbose_name = _('PayrollAdvanceRequestWorkflowAction')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
        ]
        unique_together = [
            ('entity', 'code')
        ]

    def __str__(self):
        return f'PayrollAdvanceRequestWorkflowAction: {self.code}'
