"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from uuid import uuid4
from random import choices
from string import ascii_uppercase, digits
from typing import Tuple, List, Union

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from aix.models.mixins import SlugNameMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q, QuerySet, Count
# from django_google_maps import fields as map_fields
# from map_location.fields import LocationField
from location_field.models.plain import PlainLocationField

RQ_NUMBER_CHARS = ascii_uppercase + digits

def generate_rq_number(length: int = 5, prefix: bool = True) -> str:
    rq_number = ''.join(choices(RQ_NUMBER_CHARS, k=length))
    if prefix:
        rq_number = 'RSV' + rq_number
    return rq_number

class RouteSurveyModelManager(models.Manager):

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

class RouteSurveyModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    start_place = models.CharField(max_length=200)
    via_place = models.CharField(max_length=200)
    end_place = models.CharField(max_length=200)
    start_gps = PlainLocationField(based_fields=['start_place'], zoom=7)
    via_gps = PlainLocationField(based_fields=['via_place'], zoom=7)
    end_gps = PlainLocationField(based_fields=['end_gps'], zoom=7)
    location = PlainLocationField(based_fields=['end_gps'], zoom=7)

    # location = LocationField('Pos', blank=True, null=True, options={
    #     'map': {
    #         'center': [52.52, 13.40],
    #         'zoom': 12,
    #     },
    #     # 'markerZoom': 18
    #     # 'tileLayer': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    #     # 'tileOptions': {
    #     #     attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    #     # },
    #     # 'locate': {
    #     #     'showPopup': False,
    #     # },
    # })
    purpose = models.TextField(blank=True, null=True)
    general_notes = models.TextField(blank=True, null=True)
    bo1 = models.TextField(blank=True, null=True)
    bo2 = models.TextField(blank=True, null=True)
    bo3 = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('RouteSurvey Entity'))

    objects = RouteSurveyModelManager()

    class Meta:
        verbose_name = _('RouteSurvey')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['start_gps']),
            models.Index(fields=['end_gps']),
        ]
        unique_together = [
            ('entity', 'start_date', 'end_date', 'start_place', 'end_place')
        ]

    def __str__(self):
        return f'Route: {self.code} - {self.start_place} - {self.end_place}'

    def configure(self, entity_slug, user_model):
        self.code = generate_rq_number()

    # State Update...
    def get_rs_item_data(self, queryset: QuerySet = None) -> Tuple:
        # if not queryset:
        #     # pylint: disable=no-member
        #     queryset = RouteSurveyInfoModel.all().select_related('route_survey')

        return queryset, queryset.aggregate(
            total_items=Count('uuid')
        )
