
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import WorkOrderActivityDocumentModel

class WorkOrderActivityDocumentForm(ModelForm):
    class Meta:
        model = WorkOrderActivityDocumentModel
        fields= ['doc_date', 'document', 'description', 'status',]

        widgets = {
            'doc_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            }),
            'document': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            })
        }

    def __init__(self,*args,**kwargs):
        super(WorkOrderActivityDocumentForm,self).__init__(*args,**kwargs)


class WorkOrderActivityDocumentAddForm(WorkOrderActivityDocumentForm):
    class Meta(WorkOrderActivityDocumentForm.Meta):
        fields = [
            'document',
            'doc_date',
            'description',
            'status',
        ]