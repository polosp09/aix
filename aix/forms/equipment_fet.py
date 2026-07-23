"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""
from django import forms
from django.forms import (ModelForm, DateInput, TextInput, Select, BaseModelFormSet,
                          modelformset_factory, formset_factory, Textarea, BooleanField, ValidationError)
from django.utils.translation import gettext_lazy as _

from aix.models import (ItemFetModel, EquipmentFetModel, ItemFetThroughModel, 
                          EntityUnitModel, EquipmentModel, WorkOrderAssetModel)
from aix.settings import MANDO_FORM_INPUT_CLASSES

class EquipmentFetModelCreateForm(ModelForm):
    def __init__(self, *args, entity_slug, user_model, **kwargs):
        super().__init__(*args, **kwargs)
        self.ENTITY_SLUG = entity_slug
        self.USER_MODEL = user_model

    class Meta:
        model = EquipmentFetModel
        fields = [
            'fet_date',
            'location',
            # 'fet_status',
        ]
        widgets = {
            'fet_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'location': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large',
                'placeholder': 'Location'}),
            'fet_status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large',
                'placeholder': 'Status'})
        }


class BaseEquipmentFetModelUpdateForm(ModelForm):

    def __init__(self, *args, entity_slug, user_model, **kwargs):
        super().__init__(*args, **kwargs)
        self.ENTITY_SLUG = entity_slug
        self.USER_MODEL = user_model
        self.FET_MODEL: EquipmentFetModel = self.instance

    class Meta:
        model = EquipmentFetModel
        fields = [
            'fet_date',
            'location',
            'fet_status',
        ]
        widgets = {
            'fet_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'location': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large',
                'placeholder': 'Equipment'}),
            'fet_status': Select(attrs={'class': MANDO_FORM_INPUT_CLASSES})
        }
        labels = {
            'fet_date': _('Date'),
            'location': _('Location'),
            # 'fet_status': _('Status')
        }


class DraftEquipmentFetModelUpdateForm(BaseEquipmentFetModelUpdateForm):
    class Meta(BaseEquipmentFetModelUpdateForm.Meta):
        fields = [
            'fet_date',
            'location',
            # 'fet_status',
        ]


class ReviewEquipmentFetModelUpdateForm(BaseEquipmentFetModelUpdateForm):
    class Meta(BaseEquipmentFetModelUpdateForm.Meta):
        fields = [
            'location',
            # 'fet_status',
        ]


class ApprovedEquipmentFetModelUpdateForm(BaseEquipmentFetModelUpdateForm):
    class Meta(BaseEquipmentFetModelUpdateForm.Meta):
        fields = [
            'fet_status',
        ]


class EquipmentFetItemForm(ModelForm):
    create_invoice = BooleanField(required=False)
    # equipment_model = forms.ModelChoiceField(queryset=EquipmentModel.objects.all(), 
    #                     widget=forms.Select(attrs={'class': MANDO_FORM_INPUT_CLASSES + ' is-small'}),
    #                     empty_label="Select a category",
    #                     # initial=EquipmentModel.objects.get()
    #                     )
    # equipment_qs = EquipmentModel.objects.all()
    # initial_data = [{'equipment_model': emp.uuid} for emp in equipment_qs]


    class Meta:
        model = ItemFetThroughModel
        fields = [
            'equipment_model',
            'attendance_code',
            # 'attendance_date',
            'fet_item_status',
        ]
        widgets = {
            # 'equipment_model': Select(attrs={
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
            'fet_item_status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-small',
            }),
        }

    def clean(self):
        cleaned_data = super(EquipmentFetItemForm, self).clean()
        fet_item_status = cleaned_data['fet_item_status']
        equipment_model: ItemFetThroughModel = self.instance
        if 'fet_item_status' in self.changed_data:
            fet_model: EquipmentFetModel = getattr(self, 'FET_MODEL')
            if fet_model.fet_status == fet_model.FET_STATUS_APPROVED:
                if not fet_item_status:
                    raise ValidationError('Cannot assign null status to approved PO.')
            
            if all([
                fet_item_status in [ItemFetThroughModel.STATUS_CANCELED, ItemFetThroughModel.STATUS_COMPLETED]
            ]):
                raise ValidationError(f'Cannot mark as {fet_item_status.upper()}. '
                                      'Item must be invoiced first.')
        return cleaned_data

