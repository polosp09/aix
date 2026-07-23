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


class TaskModelManager(models.Manager):

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


class TaskModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    task_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    case_status = models.CharField(max_length=255)
    due_at = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    estimated_time = models.CharField(max_length=255, blank=True, null=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('Task Entity'))
    task_status = models.ForeignKey('aix.TaskStatusModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Task Status'))

    objects = TaskModelManager()

    class Meta:
        verbose_name = _('Task')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
        ]
        unique_together = [
            ('entity', 'task_name')
        ]

    def __str__(self):
        return f'Task: {self.task_name}'
