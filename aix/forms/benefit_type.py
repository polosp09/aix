from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import BenefitTypeModel

class BenefitTypeForm(ModelForm):
    class Meta:
        model = BenefitTypeModel
        fields= ['code', 'name', 'polarity', 'value', 'algorithm', 'description', 'benefit_calculation', 'is_taxed', 'is_active',]

        widgets = {
            'code': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'polarity': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'value': Textarea(attrs={
                'class': 'textarea'
            }),
            'algorithm': Textarea(attrs={
                'class': 'textarea'
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            }),
            'benefit_calculation': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(BenefitTypeForm,self).__init__(*args,**kwargs)