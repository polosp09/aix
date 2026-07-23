from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import AbsenceDateModel

class AbsenceDateForm(ModelForm):
    class Meta:
        model = AbsenceDateModel
        fields= ['date', 'is_half_day', 'absence_type', 'employee',]

        widgets = {
            'date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('Start Date (YYYY-MM-DD)...')
            }),
            'absence_type': Select(attrs={'class': MANDO_FORM_INPUT_CLASSES}),
            'employee': Select(attrs={'class': MANDO_FORM_INPUT_CLASSES}),
            'is_half_day': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(AbsenceDateForm,self).__init__(*args,**kwargs)