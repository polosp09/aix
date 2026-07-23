"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from uuid import uuid4
from random import choices
from string import ascii_uppercase, digits

from django.shortcuts import get_object_or_404
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from aix.models.mixins import ContactInfoMixIn, CreateUpdateMixIn
from aix.models.entity import EntityModel

UserModel = get_user_model()
CODE_NUMBER_CHARS = ascii_uppercase + digits

def generate_code_number(length: int = 10, prefix: bool = True) -> str:
    code_number = ''.join(choices(CODE_NUMBER_CHARS, k=length))
    if prefix:
        code_number = 'EQ' + code_number
    return code_number

class EquipmentModelManager(models.Manager):

    def for_entity(self, entity_slug: str, user_model):
        qs = self.get_queryset()
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            # Q(active=True) &
            (
                    #Q(entity__admin=user_model) |
                    Q(entity__managers__in=[user_model])
            )
        )


class EquipmentModel(ContactInfoMixIn, CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(unique=True, max_length=255) 
    reg_no = models.CharField(null=True, max_length=255) 
    serial = models.CharField(unique=True, max_length=255) 
    yom = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=255)
    status = models.CharField(max_length=255, blank=True, null=True)
    details = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)

    
    entity = models.ForeignKey('aix.EntityModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('Equipment Entity'),
                               related_name='equipment_entity')
    eq_manufacturer = models.ForeignKey('aix.EquipmentManufacturerModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('Equipment Manufacturer'))
    eq_type = models.ForeignKey('aix.EquipmentTypeModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('Equipment Type'))
    asset = models.ForeignKey('aix.AssetModel',
                                 null=True,
                                 blank=True,
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Asset'))

    objects = EquipmentModelManager()

    class Meta:
        verbose_name = _('Equipment')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['active']),
        ]
        unique_together = [
            ('entity', 'reg_no')
        ]

    def __str__(self):
        return f'{self.serial} - {self.eq_type.name}'

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