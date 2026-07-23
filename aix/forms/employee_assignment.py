from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import EmployeeAssignmentModel

class EmployeeAssignmentForm(ModelForm):
    class Meta:
        model = EmployeeAssignmentModel
        fields= ['start_date', 'end_date', 'is_active', 'employee', 'job',]

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
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES 
            }),
            'job': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(EmployeeAssignmentForm,self).__init__(*args,**kwargs)


class EmployeeAssignmentAddForm(EmployeeAssignmentForm):
    class Meta(EmployeeAssignmentForm.Meta):
        fields = [
            'start_date', 
            'end_date', 
            'job', 
            'is_active',
        ]