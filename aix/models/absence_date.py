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


class AbsenceDateModelManager(models.Manager):

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


class AbsenceDateModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    date = models.DateField()
    is_half_day = models.BooleanField(default=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('AbsenceDate Entity'),
                               related_name='absence_dates')
    absence_type = models.ForeignKey('aix.AbsenceTypeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('AbsenceType'))

    employee = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Employee'))

    objects = AbsenceDateModelManager()

    class Meta:
        verbose_name = _('AbsenceDate')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['date']),
        ]
        unique_together = [
            ('entity', 'date')
        ]

    def __str__(self):
        return f'AbsenceDate: {self.date}'
