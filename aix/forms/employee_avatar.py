from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import EmployeeAvatarModel

class EmployeeAvatarForm(ModelForm):
    class Meta:
        model = EmployeeAvatarModel
        fields= ['name', 'extension', 'mime_type', 'size', 'description', 'employee',]

        widgets = {
            'name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'extension': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'mime_type': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'size': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(EmployeeAvatarForm,self).__init__(*args,**kwargs)