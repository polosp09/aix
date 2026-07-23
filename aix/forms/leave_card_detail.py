from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import LeaveCardDetailModel

class LeaveCardDetailForm(ModelForm):
    class Meta:
        model = LeaveCardDetailModel
        fields= ['credit', 'days_used', 'days_advanced', 'balance', 'year', 'month', 'leave_card', 'absence_type',]

        widgets = {
            'credit': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'days_used': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'days_advanced': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'balance': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'year': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'month': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(LeaveCardDetailForm,self).__init__(*args,**kwargs)