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


class PayrollAdvanceRequestActionModelManager(models.Manager):

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


class PayrollAdvanceRequestActionModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    comment = models.CharField(max_length=100)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('PayrollAdvanceRequestAction Entity'))
    par_status = models.ForeignKey('aix.PayrollAdvanceRequestStatusModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('PayrollAdvanceRequestStatus'))
    pa_request = models.ForeignKey('aix.PayrollAdvanceRequestModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('PayrollAdvanceRequest'))
    employee = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Employee'))

    objects = PayrollAdvanceRequestActionModelManager()

    class Meta:
        verbose_name = _('PayrollAdvanceRequestAction')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['comment']),
        ]
        unique_together = [
            ('entity', 'comment')
        ]

    def __str__(self):
        return f'PayrollAdvanceRequestAction: {self.comment}'
