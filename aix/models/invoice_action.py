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


class InvoiceActionModelManager(models.Manager):

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


class InvoiceActionModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    comment = models.TextField(blank=True, null=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('InvoiceAction Entity'))
    employee = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Employee'))
    invoice_status = models.ForeignKey('aix.InvoiceStatusModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('InvoiceStatus'))
    invoice = models.ForeignKey('aix.InvoiceModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Invoice'))

    objects = InvoiceActionModelManager()

    class Meta:
        verbose_name = _('InvoiceAction')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['comment']),
        ]
        unique_together = [
            ('entity', 'comment')
        ]

    def __str__(self):
        return f'InvoiceAction: {self.comment}'
