from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import PayrollAdvanceRequestWorkflowActionModel

class PayrollAdvanceRequestWorkflowActionForm(ModelForm):
    class Meta:
        model = PayrollAdvanceRequestWorkflowActionModel
        fields= ['code', 'name', 'par_action', 'workflow_action', 'par_workflow', 'is_processed', ]

        widgets = {
            'code': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'par_action': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'workflow_action': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'par_workflow': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_processed': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(PayrollAdvanceRequestWorkflowActionForm,self).__init__(*args,**kwargs)