
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import EquipmentTypeModel

class EquipmentTypeForm(ModelForm):
    class Meta:
        model = EquipmentTypeModel
        fields= ['name', 'description',]

        widgets = {
            'code': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            })
        }

    def __init__(self,*args,**kwargs):
        super(EquipmentTypeForm,self).__init__(*args,**kwargs)