from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import WorkflowActionModel

class WorkflowActionForm(ModelForm):
    class Meta:
        model = WorkflowActionModel
        fields= ['title', 'document_code', 'form_name', 'description', 'action_code', 'permission', 'parent_id', 'workflow', 'workflow_action_type', 'is_visible', 'is_form', 'has_documents',]

        widgets = {
            'title': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'document_code': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'form_name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'action_code': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'permission': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'parent_id': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'workflow': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'workflow_action_type': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            }),
            'is_visible': CheckboxInput(attrs={'type': 'checkbox'}),
            'is_form': CheckboxInput(attrs={'type': 'checkbox'}),
            'has_documents': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(WorkflowActionForm,self).__init__(*args,**kwargs)