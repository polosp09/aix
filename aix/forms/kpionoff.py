from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import KpiOnOffModel

class KpiOnOffForm(ModelForm):
    class Meta:
        model = KpiOnOffModel
        fields= ['asset', 'location', 'activity_date', 'activity_description', 'on_hire', 'off_hire', 'maintenance', 'allocation', 'comments', 'status', ]

        widgets = {
            'activity_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'activity_description': Textarea(attrs={
                'class': 'textarea'
            }),
            'on_hire': DateInput(attrs={
                'type': 'time',
                'class': 'timepicker'
            }),
            'off_hire': DateInput(attrs={
                'type': 'time',
                'class': 'timepicker'
            }),
            'maintenance': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'location': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'allocation': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'comments': Textarea(attrs={
                'class': 'textarea'
            }),
            'status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'asset': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
        }

    def __init__(self,*args,**kwargs):
        super(KpiOnOffForm,self).__init__(*args,**kwargs)