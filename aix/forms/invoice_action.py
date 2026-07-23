from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import InvoiceActionModel

class InvoiceActionForm(ModelForm):
    class Meta:
        model = InvoiceActionModel
        fields= ['comment', 'invoice_status', 'invoice', 'employee',]

        widgets = {
            'comment': Textarea(attrs={
                'class': 'textarea'
            }),
            'invoice_status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'invoice': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            })
        }

    def __init__(self,*args,**kwargs):
        super(InvoiceActionForm,self).__init__(*args,**kwargs)