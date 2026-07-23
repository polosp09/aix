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

class AssetModelManager(models.Manager):

    def for_entity(self, entity_slug: str, user_model):
        qs = self.get_queryset()
        qs = qs.filter(
            Q(entity__slug__exact=entity_slug) &
            #Q(active=True) &
            (
                    #Q(entity__admin=user_model) |
                    Q(entity__managers__in=[user_model])
            )
        )
        qs = qs.exclude(group_name='CNOOC')
        qs = qs.exclude(group_name='SLB')
        return qs


class AssetModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    vehicle_id = models.IntegerField(unique=True)
    wialon_id = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    license_plate = models.CharField(unique=True, max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    make = models.CharField(max_length=255, blank=True, null=True)
    vehicle_type_name = models.CharField(max_length=255, blank=True, null=True)
    wostatus = models.CharField(db_column='woStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True, null=True)
    imageurl = models.TextField(db_column='imageUrl', blank=True, null=True)  # Field name made lowercase.
    
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('Asset Entity'),
                               related_name='asset')

    objects = AssetModelManager()

    class Meta:
        verbose_name = _('Asset')
        indexes = [
            models.Index(fields=['license_plate']),
            models.Index(fields=['vehicle_type_name']),
            models.Index(fields=['make']),
            models.Index(fields=['model']),
        ]
        unique_together = [
            ('entity', 'license_plate')
        ]

    def __str__(self):
        return f'{self.vehicle_type_name} - {self.license_plate} - {self.name}'
