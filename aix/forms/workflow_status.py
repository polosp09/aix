from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import WorkflowStatusModel

class WorkflowStatusForm(ModelForm):
    class Meta:
        model = WorkflowStatusModel
        fields= ['title', 'description', 'workflow_type',]

        widgets = {
            'title': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'workflow_type': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            })
        }

    def __init__(self,*args,**kwargs):
        super(WorkflowStatusForm,self).__init__(*args,**kwargs)