
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import WorkOrderActivityTransportModel, WorkOrderTaskAssetModel, WorkOrderActivityModel, EquipmentModel

class WorkOrderActivityTransportForm(ModelForm):
    class Meta:
        model = WorkOrderActivityTransportModel
        fields= ['trip_code', 'driver', 'vehicle', 'etd', 'eta', 'atd', 'ata', 'comments', 'status',]

        widgets = {
            'etd': DateInput(attrs={
                'type': 'time',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'eta': DateInput(attrs={
                'type': 'time',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'atd': DateInput(attrs={
                'type': 'time',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'ata': DateInput(attrs={
                'type': 'time',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            # 'driver': Select(attrs={
            #     'class': MANDO_FORM_INPUT_CLASSES
            # }),
            'vehicle': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'comments': Textarea(attrs={
                'class': 'textarea'
            }),
            'vehicle': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            })
        }

    def __init__(self,*args,vehicles,staff,**kwargs):
        super().__init__(*args, **kwargs)

        # form = self.get_form_class()(**kwargs)
        # form = WorkOrderActivityTransportForm(self, transports=transports, *args,**kwargs)
        
        self.fields['vehicle'].queryset = vehicles
        self.fields['vehicle'].empty_label = _('Select Vehicle')
        self.fields['driver'].queryset = staff
        self.fields['assistants'].queryset = staff
        # return form
        # super(WorkOrderActivityTransportForm,self).__init__(*args,**kwargs)


class WorkOrderActivityTransportAddForm(WorkOrderActivityTransportForm):
    class Meta(WorkOrderActivityTransportForm.Meta):
        fields = [
            'vehicle',
            'driver',
            'etd',
            'eta',
            'atd',
            'ata',
            'comments',
            'status',
        ]