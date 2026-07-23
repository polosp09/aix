from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import WeeklyEmployeeModel

class WeeklyEmployeeForm(ModelForm):
    class Meta:
        model = WeeklyEmployeeModel
        fields= ['employee', 'point', 'action',]

        widgets = {
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'point': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'action': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            })
        }

    def __init__(self,*args,**kwargs):
        super(WeeklyEmployeeForm,self).__init__(*args,**kwargs)