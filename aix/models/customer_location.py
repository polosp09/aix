"""
Contributions to this module:
Mando <mandonpolo@gmail.com>
"""

from uuid import uuid4
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from string import ascii_uppercase, digits

from aix.models.mixins import SlugNameMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q

UserModel = get_user_model()
CODE_NUMBER_CHARS = ascii_uppercase + digits

def generate_code(length: int = 10, prefix: bool = True) -> str:
    code = ''.join(choices(CODE_NUMBER_CHARS, k=length))
    if prefix:
        code = 'FET' + code
    return code

class CustomerLocationModelManager(models.Manager):

    def for_entity(self, entity_slug: str, user_model):
        qs = self.get_queryset()
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            Q(is_active=True) &
            Q(entity__managers__in=[user_model])
            # (
            #         Q(entity__admin=user_model) |
            #         Q(entity__managers__in=[user_model])
            # )
        )

    # def for_customer(self, entity_slug, user_model, customer):
    #     qs = self.get_queryset().filter(
    #         Q(entity__slug__exact=entity_slug) &
    #         # Q(entity__admin=user_model) |
    #         Q(entity__managers__in=[user_model])
    #     )
    #     qs = qs.filter(customer=customer)
    #     return qs

class CustomerLocationModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=True,
                               on_delete=models.CASCADE,
                               verbose_name=_('Customer Location Entity'))
    customer = models.ForeignKey('aix.CustomerModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('Customer'))

    objects = CustomerLocationModelManager()

    class Meta:
        verbose_name = _('Customer Location')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['name']),
        ]
        unique_together = [
            ('entity', 'name', 'customer')
        ]

    def __str__(self):
        return f'{self.code} - {self.name}'

    def get_form(self, form=None):
        return form

    def configure(self, entity_slug: str or EntityModel, user_model,):
        self.code = generate_code()
        return self