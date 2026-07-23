
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import EquipmentModel, AssetModel, WorkOrderTaskAssetModel

class EquipmentForm(ModelForm):

    def __init__(self, *args, entity_slug, user_model, **kwargs):
        super().__init__(*args, **kwargs)
        self.ENTITY_SLUG = entity_slug
        self.USER_MODEL = user_model
    
        work_order_pk = kwargs.pop('work_order_pk', None)
        assigned_asset_qs = WorkOrderTaskAssetModel.objects.filter(task__work_order_id=work_order_pk)
        asset_qs = AssetModel.objects.filter(pk__in=assigned_asset_qs.values_list("asset_id", flat=True))
        self.fields['asset'].queryset = asset_qs

    class Meta:
        model = EquipmentModel
        fields= ['reg_no', 'serial', 'yom', 'model','details','eq_manufacturer', 'eq_type', 'asset', 'active',]

        widgets = {
            'reg_no': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'serial': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'yom': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'model': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'details': Textarea(attrs={
                'class': 'textarea'
            }),
            'eq_manufacturer': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'eq_type': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(EquipmentForm,self).__init__(*args,**kwargs)