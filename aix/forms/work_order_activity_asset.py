
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import WorkOrderActivityAssetModel, WorkOrderTaskAssetModel, WorkOrderActivityModel, EquipmentModel

class WorkOrderActivityAssetForm(ModelForm):
    class Meta:
        model = WorkOrderActivityAssetModel
        fields= ['asset', 'start_date', 'end_date', 'description', 'status',]

        widgets = {
            'start_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'end_date': DateInput(attrs={
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

    def __init__(self,*args,assets,**kwargs):
        super().__init__(*args, **kwargs)

        # form = self.get_form_class()(**kwargs)
        # form = WorkOrderActivityAssetForm(self, assets=assets, *args,**kwargs)
        
        self.fields['asset'].queryset = assets
        self.fields['asset'].empty_label = _('Select Asset')
        # return form
        # super(WorkOrderActivityAssetForm,self).__init__(*args,**kwargs)


class WorkOrderActivityAssetAddForm(WorkOrderActivityAssetForm):
    class Meta(WorkOrderActivityAssetForm.Meta):
        fields = [
            'asset',
            'start_date',
            'end_date',
            'description',
            'status',
        ]