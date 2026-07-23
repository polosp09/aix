from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import KpiHseModel

class KpiHseForm(ModelForm):
    class Meta:
        model = KpiHseModel
        fields= [
            'activity_date',
            'start_time',
            'end_time',
            'fat',
            'lti',
            'rwdc',
            'mtc',
            'fac',
            'hipo',
            'envdam',
            'nmi',
            'matloss',
            'ptw',
            'ptw_description',
            'tbt',
            'tbt_description',
            'hht',
            'hht_description',
            'drills',
            'drills_description',
            'audit',
            'audit_description',
            'training_subject',
            'reporting_cards',
            'rc_description',
            'safety_initiative',
            'si_description',
            'status', ]

        widgets = {
            'activity_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'activity_description': Textarea(attrs={
                'class': 'textarea'
            }),
            'start_time': DateInput(attrs={
                'type': 'time',
                'class': 'timepicker'
            }),
            'end_time': DateInput(attrs={
                'type': 'time',
                'class': 'timepicker'
            }),
        }

    def __init__(self,*args,**kwargs):
        super(KpiHseForm,self).__init__(*args,**kwargs)