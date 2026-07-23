from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import RequisitionActionModel

class RequisitionActionForm(ModelForm):
    class Meta:
        model = RequisitionActionModel
        fields= ['comment', 'employee', 'requisition_status', 'requisition',]

        widgets = {
            'comment': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'requisition_status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'requisition': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            })
        }

    def __init__(self,*args,**kwargs):
        super(RequisitionActionForm,self).__init__(*args,**kwargs)