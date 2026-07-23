
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import EquipmentAssignmentModel

class EquipmentAssignmentForm(ModelForm):
    class Meta:
        model = EquipmentAssignmentModel
        fields= ['code', 'date', 'equipment', 'operator', 'is_supervisor', 'is_assistant', 'is_active',]

        widgets = {
            'code': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'date': TextInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'equipment': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'operator': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_supervisor': CheckboxInput(attrs={'type': 'checkbox'}),
            'is_assistant': CheckboxInput(attrs={'type': 'checkbox'}),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(EquipmentAssignmentForm,self).__init__(*args,**kwargs)