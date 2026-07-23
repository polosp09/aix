from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import DocumentModel

class DocumentForm(ModelForm):
    class Meta:
        model = DocumentModel
        fields= ['name', 'doc_type', 'description', 'doc_status',]

        widgets = {
            'name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'extension': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'name_on_file': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'temp_key': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'external_key': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'mime_type': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'size': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'doc_type': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'doc_status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            })
        }

    def __init__(self,*args,**kwargs):
        super(DocumentForm,self).__init__(*args,**kwargs)