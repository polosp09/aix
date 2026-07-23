
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import CustomerLocationModel

class CustomerLocationForm(ModelForm):
    class Meta:
        model = CustomerLocationModel
        fields= ['code', 'customer', 'name', 'description', 'is_active']

        widgets = {
            'code': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'customer': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea',
                'rows': 3
            })
        }

    def __init__(self,*args,**kwargs):
        super(CustomerLocationForm,self).__init__(*args,**kwargs)