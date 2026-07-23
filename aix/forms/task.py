from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import TaskModel

class TaskForm(ModelForm):
    class Meta:
        model = TaskModel
        fields= ['task_name', 'description', 'case_status', 'due_at', 'task_status', 'end_date', 'estimated_time',]

        widgets = {
            'task_name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'due_at': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('End Date (YYYY-MM-DD)...')
            }),
            'estimated_time': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'end_date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('End Date (YYYY-MM-DD)...')
            }),
            'case_status': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'task_status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            })
        }

    def __init__(self,*args,**kwargs):
        super(TaskForm,self).__init__(*args,**kwargs)