"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""
from random import choices
from string import ascii_uppercase, digits
from uuid import uuid4

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from aix.models.mixins import SlugNameMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q


PAR_CHARS = ascii_uppercase + digits

def generate_par_number(length: int = 10, prefix: bool = True) -> str:
    par_number = ''.join(choices(PAR_CHARS, k=length))
    if prefix:
        par_number = 'PAR-' + par_number
    return par_number

class PayrollAdvanceRequestModelManager(models.Manager):

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


class PayrollAdvanceRequestModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    number = models.CharField(max_length=255)
    date = models.DateField()
    remarks = models.CharField(max_length=255, blank=True, null=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('Payroll Advance Request Entity'))
    par_status = models.ForeignKey('aix.PayrollAdvanceRequestStatusModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Payroll Advance Request Status'))
    employee = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Payroll - Employee'),
                                 related_name=_('payroll_request_employee'))
    supervisor = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Payroll - Supervisor'),
                                 related_name=_('payroll_supervisor'))

    objects = PayrollAdvanceRequestModelManager()

    class Meta:
        verbose_name = _('Payroll Advance Request')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['number']),
            models.Index(fields=['date']),
        ]
        unique_together = [
            ('entity', 'number')
        ]

    def __str__(self):
        return f'PAR: {self.number}'

    def clean(self):
        if not self.number:
            self.number = generate_par_number()
        super().clean()