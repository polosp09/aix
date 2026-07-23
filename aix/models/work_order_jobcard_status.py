"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""
from random import choices
from string import ascii_uppercase, digits
from uuid import uuid4

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from aix.models.mixins import SlugNameMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q

UserModel = get_user_model()
CODE_NUMBER_CHARS = ascii_uppercase + digits

def generate_code_number(length: int = 10, prefix: bool = True) -> str:
    code_number = ''.join(choices(CODE_NUMBER_CHARS, k=length))
    if prefix:
        code_number = 'JCDST' + code_number
    return code_number

class WorkOrderJobcardStatusModelManager(models.Manager):

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


class WorkOrderJobcardStatusModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=100, default='NA')
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('WO JobcardStatus Entity'))
    jobcard = models.ForeignKey('aix.WorkOrderJobcardModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('Jobcard'))
    status = models.ForeignKey('aix.WorkOrderStatusModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('WO Status'))

    objects = WorkOrderJobcardStatusModelManager()

    class Meta:
        verbose_name = _('Jobcard Status')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['code']),
        ]
        unique_together = [
            ('entity', 'code')
        ]

    def __str__(self):
        return f'Jobcard Status: {self.code}'

    def configure(self,
                  entity_slug: str or EntityModel,
                  user_model: UserModel,
                  post_ledger: bool = False):

        if isinstance(entity_slug, str):
            entity_qs = EntityModel.objects.for_user(
                user_model=user_model)
            entity_model: EntityModel = get_object_or_404(entity_qs, slug__exact=entity_slug)
        elif isinstance(entity_slug, EntityModel):
            entity_model = entity_slug
        else:
            raise ValidationError('entity_slug must be an instance of str or EntityModel')

        if not self.code:
            self.code = generate_code_number()
