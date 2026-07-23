"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""
from random import choices
from string import ascii_uppercase, digits
from typing import Tuple
from uuid import uuid4

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from aix.models.entity import EntityModel
from aix.models.mixins import SlugNameMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q, QuerySet

LEAVE_REQUEST_CHARS = ascii_uppercase + digits

def generate_leave_request_number(length: int = 10, prefix: bool = True) -> str:
    leave_request_number = ''.join(choices(LEAVE_REQUEST_CHARS, k=length))
    if prefix:
        leave_request_number = 'LR-' + leave_request_number
    return leave_request_number

class LeaveRequestModelManager(models.Manager):

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


class LeaveRequestModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    number = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=255, blank=True, null=True)
    contact_email = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('Leave Request Entity'))
    leave_request_status = models.ForeignKey('aix.LeaveRequestStatusModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Leave Request Status'))
    employee = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Leave - Employee'),
                                 related_name=_('leave_request_employee'))
    supervisor = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Leave - Supervisor'),
                                 related_name=_('leave_request_supervisor'))

    objects = LeaveRequestModelManager()

    class Meta:
        verbose_name = _('LeaveRequest')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['number']),
        ]
        unique_together = [
            ('entity', 'number')
        ]

    def __str__(self):
        return f'Leave Request: {self.number}'

    def clean(self):
        if not self.number:
            self.number = generate_leave_request_number()
        super().clean()