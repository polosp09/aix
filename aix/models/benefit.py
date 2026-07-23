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


class BenefitModelManager(models.Manager):

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


class BenefitModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    value = models.CharField(max_length=100)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('Benefit Entity'),
                               related_name='benefits')
    benefit_type = models.ForeignKey('aix.BenefitTypeModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('BenefitType Entity'))
    salary = models.ForeignKey('aix.SalaryModel',
                               on_delete=models.RESTRICT,
                               verbose_name=_('Salary Entity'))
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    hidden = models.BooleanField(default=False)

    additional_info = models.JSONField(null=True, blank=True)

    objects = BenefitModelManager()

    class Meta:
        verbose_name = _('Benefit')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['start_date']),
            models.Index(fields=['end_date']),
        ]
        unique_together = [
            ('entity', 'value')
        ]

    def __str__(self):
        return f'Benefit: {self.value}'
