
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import WorkOrderAssetModel

class WorkOrderAssetForm(ModelForm):
    class Meta:
        model = WorkOrderAssetModel
        fields= ['asset', 'startdate', 'enddate', 'description', 'wostatus', 'status',]

        widgets = {
            'startdate': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'enddate': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'status': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            }),
            'asset': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            })
        }

    def __init__(self,*args,**kwargs):
        super(WorkOrderAssetForm,self).__init__(*args,**kwargs)


class WorkOrderAssetAddForm(WorkOrderAssetForm):
    class Meta(WorkOrderAssetForm.Meta):
        fields = [
            'startdate',
            'enddate',
            'description',
            'asset',
        ]