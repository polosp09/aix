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

STATUSES = (('DRAFT', 'DRAFT'), ('APPROVED','APPROVED'))
USES = (('OFFICIAL','OFFICIAL'), ('PERSONAL', 'PERSONAL'))

class AixItsHandOverModelManager(models.Manager):

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


class AixItsHandOverModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=100, default='NA')
    equipment_condition = models.CharField(max_length=100)
    proper_use = models.CharField(max_length=255, blank=True, null=True, choices=USES, default="OFFICAL")  # Field name made lowercase.
    description = models.TextField()
    issue_date = models.DateField(db_column='issueDate', blank=True, null=True)  # Field name made lowercase.
    return_date = models.DateField(db_column='returnDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True, null=True, choices=STATUSES, default="APPROVED")  # Field name made lowercase.
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('Entity'))
    equipment = models.ForeignKey('aix.EquipmentModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('Equipment'),
                               related_name='equipment')
    staff = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Staff'))

    objects = AixItsHandOverModelManager()

    class Meta:
        verbose_name = _('Systems Support Status')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
        ]
        unique_together = [
            ('entity', 'equipment', 'staff', 'status')
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