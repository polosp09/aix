"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from uuid import uuid4

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from aix.models.mixins import SlugNameMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q

UserModel = get_user_model()

class UserAllocationModelManager(models.Manager):

    def for_entity(self, entity_slug: str, user_model):
        qs = self.get_queryset()
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            Q(active=True) &
            (
                    #Q(entity__admin=user_model) |
                    Q(entity__managers__in=[user_model])
            )
        )


    def for_allocation(self, entity_slug: str, allocation):
        qs = self.get_queryset()
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            Q(allocation=allocation)
        )

class UserAllocationModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    active = models.BooleanField(default=True, verbose_name=_('Active'))

    entity = models.ForeignKey('aix.EntityModel',
                               editable=True,
                               on_delete=models.CASCADE,
                               verbose_name=_('UserAllocation Entity'),
                               related_name='user_allocation')
    allocation = models.ForeignKey(UserModel,
                              on_delete=models.CASCADE,
                              related_name='allocated_to',
                              verbose_name=_('Allocation'))
    work_order = models.ForeignKey('aix.WorkOrderModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Work Order'),
                                 blank=True,
                                 null=True)
    task = models.ForeignKey('aix.WorkOrderTaskModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Work Order Task'),
                                 blank=True,
                                 null=True)

    objects = UserAllocationModelManager()

    class Meta:
        verbose_name = _('UserAllocation')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
        ]
        unique_together = [
            ('entity', 'work_order', 'task')
        ]

    def __str__(self):
        return f'Allocation: {self.work_order} - {self.task} - {self.allocation}'
