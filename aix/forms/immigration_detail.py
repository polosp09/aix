
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import ImmigrationDetailModel

class ImmigrationDetailForm(ModelForm):
    class Meta:
        model = ImmigrationDetailModel
        fields= ['passport_number', 'issue_date', 'expiry_date', 'citizenship', 'employee',]

        widgets = {
            'passport_number': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'issue_date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('Issue Date (YYYY-MM-DD)...')
            }),
            'expiry_date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('Expiry Date (YYYY-MM-DD)...')
            }),
            'citizenship': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(ImmigrationDetailForm,self).__init__(*args,**kwargs)