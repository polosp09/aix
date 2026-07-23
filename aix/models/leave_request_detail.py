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


class LeaveRequestDetailModelManager(models.Manager):

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


class LeaveRequestDetailModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    total_calendar_days_requested = models.FloatField()
    total_work_days_requested = models.FloatField()
    half_day_used = models.TextField()
    description = models.CharField(max_length=255, blank=True, null=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('LeaveRequestDetail Entity'))
    absence_type = models.ForeignKey('aix.AbsenceTypeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('AbsenceType'))
    leave_request = models.ForeignKey('aix.LeaveRequestModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('LeaveRequest'))

    objects = LeaveRequestDetailModelManager()

    class Meta:
        verbose_name = _('LeaveRequestDetail')
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
        return f'LeaveRequestDetail: {self.start_date}'
