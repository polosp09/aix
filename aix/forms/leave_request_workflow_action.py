from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import LeaveRequestWorkflowActionModel

class LeaveRequestWorkflowActionForm(ModelForm):
    class Meta:
        model = LeaveRequestWorkflowActionModel
        fields= ['name', 'leave_request_action', 'workflow_action', 'workflow', 'is_processed',]

        widgets = {
            'name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'leave_request_action': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'workflow_action': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'workflow': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_processed': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(LeaveRequestWorkflowActionForm,self).__init__(*args,**kwargs)