from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import VisaModel

class VisaForm(ModelForm):
    class Meta:
        model = VisaModel
        fields= ['visa_number', 'issue_date', 'expiry_date', 'immigration_detail',]

        widgets = {
            'visa_number': TextInput(attrs={
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
            'immigration_detail': Textarea(attrs={
                'class': 'textarea'
            })
        }

    def __init__(self,*args,**kwargs):
        super(VisaForm,self).__init__(*args,**kwargs)