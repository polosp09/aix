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


class EmployeePayrollBenefitModelManager(models.Manager):

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


class EmployeePayrollBenefitModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    polarity = models.IntegerField(default=0, blank=True, null=True)
    is_taxed = models.IntegerField(default=0)
    amount = models.TextField()
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('EmployeePayrollBenefit Entity'))
    employee_payroll = models.ForeignKey('aix.EmployeePayrollModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('EmployeePayroll'))
    benefit_type = models.ForeignKey('aix.BenefitTypeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('BenefitType'))

    objects = EmployeePayrollBenefitModelManager()

    class Meta:
        verbose_name = _('EmployeePayrollBenefit')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
        ]
        unique_together = [
            ('entity', 'polarity')
        ]

    def __str__(self):
        return f'EmployeePayrollBenefit: {self.polarity}'
