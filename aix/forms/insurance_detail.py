from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import InsuranceDetailModel

class InsuranceDetailForm(ModelForm):
    class Meta:
        model = InsuranceDetailModel
        fields= ['policy_name', 'company_name', 'pin_number', 'certificate_number', 'premium', 'address', 'issue_date', 'expiry_date', 'is_active', 'comment', 'employee', 'currency',]

        widgets = {
            'policy_name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'company_name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'pin_number': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'certificate_number': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'premium': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('UGX 0.00')
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
            'address': Textarea(attrs={
                'class': 'textarea'
            }),
            'comment': Textarea(attrs={
                'class': 'textarea'
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'currency': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(InsuranceDetailForm,self).__init__(*args,**kwargs)