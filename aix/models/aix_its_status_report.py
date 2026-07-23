"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from uuid import uuid4
from random import choices
from string import ascii_uppercase, digits

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _

from aix.models.entity import EntityModel
from aix.models.mixins import SlugNameMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q

UserModel = get_user_model()
CODE_NUMBER_CHARS = ascii_uppercase + digits
AIX_NUMBER_CHARS = ascii_uppercase + digits

def generate_aix_number(length: int = 10, prefix: bool = True) -> str:
    aix_number = ''.join(choices(AIX_NUMBER_CHARS, k=length))
    if prefix:
        aix_number = 'AIX' + aix_number
    return aix_number

STATUSES = (('NEW', 'NEW'), ('IN PROGRESS','IN PROGRESS'), ('DELAYED','DELAYED'), ('POSTPONED','POSTPONED'), ('COMPLETED','COMPLETED'))
PRIORITIES = (('IMMEDIATE','IMMEDIATE'), ('LONG TERM', 'LONG TERM'), ('SHORT TERM','SHORT TERM'), ('QUARTERLY','QUARTERLY'), ('YEARLY','YEARLY'))
TYPES = (('General', 'General'), ('IT Support','IT Support'), ('Troubleshooting','Troubleshooting'))

class AixItsStatusReportModelManager(models.Manager):

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


class AixItsStatusReportModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=100, default='NA')
    activity = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=255, blank=True, null=True, choices=TYPES, default="IMMEDIATE")  # Field name made lowercase.
    description = models.TextField()
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateField(db_column='dueDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True, null=True, choices=STATUSES, default="IN PROGRESS")  # Field name made lowercase.
    priority = models.CharField(max_length=255, blank=True, null=True, choices=PRIORITIES, default="General")  # Field name made lowercase.
    is_active = models.BooleanField(default=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('Entity'))

    objects = AixItsStatusReportModelManager()

    class Meta:
        verbose_name = _('Systems Support Status')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['activity']),
        ]
        unique_together = [
            ('entity', 'activity', 'status')
        ]

    def __str__(self):
        return f'{self.activity} - {self.status}'

    def configure(self,
                  entity_slug: str or EntityModel,
                  user_model: UserModel):

        if isinstance(entity_slug, str):
            entity_qs = EntityModel.objects.for_user(
                user_model=user_model)
            entity_model: EntityModel = get_object_or_404(entity_qs, slug__exact=entity_slug)
        elif isinstance(entity_slug, EntityModel):
            entity_model = entity_slug
        else:
            raise ValidationError('entity_slug must be an instance of str or EntityModel')

        self.code = generate_aix_number()