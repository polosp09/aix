"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from uuid import uuid4

from string import ascii_uppercase, digits
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from aix.models.mixins import SlugNameMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q

ORDERBYDIR = (("ASC", "ASC"), ("DESC", "DESC"))
CODE_NUMBER_CHARS = ascii_uppercase + digits

def generate_code(length: int = 10, prefix: bool = True) -> str:
    serial_code = ''.join(choices(CODE_NUMBER_CHARS, k=length))
    if prefix:
        serial_code = 'HSE' + serial_code
    return serial_code

class ReportModelManager(models.Manager):

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


class ReportModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=100, default='NA')
    rpt_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    sort_by = models.TextField(blank=True, null=True)
    order_by = models.TextField(blank=True, null=True)
    order_by_dir = models.TextField(default='ASC', choices=ORDERBYDIR, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('Report Entity'))

    objects = ReportModelManager()

    class Meta:
        verbose_name = _('Report')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
        ]
        unique_together = [
            ('entity', 'rpt_name')
        ]

    def __str__(self):
        return f'{self.code} {self.rpt_name}'

    def configure(self, entity_slug: str or EntityModel, user_model,):
        self.code = generate_code()
        return self