
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import EquipmentJoinModel

class EquipmentJoinForm(ModelForm):
    class Meta:
        model = EquipmentJoinModel
        fields= ['code', 'date', 'eq_primary', 'eq_secondary', 'is_active',]

        widgets = {
            'code': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'eq_primary': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'eq_secondary': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(EquipmentJoinForm,self).__init__(*args,**kwargs)