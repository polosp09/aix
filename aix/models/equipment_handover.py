"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""
from random import choices
from string import ascii_uppercase, digits
from uuid import uuid4

from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q
from aix.models.entity import EntityModel
from aix.models.employee import EmployeeModel
from django.utils.timezone import localdate
from django.utils.translation import gettext_lazy as _

from aix.models.mixins import ContactInfoMixIn, CreateUpdateMixIn

UserModel = get_user_model()
CODE_NUMBER_CHARS = ascii_uppercase + digits

def generate_code_number(length: int = 10, prefix: bool = True) -> str:
    jobcard_number = ''.join(choices(CODE_NUMBER_CHARS, k=length))
    if prefix:
        jobcard_number = 'EHO' + jobcard_number
    return jobcard_number


PROJECTS = (("RG1501", "Rig Move 1501"), ("RG1502", "Rig Move 1502"), ("RG1503", "Rig Move 1503"), ("KFDA", "King Fisher Oil Field"), ("CPP", "CPP"),)
CONDITIONS = (("GOOD", "GOOD"), ("FAULTY", "FAULTY"), ("DAMAGED", "DAMAGED"), ("FOR REPAIR", "FOR REPAIR"), ("FOR REPLACEPMENT", "FOR REPLACEPMENT"),)
PURPOSES = (("OFF", "OFFICIAL"), ("UNOFF", "UN-OFFICIAL"), ("FOH", "FOR HIRE"), ("EXT", "EXTERNAL"),)

class EquipmentHandoverModelManager(models.Manager):

    def for_entity(self, entity_slug: str, user_model):
        qs = self.get_queryset()
        return qs.filter(
            Q(entity__slug__exact=entity_slug) &
            Q(is_active=True) &
            (
                    #Q(entity__admin=user_model) |
                    Q(entity__managers__in=[user_model])
            )
        )


class EquipmentHandoverModel(ContactInfoMixIn, CreateUpdateMixIn):
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    code = models.CharField(max_length=100)
    ho_date = models.DateField(blank=True, null=True)
    ho_time = models.TimeField(auto_now=False, auto_now_add=False)
    project = models.CharField(max_length=100, choices=PROJECTS)
    dho = models.TextField(blank=True, null=True)
    condition = models.CharField(max_length=100, choices=CONDITIONS)
    purpose = models.CharField(max_length=100, choices=PURPOSES)
    is_active = models.BooleanField(default=False)
    return_date = models.DateField(blank=True, null=True)
    approved_date_hr = models.DateField(blank=True, null=True)
    approved_date_ict = models.DateField(blank=True, null=True)

    entity = models.ForeignKey('aix.EntityModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('EquipmentHandover Entity'),
                               related_name='equipment_handover_entity')
    equipment = models.ForeignKey('aix.EquipmentModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('Items Handed Over'))
    handover_by = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Handover By'),
                                 related_name='equipment_handover_by')
    received_by = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 verbose_name=_('Received By'),
                                 related_name='equipment_received_by')
    location = models.ForeignKey('aix.CustomerLocationModel',
                               on_delete=models.CASCADE,
                               verbose_name=_('Customer Location'))
    approved_by_hr = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 blank=True, 
                                 null=True,
                                 verbose_name=_('Approved By HR'),
                                 related_name='approved_by_hr')
    approved_by_ict = models.ForeignKey('aix.EmployeeModel',
                                 on_delete=models.RESTRICT,
                                 blank=True, 
                                 null=True,
                                 verbose_name=_('Approved By ICT'),
                                 related_name='approved_by_ict')

    objects = EquipmentHandoverModelManager()

    class Meta:
        verbose_name = _('Equipment Handover')
        indexes = [
            models.Index(fields=['created']),
            models.Index(fields=['updated']),
            models.Index(fields=['is_active']),
        ]
        unique_together = [
            ('entity', 'ho_date', 'equipment', 'handover_by', 'received_by')
        ]

    def __str__(self):
        return f'EHO: {self.ho_date}-{self.equipment}-{self.handover_by}-{self.received_by}'

    def configure(self,
                  entity_slug: str or EntityModel,
                  user_model: UserModel):

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

    
    def mark_as_approved_by_hr(self, commit: bool = False, **kwargs):
        # employee_model = kwargs['employee_model']
        user_id = kwargs['user_id']
        employee_qs = EmployeeModel.objects.for_entity(
            entity_slug=kwargs['entity_slug'],
            user_model=user_id
        )
        print(user_id, employee_qs.count(), kwargs['entity_slug'])
        # kwargs['employee_model'] = None
        if employee_qs:
            employee_model: EmployeeModel = get_object_or_404(employee_qs, username__exact=user_id)
            # kwargs['employee_model'] = employee_model.uuid
            self.approved_by_hr = employee_model
            self.approved_date_hr = localdate()
            self.clean()
            if commit:
                self.save()
                # print(employee_model, commit)

    def mark_as_approved_by_ict(self, commit: bool = False, **kwargs):
        user_id = kwargs['user_id']
        employee_qs = EmployeeModel.objects.for_entity(
            entity_slug=kwargs['entity_slug'],
            user_model=user_id
        )
        if employee_qs:
            employee_model: EmployeeModel = get_object_or_404(employee_qs, username__exact=user_id)
            self.approved_by_ict = employee_model
            self.approved_date_ict = localdate()
            self.clean()
            if commit:
                self.save()

    def get_mark_as_approved_hr_html_id(self):
        return f'djl-{self.uuid}-mark-as-approved-hr'

    def get_mark_as_approved_hr_url(self):
        return reverse('aix:equipment-handover-action-mark-as-approved-by-hr',
                       kwargs={
                           'entity_slug': self.entity.slug,
                           'equipment_handover_pk': self.uuid
                       })
                       
    def get_mark_as_approved_ict_html_id(self):
        return f'djl-{self.uuid}-mark-as-approved-ict'

    def get_mark_as_approved_ict_url(self):
        return reverse('aix:equipment-handover-action-mark-as-approved-by-ict',
                       kwargs={
                           'entity_slug': self.entity.slug,
                           'equipment_handover_pk': self.uuid
                       })
                       
    def get_mark_as_approved_hr_message(self):
        return _('Dear HR, Do you want to mark Equipment Handover %s as Approved?') % self.equipment.serial

    def get_mark_as_approved_ict_message(self):
        return _('Dear ICT, Do you want to mark Equipment Handover %s as Approved?') % self.equipment.serial