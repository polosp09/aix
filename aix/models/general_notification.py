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


class GeneralNotificationModelManager(models.Manager):

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


class GeneralNotificationModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    link = models.TextField(blank=True, null=True)
    parameter = models.TextField(blank=True, null=True)
    extra_parameter = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=100)
    date = models.DateField()
    is_read = models.BooleanField(default=False)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('GeneralNotification Entity'))
    employee = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Employee'))
    notification_external_type = models.ForeignKey('aix.NotificationExternalTypeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('NotificationExternalType'))

    objects = GeneralNotificationModelManager()

    class Meta:
        verbose_name = _('GeneralNotification')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['link']),
        ]
        unique_together = [
            ('entity', 'title')
        ]

    def __str__(self):
        return f'GeneralNotification: {self.title}'
