from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import RequisitionWorkflowActionModel

class RequisitionWorkflowActionForm(ModelForm):
    class Meta:
        model = RequisitionWorkflowActionModel
        fields= ['code', 'name', 'requisition_action', 'workflow_action', 'workflow', 'is_processed',]

        widgets = {
            'code': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'requisition_action': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'workflow_action': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_processed': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(RequisitionWorkflowActionForm,self).__init__(*args,**kwargs)