
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import SalaryModel

class SalaryForm(ModelForm):
    class Meta:
        model = SalaryModel
        fields= ['start_date', 'end_date', 'basic_pay', 'description', 'employee', 'currency', 'is_active', ]

        widgets = {
            'basic_pay': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'currency': Select(attrs={'class': MANDO_FORM_INPUT_CLASSES}),
            'employee': Select(attrs={'class': MANDO_FORM_INPUT_CLASSES}),
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
            'description': Textarea(attrs={
                'class': 'textarea'
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(SalaryForm,self).__init__(*args,**kwargs)