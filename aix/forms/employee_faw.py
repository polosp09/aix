"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""
from django import forms
from django.forms import (ModelForm, DateInput, TextInput, Select, BaseModelFormSet,
                          modelformset_factory, formset_factory, Textarea, BooleanField, ValidationError)
from django.utils.translation import gettext_lazy as _

from aix.models import (ItemFawModel, EmployeeFawModel, ItemFawThroughModel, EntityUnitModel, EmployeeModel, WorkOrderPersonnelModel)
from aix.settings import MANDO_FORM_INPUT_CLASSES

class EmployeeFawModelCreateForm(ModelForm):
    def __init__(self, *args, entity_slug, user_model, **kwargs):
        super().__init__(*args, **kwargs)
        self.ENTITY_SLUG = entity_slug
        self.USER_MODEL = user_model

    class Meta:
        model = EmployeeFawModel
        fields = [
            'faw_date',
            'location',
            # 'faw_status',
        ]
        widgets = {
            'faw_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'location': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large',
                'placeholder': 'Employee'}),
            'faw_status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large',
                'placeholder': 'Status'})
        }


class BaseEmployeeFawModelUpdateForm(ModelForm):

    def __init__(self, *args, entity_slug, user_model, **kwargs):
        super().__init__(*args, **kwargs)
        self.ENTITY_SLUG = entity_slug
        self.USER_MODEL = user_model
        self.FAW_MODEL: EmployeeFawModel = self.instance

    class Meta:
        model = EmployeeFawModel
        fields = [
            'faw_date',
            'location',
            'faw_status',
        ]
        widgets = {
            'faw_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'location': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large',
                'placeholder': 'Employee'}),
            'faw_status': Select(attrs={'class': MANDO_FORM_INPUT_CLASSES})
        }
        labels = {
            'faw_date': _('Date'),
            'location': _('Location'),
            # 'faw_status': _('Status')
        }


class DraftEmployeeFawModelUpdateForm(BaseEmployeeFawModelUpdateForm):
    class Meta(BaseEmployeeFawModelUpdateForm.Meta):
        fields = [
            'faw_date',
            'location',
            # 'faw_status',
        ]


class ReviewEmployeeFawModelUpdateForm(BaseEmployeeFawModelUpdateForm):
    class Meta(BaseEmployeeFawModelUpdateForm.Meta):
        fields = [
            'location',
            # 'faw_status',
        ]


class ApprovedEmployeeFawModelUpdateForm(BaseEmployeeFawModelUpdateForm):
    class Meta(BaseEmployeeFawModelUpdateForm.Meta):
        fields = [
            'faw_status',
        ]


class EmployeeFawItemForm(ModelForm):
    create_invoice = BooleanField(required=False)
    # employee_model = forms.ModelChoiceField(queryset=EmployeeModel.objects.all(), 
    #                     widget=forms.Select(attrs={'class': MANDO_FORM_INPUT_CLASSES + ' is-small'}),
    #                     empty_label="Select a category",
    #                     # initial=EmployeeModel.objects.get()
    #                     )
    # employee_qs = EmployeeModel.objects.all()
    # initial_data = [{'employee_model': emp.uuid} for emp in employee_qs]


    class Meta:
        model = ItemFawThroughModel
        fields = [
            'employee_model',
            'attendance_code',
            # 'attendance_date',
            'faw_item_status',
        ]
        widgets = {
            # 'employee_model': Select(attrs={
            #     'class': MANDO_FORM_INPUT_CLASSES + ' is-small',
            # }),
            'attendance_code': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-small',
            }),
            'attendance_date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('D.O.B (YYYY-MM-DD)...')
            }),
            'faw_item_status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-small',
            }),
        }

    def clean(self):
        cleaned_data = super(EmployeeFawItemForm, self).clean()
        faw_item_status = cleaned_data['faw_item_status']
        employee_model: ItemFawThroughModel = self.instance
        if 'faw_item_status' in self.changed_data:
            faw_model: EmployeeFawModel = getattr(self, 'FAW_MODEL')
            if faw_model.faw_status == faw_model.FAW_STATUS_APPROVED:
                if not faw_item_status:
                    raise ValidationError('Cannot assign null status to approved PO.')
            
            if all([
                faw_item_status in [ItemFawThroughModel.STATUS_CANCELED, ItemFawThroughModel.STATUS_COMPLETED]
            ]):
                raise ValidationError(f'Cannot mark as {faw_item_status.upper()}. '
                                      'Item must be invoiced first.')
        return cleaned_data


