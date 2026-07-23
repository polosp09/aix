from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import DependantModel

class DependantForm(ModelForm):
    class Meta:
        model = DependantModel
        fields= ['first_name', 'middle_name', 'last_name', 'date_of_birth', 'gender', 'address', 'relationship', 'employee',]

        widgets = {
            'first_name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'middle_name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'last_name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'gender': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'date_of_birth': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('D.O.B (YYYY-MM-DD)...')
            }),
            'relationship': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'address': Textarea(attrs={
                'class': 'textarea'
            })
        }

    def __init__(self,*args,**kwargs):
        super(DependantForm,self).__init__(*args,**kwargs)