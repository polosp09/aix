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


class EmployeeModelManager(models.Manager):

    def for_entity(self, entity_slug: str, user_model):
        qs = self.get_queryset()
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            # Q(active=True) &
            (
                    Q(entity__admin=user_model) |
                    Q(entity__managers__in=[user_model])
            )
        )

    def for_user(self, user_model):
        qs = self.get_queryset()
        return qs.filter(
            #Q(entity__admin=user_model) |
            Q(entity__managers__in=[user_model])
        )


class EmployeeModel(CreateUpdateMixIn):
    OPTIONS_SALUTATIONS = [
        ('Mr', _('MR')),
        ('Mrs', _('MRS')),
        ('Miss', _('MISS')),
        ('Sir', _('SIR')),
        ('Madam', _('MADAM')),
    ]
    OPTIONS_GENDER = (('Male', 'Male'), ('Female', 'Female'),) #('Male', 'Female')

    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)    
    idnumber = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(blank=False, null=False, max_length=255)
    designation = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True,choices=OPTIONS_GENDER)
    dateofbirth = models.DateField(blank=True, null=True)
    contactnumber = models.CharField(max_length=255, blank=True, null=True)
    emergencycontact = models.CharField(max_length=255, blank=True, null=True)
    contractstartdate = models.DateField(blank=True, null=True)
    locationsite = models.CharField(max_length=255, blank=True, null=True)
    passportidno = models.CharField(max_length=255, blank=True, null=True)
    permitissuedate = models.DateField(blank=True, null=True)
    permitexpirydate = models.DateField(blank=True, null=True)
    medicalstartdate = models.DateField(blank=True, null=True)
    medicalexpirydate = models.DateField(blank=True, null=True)
    operatorstartdate = models.DateField(blank=True, null=True)
    operatorexpirydate = models.DateField(blank=True, null=True)
    defensivestartdate = models.DateField(blank=True, null=True)
    defensiveexpirydate = models.DateField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    wostatus = models.CharField(db_column='woStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=255, blank=True, null=True)
    imageurl = models.TextField(db_column='imageUrl', blank=True, null=True)  # Field name made lowercase.
    
    entity = models.ForeignKey('aix.EntityModel',
                               editable=False,
                               on_delete=models.CASCADE,
                               verbose_name=_('Employee Entity'))
    department = models.ForeignKey('aix.DepartmentModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Department'))
    username = models.ForeignKey(UserModel,
                              on_delete=models.CASCADE,
                              related_name='user_of',
                              verbose_name=_('Username'), 
                              blank=True, 
                              null=True)

    objects = EmployeeModelManager()

    class Meta:
        verbose_name = _('Employee')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['idnumber']),
            models.Index(fields=['name']),
        ]
        unique_together = [
            ('entity', 'idnumber', 'username')
        ]

    def __str__(self):
        return f'{self.idnumber} - {self.name}'
