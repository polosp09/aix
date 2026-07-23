from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import BenefitModel

class BenefitForm(ModelForm):
    class Meta:
        model = BenefitModel
        fields= ['start_date', 'end_date', 'value', 'description', 'benefit_type', 'salary', 'is_active',]

        widgets = {
            'start_date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('Start Date (YYYY-MM-DD)...')
            }),
            'end_date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('End Date (YYYY-MM-DD)...')
            }),
            'value': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            }),
            'benefit_type': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'salary': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(BenefitForm,self).__init__(*args,**kwargs)