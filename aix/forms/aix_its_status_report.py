from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import AixItsStatusReportModel

class AixItsStatusReportForm(ModelForm):
    class Meta:
        model = AixItsStatusReportModel
        fields= ['activity', 'activity_type', 'priority', 'startdate', 'duedate', 'status', 'is_active', 'description', ]

        widgets = {
            'code': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'activity': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'priority': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'activity_type': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'startdate': DateInput(attrs={
                'type' : 'date',
            }),
            'duedate': DateInput(attrs={
                'type' : 'date',
            }),
            'status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_active': CheckboxInput(attrs={
                'type': 'checkbox'
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            }),
        }

    def __init__(self,*args,**kwargs):
        super(AixItsStatusReportForm,self).__init__(*args,**kwargs)