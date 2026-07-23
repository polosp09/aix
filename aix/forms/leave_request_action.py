from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import LeaveRequestActionModel

class LeaveRequestActionForm(ModelForm):
    class Meta:
        model = LeaveRequestActionModel
        fields= ['comment', 'leave_request_status', 'leave_request', 'employee',]

        widgets = {
            'leave_request_status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'leave_request': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'comment': Textarea(attrs={
                'class': 'textarea'
            })
        }

    def __init__(self,*args,**kwargs):
        super(LeaveRequestActionForm,self).__init__(*args,**kwargs)
