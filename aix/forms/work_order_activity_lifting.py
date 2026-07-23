from django import forms
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import WorkOrderActivityLiftingModel, WorkOrderTaskAssetModel, WorkOrderActivityModel, EquipmentModel
from django_json_widget.widgets import JSONEditorWidget

class WorkOrderActivityLiftingForm(ModelForm):
    class Meta:
        model = WorkOrderActivityLiftingModel
        fields= ['trip_code', 'equipment', 'operator', 'supervisor', 'operators', 'status', 'comments',]

        widgets = {
            'equipment': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'operator': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'supervisor': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            # 'driver': Select(attrs={
            #     'class': MANDO_FORM_INPUT_CLASSES
            # }),
            'status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'comments': Textarea(attrs={
                'class': 'textarea'
            }),
            'operators': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            # 'operators': JSONEditorWidget,
            'operators': forms.CheckboxSelectMultiple(attrs={'class': 'custom-checkbox-class'}),
            }

    def __init__(self,*args,assets,staff,**kwargs):
        super().__init__(*args, **kwargs)

        # form = self.get_form_class()(**kwargs)
        # form = WorkOrderActivityLiftingForm(self, transports=transports, *args,**kwargs)
        # print(staff)
        self.fields['equipment'].queryset = assets
        self.fields['equipment'].empty_label = _('Select Equipment')
        self.fields['operators'].queryset = staff
        # return form
        # super(WorkOrderActivityLiftingForm,self).__init__(*args,**kwargs)


class WorkOrderActivityLiftingAddForm(WorkOrderActivityLiftingForm):
    class Meta(WorkOrderActivityLiftingForm.Meta):
        fields = [
            'trip_code',
            'equipment',
            'operator',
            'supervisor',
            'operators',
            'comments',
            'status',
        ]