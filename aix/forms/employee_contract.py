from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import EmployeeContractModel

class EmployeeContractForm(ModelForm):
    class Meta:
        model = EmployeeContractModel
        fields= ['start_date', 'end_date', 'completed', 'comment', 'contract_type', 'employee',]

        widgets = {
            'start_date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('Stat Date (YYYY-MM-DD)...')
            }),
            'end_date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('End Date (YYYY-MM-DD)...')
            }),
            'comment': Textarea(attrs={
                'class': 'textarea'
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'completed': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(EmployeeContractForm,self).__init__(*args,**kwargs)


class EmployeeContractAddForm(EmployeeContractForm):
    class Meta(EmployeeContractForm.Meta):
        fields = [
            'start_date',
            'end_date',
            'comment',
            'contract_type',
            'completed',
        ]