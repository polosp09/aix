from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import EmployeePayrollBenefitModel

class EmployeePayrollBenefitForm(ModelForm):
    class Meta:
        model = EmployeePayrollBenefitModel
        fields= ['polarity', 'amount', 'employee_payroll', 'benefit_type', 'is_taxed',]

        widgets = {
            'polarity': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'amount': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'employee_payroll': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'benefit_type': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            }),
            'is_taxed': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(EmployeePayrollBenefitForm,self).__init__(*args,**kwargs)