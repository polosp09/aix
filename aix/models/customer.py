"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from uuid import uuid4

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from aix.models.mixins import ContactInfoMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class CustomerModelManager(models.Manager):

    def for_entity(self, entity_slug: str, user_model):
        qs = self.get_queryset()
        # print(entity_slug, 'else')
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            Q(entity__managers__in=[user_model]) &
            Q(active=True) #&
            # (
            #         Q(entity__admin=user_model) |
            #         Q(entity__managers__in=[user_model])
            # )
        )


class CustomerModel(ContactInfoMixIn, CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    customer_name = models.CharField(max_length=100)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('Customer Entity'))
    business_industry = models.ForeignKey('aix.BusinessIndustryModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('BusinessIndustry'))
    nation = models.ForeignKey('aix.NationModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Country'))
    user = models.OneToOneField(User, unique=False, 
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('User'))
    description = models.TextField()
    active = models.BooleanField(default=True)
    hidden = models.BooleanField(default=False)

    additional_info = models.JSONField(null=True, blank=True)


    objects = CustomerModelManager()

    class Meta:
        verbose_name = _('Customer')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['active']),
            models.Index(fields=['hidden']),
        ]
        unique_together = [
            ('entity', 'customer_name')
        ]

    def __str__(self):
        return f'{self.customer_name}'
