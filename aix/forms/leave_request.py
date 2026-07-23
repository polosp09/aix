from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import LeaveRequestModel

class LeaveRequestForm(ModelForm):
    class Meta:
        model = LeaveRequestModel
        fields= ['contact_phone', 'contact_email', 'remarks', 'leave_request_status', 'employee', 'supervisor',]

        widgets = {
            'number': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'contact_phone': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'contact_email': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'remarks': Textarea(attrs={
                'class': 'textarea'
            }),
            'leave_request_status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'supervisor': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            })
        }

    def __init__(self,*args,**kwargs):
        super(LeaveRequestForm,self).__init__(*args,**kwargs)