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


class LeaveCardModelManager(models.Manager):

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

    def for_employee(self, entity_slug, user_model, employee):
        qs = self.get_queryset()
        qs = qs.filter(
            #Q(entity__admin=user_model) |
            Q(entity__managers__in=[user_model])
        )
        qs = qs.filter(employee=employee)
        return qs


class LeaveCardModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    is_dirty = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    parent_id = models.IntegerField(default=0, blank=True, null=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('LeaveCard Entity'))
    employee = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Employee'))

    objects = LeaveCardModelManager()

    class Meta:
        verbose_name = _('LeaveCard')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['start_date']),
            models.Index(fields=['end_date']),
        ]
        unique_together = [
            ('entity', 'start_date')
        ]

    def __str__(self):
        return f'LeaveCard: {self.start_date}'
