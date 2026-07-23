"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""
from random import choices
from string import ascii_uppercase, digits
from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from aix.models.mixins import ContactInfoMixIn, CreateUpdateMixIn

UserModel = get_user_model()
CODE_NUMBER_CHARS = ascii_uppercase + digits

def generate_code_number(length: int = 10, prefix: bool = True) -> str:
    jobcard_number = ''.join(choices(CODE_NUMBER_CHARS, k=length))
    if prefix:
        jobcard_number = 'EQAS' + jobcard_number
    return jobcard_number

class EquipmentAssignmentModelManager(models.Manager):

    def for_entity(self, entity_slug: str, user_model):
        qs = self.get_queryset()
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            Q(active=True) &
            (
                    #Q(entity__admin=user_model) |
                    Q(entity__managers__in=[user_model])
            )
        )


class EquipmentAssignmentModel(ContactInfoMixIn, CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)
    is_supervisor = models.BooleanField(default=False)    
    is_assistant = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    entity = models.ForeignKey('aix.EntityModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('EquipmentAssignment Entity'),
                               related_name='equipment_assignment_entity')
    equipment = models.ForeignKey('aix.EquipmentModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('Equipment'))
    operator = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Employee'))

    objects = EquipmentAssignmentModelManager()

    class Meta:
        verbose_name = _('Equipment Assignment')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['is_active']),
        ]
        unique_together = [
            ('entity', 'date', 'equipment', 'operator')
        ]

    def __str__(self):
        return f'Equip.Assignment: {self.date}-{self.equipment.reg_no}-{self.operator}'

    def configure(self,
                  entity_slug: str or EntityModel,
                  user_model: UserModel,
                  post_ledger: bool = False):

        if isinstance(entity_slug, str):
            entity_qs = EntityModel.objects.for_user(
                user_model=user_model)
            entity_model: EntityModel = get_object_or_404(entity_qs, slug__exact=entity_slug)
        elif isinstance(entity_slug, EntityModel):
            entity_model = entity_slug
        else:
            raise ValidationError('entity_slug must be an instance of str or EntityModel')

        if not self.code:
            self.code = generate_code_number()
