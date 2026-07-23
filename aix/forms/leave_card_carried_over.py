from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import LeaveCardCarriedOverModel

class LeaveCardCarriedOverForm(ModelForm):
    class Meta:
        model = LeaveCardCarriedOverModel
        fields= ['days', 'leave_card', 'absence_type',]

        widgets = {
            'days': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'leave_card': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'absence_type': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            })
        }

    def __init__(self,*args,**kwargs):
        super(LeaveCardCarriedOverForm,self).__init__(*args,**kwargs)