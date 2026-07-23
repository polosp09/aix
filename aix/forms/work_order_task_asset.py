
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import WorkOrderTaskAssetModel

class WorkOrderTaskAssetForm(ModelForm):
    class Meta:
        model = WorkOrderTaskAssetModel
        fields= ['asset', 'startdate', 'enddate', 'description', 'status',]

        widgets = {
            'startdate': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'enddate': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'status': Select(attrs={
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
        super(WorkOrderTaskAssetForm,self).__init__(*args,**kwargs)


class WorkOrderTaskAssetAddForm(WorkOrderTaskAssetForm):
    class Meta(WorkOrderTaskAssetForm.Meta):
        fields = [
            'asset',
            'startdate',
            'enddate',
            'description',
            'status',
        ]