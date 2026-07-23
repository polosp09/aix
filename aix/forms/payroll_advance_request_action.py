from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import PayrollAdvanceRequestActionModel

class PayrollAdvanceRequestActionForm(ModelForm):
    class Meta:
        model = PayrollAdvanceRequestActionModel
        fields= ['comment', 'par_status', 'pa_request', 'employee',]

        widgets = {
            'comment': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'par_status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'pa_request': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            })
        }

    def __init__(self,*args,**kwargs):
        super(PayrollAdvanceRequestActionForm,self).__init__(*args,**kwargs)