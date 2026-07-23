from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import IncomingDocumentModel

class IncomingDocumentForm(ModelForm):
    class Meta:
        model = IncomingDocumentModel
        fields= ['doc_from', 'subject', 'delivered_by', 'date_written', 'date_received', 'comment', 'doc_type', 'received_by',]

        widgets = {
            'doc_from': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'subject': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'delivered_by': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'date_written': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('Date-Written (YYYY-MM-DD)...')
            }),
            'date_received': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('Date-Received (YYYY-MM-DD)...')
            }),
            'comment': Textarea(attrs={
                'class': 'textarea'
            }),
            'received_by': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'doc_type': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(IncomingDocumentForm,self).__init__(*args,**kwargs)