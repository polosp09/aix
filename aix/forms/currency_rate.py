from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import CurrencyRateModel

class CurrencyRateForm(ModelForm):
    class Meta:
        model = CurrencyRateModel
        fields= ['date', 'currency', 'buying', 'selling',]

        widgets = {
            'buying': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'selling': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'currency': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            })
        }

    def __init__(self,*args,**kwargs):
        super(CurrencyRateForm,self).__init__(*args,**kwargs)