"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from aix.models.mixins import ContactInfoMixIn, CreateUpdateMixIn

UserModel = get_user_model()

class JobApplicantModelManager(models.Manager):

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


class JobApplicantModel(ContactInfoMixIn, CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=False)

    entity = models.ForeignKey('aix.EntityModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('JobApplicant Entity'),
                               related_name='Job_Applicant_Entity')
    job = models.ForeignKey('aix.JobModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('Job'),
                               related_name='applied_job')
    applicant = models.ForeignKey(UserModel,
                              on_delete=models.CASCADE,
                              related_name='applicant_of',
                              verbose_name=_('Applicant'))

    objects = JobApplicantModelManager()

    class Meta:
        verbose_name = _('Job Applicant')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['is_active']),
        ]
        unique_together = [
            ('entity', 'date', 'job', 'applicant', 'is_active')
        ]

    def __str__(self):
        return f'Equip.Join: {self.date}-{self.eq_primary.reg_no}-{self.eq_secondary.reg_no}'
