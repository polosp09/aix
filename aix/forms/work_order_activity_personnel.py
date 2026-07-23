
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import WorkOrderActivityPersonnelModel

class WorkOrderActivityPersonnelForm(ModelForm):
    class Meta:
        model = WorkOrderActivityPersonnelModel
        fields= ['employee', 'start_date', 'end_date', 'deploy_date', 'relieve_date', 'duties', 'status',]

        widgets = {
            'start_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'end_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'deploy_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'relieve_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'duties': Textarea(attrs={
                'class': 'textarea'
            }),
            'status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            })
        }

    def __init__(self,*args,**kwargs):
        super(WorkOrderActivityPersonnelForm,self).__init__(*args,**kwargs)


class WorkOrderActivityPersonnelAddForm(WorkOrderActivityPersonnelForm):
    class Meta(WorkOrderActivityPersonnelForm.Meta):
        fields = [
            'employee',
            'start_date',
            'end_date',
            'deploy_date',
            'relieve_date',
            'duties',
            'status',
        ]