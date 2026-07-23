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


class DependantModelManager(models.Manager):

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


class DependantModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.IntegerField(default=0)
    address = models.CharField(max_length=255, blank=True, null=True)
    is_default = models.BooleanField(default=False)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('Dependant Entity'))
    relationship = models.ForeignKey('aix.RelationshipModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Relationship'))
    employee = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('EmployeeStatus'))

    objects = DependantModelManager()

    class Meta:
        verbose_name = _('Dependant')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['first_name']),
            models.Index(fields=['last_name']),
        ]
        unique_together = [
            ('entity', 'first_name')
        ]

    def __str__(self):
        return f'Dependant: {self.first_name} - {self.last_name}'
