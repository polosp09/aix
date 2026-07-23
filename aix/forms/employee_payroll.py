from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import EmployeePayrollModel

class EmployeePayrollForm(ModelForm):
    class Meta:
        model = EmployeePayrollModel
        fields= ['start_date', 'end_date', 'net_pay', 'paid', 'employee', 'done_by', 'currency',]

        widgets = {
            'start_date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('End Date (YYYY-MM-DD)...')
            }),
            'end_date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('End Date (YYYY-MM-DD)...')
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'currency': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            })
        }

    def __init__(self,*args,**kwargs):
        super(EmployeePayrollForm,self).__init__(*args,**kwargs)


class EmployeePayrollAddForm(EmployeePayrollForm):
    class Meta(EmployeePayrollForm.Meta):
        fields = [
            'start_date',
            'end_date',
            'net_pay',
            'paid',
            'done_by',
            'currency',
        ]