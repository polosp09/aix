from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import KpiPobModel

class KpiPobForm(ModelForm):
    class Meta:
        model = KpiPobModel
        fields= ['activity_date', 'activity_description', 'activity_location', 'allocation', 'rotation1', 'rotation2', 'rotation3', 'status', ]

        widgets = {
            'activity_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'activity_description': Textarea(attrs={
                'class': 'textarea'
            }),
            'activity_location': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'rotation1': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'rotation2': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'rotation3': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'allocation': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            })
        }

    def __init__(self,*args,**kwargs):
        super(KpiPobForm,self).__init__(*args,**kwargs)