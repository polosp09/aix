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


class InsuranceDetailModelManager(models.Manager):

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


class InsuranceDetailModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    policy_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    pin_number = models.CharField(max_length=255, blank=True, null=True)
    certificate_number = models.CharField(max_length=255)
    premium = models.IntegerField(default=0)
    address = models.CharField(max_length=255)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=0)
    comment = models.TextField(blank=True, null=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('InsuranceDetail Entity'))
    employee = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Employee'))
    currency = models.ForeignKey('aix.CurrencyModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Currency'))

    objects = InsuranceDetailModelManager()

    class Meta:
        verbose_name = _('InsuranceDetail')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['policy_name']),
            models.Index(fields=['company_name']),
        ]
        unique_together = [
            ('entity', 'policy_name')
        ]

    def __str__(self):
        return f'InsuranceDetail: {self.policy_name}'
