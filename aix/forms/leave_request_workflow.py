from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import LeaveRequestWorkflowModel

class LeaveRequestWorkflowForm(ModelForm):
    class Meta:
        model = LeaveRequestWorkflowModel
        fields= ['workflow', 'leave_request', 'workflow_status',]

        widgets = {
            'leave_request': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'workflow_status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'workflow': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            })
        }

    def __init__(self,*args,**kwargs):
        super(LeaveRequestWorkflowForm,self).__init__(*args,**kwargs)