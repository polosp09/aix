from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import RequisitionModel

class RequisitionForm(ModelForm):
    class Meta:
        model = RequisitionModel
        fields= ['date', 'number', 'amount', 'payout_amount', 'description', 'employee', 'supervisor', 'requisition_status', 'requisition_category', 'currency',]

        widgets = {
            'end_date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('End Date (YYYY-MM-DD)...')
            }),
            'number': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'amount': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'payout_amount': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'supervisor': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'requisition_status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'requisition_category': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'currency': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(RequisitionForm,self).__init__(*args,**kwargs)