from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import RequisitionWorkflowModel

class RequisitionWorkflowForm(ModelForm):
    class Meta:
        model = RequisitionWorkflowModel
        fields= ['workflow', 'requisition', 'workflow_status',]

        widgets = {
            'workflow': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'requisition_action': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'workflow_action': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(RequisitionWorkflowForm,self).__init__(*args,**kwargs)