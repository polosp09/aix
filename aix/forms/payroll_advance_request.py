from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import PayrollAdvanceRequestModel

class PayrollAdvanceRequestForm(ModelForm):
    class Meta:
        model = PayrollAdvanceRequestModel
        fields= ['date', 'remarks', 'par_status', 'employee', 'supervisor',]

        widgets = {
            'number': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('Date (YYYY-MM-DD)...')
            }),
            'par_status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'supervisor': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'remarks': Textarea(attrs={
                'class': 'textarea'
            })
        }

    def __init__(self,*args,**kwargs):
        super(PayrollAdvanceRequestForm,self).__init__(*args,**kwargs)