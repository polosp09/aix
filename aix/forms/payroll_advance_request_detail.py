from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import PayrollAdvanceRequestDetailModel

class PayrollAdvanceRequestDetailForm(ModelForm):
    class Meta:
        model = PayrollAdvanceRequestDetailModel
        fields= ['period', 'amount', 'description', 'pa_request',]

        widgets = {
            'period': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'amount': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'pa_request': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(PayrollAdvanceRequestDetailForm,self).__init__(*args,**kwargs)