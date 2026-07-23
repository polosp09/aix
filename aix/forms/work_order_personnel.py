
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import WorkOrderPersonnelModel

class WorkOrderPersonnelForm(ModelForm):
    class Meta:
        model = WorkOrderPersonnelModel
        fields= ['employee', 'startdate', 'enddate', 'deploydate', 'relievedate', 'duties', 'wostatus', 'status',]

        widgets = {
            'startdate': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'enddate': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'deploydate': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'relievedate': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'status': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'duties': Textarea(attrs={
                'class': 'textarea'
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            })
        }

    def __init__(self,*args,**kwargs):
        super(WorkOrderPersonnelForm,self).__init__(*args,**kwargs)


class WorkOrderPersonnelAddForm(WorkOrderPersonnelForm):
    class Meta(WorkOrderPersonnelForm.Meta):
        fields = [
            'startdate',
            'enddate',
            'deploydate',
            'relievedate',
            'duties',
            'employee',
        ]