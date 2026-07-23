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


class EmployeeAssignmentModelManager(models.Manager):

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

class EmployeeAssignmentModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('EmployeeAssignment Entity'))
    employee = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Employee'))
    job = models.ForeignKey('aix.JobModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Job'))
                               
    objects = EmployeeAssignmentModelManager()

    class Meta:
        verbose_name = _('EmployeeAssignment')
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
        return f'EmployeeAssignment: {self.start_date}'
