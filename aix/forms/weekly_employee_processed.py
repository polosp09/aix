from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import WeeklyEmployeeProcessedModel

class WeeklyEmployeeProcessedForm(ModelForm):
    class Meta:
        model = WeeklyEmployeeProcessedModel
        fields= ['employee', 'points',]

        widgets = {
            'employee': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'points': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            })
        }

    def __init__(self,*args,**kwargs):
        super(WeeklyEmployeeProcessedForm,self).__init__(*args,**kwargs)