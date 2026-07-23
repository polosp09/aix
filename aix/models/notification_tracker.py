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


class NotificationTrackerModelManager(models.Manager):

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


class NotificationTrackerModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    next_notification = models.DateField()
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('NotificationTracker Entity'))
    #calendar_event = models.ForeignKey('aix.CalendarEventModel',
    #                             on_delete=models.RESTRICT,
    #                             verbose_name=_('CalendarEvent'))

    objects = NotificationTrackerModelManager()

    class Meta:
        verbose_name = _('NotificationTracker')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
        ]
        unique_together = [
            ('entity', 'next_notification')
        ]

    def __str__(self):
        return f'NotificationTracker: {self.next_notification}'
