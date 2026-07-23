from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import TaskAssigneeModel

class TaskAssigneeForm(ModelForm):
    class Meta:
        model = TaskAssigneeModel
        fields= ['employee', 'task',]

        widgets = {
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'task': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            })
        }

    def __init__(self,*args,**kwargs):
        super(TaskAssigneeForm,self).__init__(*args,**kwargs)