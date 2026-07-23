
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import EquipmentHandoverModel

class EquipmentHandoverForm(ModelForm):
    class Meta:
        model = EquipmentHandoverModel
        fields= ['ho_date', 'ho_time', 'project', 'location','dho','condition','purpose', 'equipment', 'return_date', 'handover_by', 'received_by', 'is_active']

        widgets = {
            'ho_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'ho_time': DateInput(attrs={
                'type': 'time',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'project': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'location': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'dho': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'condition': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'purpose': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'return_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'handover_by': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'received_by': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'location': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(EquipmentHandoverForm,self).__init__(*args,**kwargs)