class BaseEquipmentFetItemFormset(BaseModelFormSet):

    def __init__(self, *args, entity_slug, user_model, fet_model: EquipmentFetModel, **kwargs):
        super().__init__(*args, **kwargs)
        self.USER_MODEL = user_model
        self.ENTITY_SLUG = entity_slug
        self.FET_MODEL = fet_model
        # print(fet_model.uuid)
        self.queryset = ItemFetThroughModel.objects.filter(fet_model=fet_model)

        # items_qs = ItemFetModel.objects.for_fet(
        #     entity_slug=self.ENTITY_SLUG,
        #     user_model=self.USER_MODEL
        # )
        asset_qs = WorkOrderAssetModel.objects.filter(work_order_id=fet_model.work_order.uuid)  
        initial_data = [{'attendance_code': 'OH',
                        'equipment_model': emp} for emp in EquipmentModel.objects.filter(asset__in=asset_qs.values_list('asset_id', flat=True))]
        equipment_qs = []
        for emp in initial_data:
            equipment_qs.append(emp['equipment_model'].uuid)
            print(emp['equipment_model'].uuid)
            # equipment_qs.union(emp)
        eqs = EquipmentModel.objects.filter(pk__in=equipment_qs)

        for form in self.forms:
            form.FET_MODEL = self.FET_MODEL
            form.fields['equipment_model'].queryset = eqs
            # form.initial['attendance_date'] = fet_model.fet_date
            # form.fields['attendance_date'].disabled = True
            if not self.FET_MODEL.can_edit_items():
                form.fields['fet_date'].disabled = True
                form.fields['equipment_model'].disabled = True
                form.fields['fet_item_status'].disabled = True
                if not self.FET_MODEL.is_approved() or self.JCD_MODEL.is_fulfilled():
                    form.fields['fet_item_status'].disabled = False
                    # form.fields['fet_item_status'].widget.attrs['class'] += form.instance.get_fet_status_css_class()
            # FET is Draft
            else:
                form.fields['fet_item_status'].disabled = True

def get_extra_form_count():
    equipment_list = EquipmentModel.objects.all()
    if equipment_list.exists():
        print(len(equipment_list))
    else:
        print("QuerySet is empty.")
    return len(equipment_list)

CanDeleteEquipmentFetItemFormset = modelformset_factory(
    model=ItemFetThroughModel,
    form=EquipmentFetItemForm,
    formset=BaseEquipmentFetItemFormset,
    can_delete=True,
    extra=5
)

CanEditEquipmentFetItemFormset = modelformset_factory(
    model=ItemFetThroughModel,
    form=EquipmentFetItemForm,
    formset=BaseEquipmentFetItemFormset,
    can_delete=True,
    # extra=get_extra_form_count()
)

ReadOnlyEquipmentFetItemFormset = modelformset_factory(
    model=ItemFetThroughModel,
    form=EquipmentFetItemForm,
    formset=BaseEquipmentFetItemFormset,
    can_delete=False,
    extra=0
)


def get_fet_item_formset(fet_model: EquipmentFetModel):
    # if fet_model.is_draft():
    #     return CanEditEquipmentFetItemFormset
    # return ReadOnlyEquipmentFetItemFormset
    return CanEditEquipmentFetItemFormset

def get_fet_item_formset2(fet_model: EquipmentFetModel):
    fet_formset = modelformset_factory(
    model=ItemFetThroughModel,
    form=EquipmentFetItemForm,
    formset=BaseEquipmentFetItemFormset,
    extra=0)
    return fet_formset
