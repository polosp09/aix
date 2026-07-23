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

# from django_ckeditor_5.fields import CKEditor5Field
# from ckeditor.fields import RichTextField
# from taggit.managers import TaggableManager


JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)

class JobModelManager(models.Manager):

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


class JobModel(CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=300)
    job_type = models.CharField(choices=JOB_TYPE, max_length=1)
    salary = models.CharField(max_length=30, blank=True)
    company_name = models.CharField(max_length=300)
    company_description = models.TextField(blank=True, null=True)
    # tags = TaggableManager()
    url = models.URLField(max_length=200)
    last_date = models.DateField()
    is_published = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('Job Entity'))
    category = models.ForeignKey('aix.JobCategoryModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('JobCategory'))

    objects = JobModelManager()

    class Meta:
        verbose_name = _('Job')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['title']),
        ]
        unique_together = [
            ('entity', 'title', 'category')
        ]

    def __str__(self):
        return f'Job: {self.title}'
