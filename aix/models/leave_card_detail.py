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


class LeaveCardDetailModelManager(models.Manager):

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


class LeaveCardDetailModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    credit = models.FloatField()
    days_used = models.FloatField()
    days_advanced = models.FloatField()
    balance = models.FloatField()
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('LeaveCardDetail Entity'))
    leave_card = models.ForeignKey('aix.LeaveCardModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('LeaveCard'))
    absence_type = models.ForeignKey('aix.AbsenceTypeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('AbsenceType'))

    objects = LeaveCardDetailModelManager()

    class Meta:
        verbose_name = _('LeaveCardDetail')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
        ]
        unique_together = [
            ('entity', 'credit')
        ]

    def __str__(self):
        return f'LeaveCardDetail: {self.credit}'
