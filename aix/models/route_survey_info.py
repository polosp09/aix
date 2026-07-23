"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from uuid import uuid4
from random import choices
from string import ascii_uppercase, digits

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from aix.models.mixins import SlugNameMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q

from location_field.models.plain import PlainLocationField

RQ_NUMBER_CHARS = ascii_uppercase + digits

def generate_rq_number(length: int = 5, prefix: bool = True) -> str:
    rq_number = ''.join(choices(RQ_NUMBER_CHARS, k=length))
    if prefix:
        rq_number = 'RQC' + rq_number
    return rq_number

COLORS = (("RED", "RED"), ("AMBER", "AMBER"), ("GREEN", "GREEN"),)

class RouteSurveyInfoModelManager(models.Manager):

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


class RouteSurveyInfoModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=100)
    route_code = models.CharField(max_length=100)
    south_coordinate = PlainLocationField(zoom=7)
    east_coordinate = PlainLocationField(zoom=7)
    distance_start = models.CharField(max_length=100)
    color = models.CharField(max_length=50, choices=COLORS)
    koc = models.CharField(max_length=50, choices=COLORS)
    kfi_description = models.TextField(blank=True, null=True)
    photo = models.ImageField(
                    upload_to=None,
                    height_field=None,
                    width_field=None,
                    max_length=100
                )
    location = PlainLocationField(based_fields=['south_coordinate'], zoom=7)
    is_active = models.BooleanField(default=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('RouteSurveyInfo Entity'))
    route_survey = models.ForeignKey('aix.RouteSurveyModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('RouteSurvey'),
                                 related_name='route_survey')

    objects = RouteSurveyInfoModelManager()

    class Meta:
        verbose_name = _('RouteSurveyInfo')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['south_coordinate']),
            models.Index(fields=['east_coordinate']),
        ]
        unique_together = [
            ('entity', 'south_coordinate', 'east_coordinate', 'route_survey')
        ]

    def __str__(self):
        return f'Route: {self.code} - {self.south_coordinate} - {self.east_coordinate} - {self.route_survey.name}'

    def configure(self):
        self.code = generate_rq_number()
