from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import EmployeeOfTheWeekModel

class EmployeeOfTheWeekForm(ModelForm):
    class Meta:
        model = EmployeeOfTheWeekModel
        fields= ['week_number', 'year', 'count', 'employee',]

        widgets = {
            'week_number': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'year': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'count': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(EmployeeOfTheWeekForm,self).__init__(*args,**kwargs)