class BaseEmployeeFawItemFormset(BaseModelFormSet):

    def __init__(self, *args, entity_slug, user_model, faw_model: EmployeeFawModel, **kwargs):
        super().__init__(*args, **kwargs)
        self.USER_MODEL = user_model
        self.ENTITY_SLUG = entity_slug
        self.FAW_MODEL = faw_model
        self.queryset = ItemFawThroughModel.objects.filter(faw_model=faw_model)
        # items_qs = ItemFawModel.objects.for_faw(
        #     entity_slug=self.ENTITY_SLUG,
        #     user_model=self.USER_MODEL
        # )
        employee_qs = WorkOrderPersonnelModel.objects.filter(work_order_id=faw_model.work_order.uuid)  
        initial_data = [{'attendance_code': 'A',
                        'employee_model': emp} for emp in EmployeeModel.objects.filter(pk__in=employee_qs.values_list('employee_id', flat=True))]
        employee_qs = []
        for emp in initial_data:
            employee_qs.append(emp['employee_model'].uuid)
        eqs = EmployeeModel.objects.filter(pk__in=employee_qs)

        for form in self.forms:
            form.FAW_MODEL = self.FAW_MODEL
            form.fields['employee_model'].queryset = eqs
            if not self.FAW_MODEL.can_edit_items():
                form.fields['faw_date'].disabled = True
                form.fields['employee_model'].disabled = True
                form.fields['faw_item_status'].disabled = True
                if not self.FAW_MODEL.is_approved() or self.JCD_MODEL.is_fulfilled():
                    form.fields['faw_item_status'].disabled = False
                    # form.fields['faw_item_status'].widget.attrs['class'] += form.instance.get_faw_status_css_class()
            # FAW is Draft
            else:
                form.fields['faw_item_status'].disabled = True

def get_extra_form_count():
    employee_list = EmployeeModel.objects.all()
    if employee_list.exists():
        print(len(employee_list))
    else:
        print("QuerySet is empty.")
    return len(employee_list)

CanDeleteEmployeeFawItemFormset = modelformset_factory(
    model=ItemFawThroughModel,
    form=EmployeeFawItemForm,
    formset=BaseEmployeeFawItemFormset,
    can_delete=True,
    extra=5
)

CanEditEmployeeFawItemFormset = modelformset_factory(
    model=ItemFawThroughModel,
    form=EmployeeFawItemForm,
    formset=BaseEmployeeFawItemFormset,
    can_delete=True,
    extra=0
    # extra=get_extra_form_count()
)

ReadOnlyEmployeeFawItemFormset = modelformset_factory(
    model=ItemFawThroughModel,
    form=EmployeeFawItemForm,
    formset=BaseEmployeeFawItemFormset,
    can_delete=False,
    extra=0
)


def get_faw_item_formset(faw_model: EmployeeFawModel):
    # if faw_model.is_draft():
    #     return CanEditEmployeeFawItemFormset
    # return ReadOnlyEmployeeFawItemFormset
    return CanEditEmployeeFawItemFormset

def get_faw_item_formset2(faw_model: EmployeeFawModel):
    faw_formset = modelformset_factory(
    model=ItemFawThroughModel,
    form=EmployeeFawItemForm,
    formset=BaseEmployeeFawItemFormset,
    extra=0)
    return faw_formset