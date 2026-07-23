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


class EmployeeTransactionModelManager(models.Manager):

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


class EmployeeTransactionModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    account_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255, blank=True, null=True)
    account_code = models.CharField(max_length=255, blank=True, null=True)
    branch = models.CharField(max_length=255, blank=True, null=True)
    entity = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    preferred = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('EmployeeTransaction Entity'))
    employee = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Employee'))
    payment_mode = models.ForeignKey('aix.PaymentModeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('PaymentMode'))

    objects = EmployeeTransactionModelManager()

    class Meta:
        verbose_name = _('EmployeeTransaction')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['account_name']),
        ]
        unique_together = [
            ('entity', 'account_name')
        ]

    def __str__(self):
        return f'EmployeeTransaction: {self.account_name}'
