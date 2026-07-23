"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from django.forms import ModelForm, Select, TextInput, EmailInput

from aix.forms.utils import validate_cszc
from aix.models.customer import CustomerModel
from aix.settings import MANDO_FORM_INPUT_CLASSES


class CustomerModelForm(ModelForm):

    def clean(self):
        validate_cszc(self.cleaned_data)

    class Meta:
        model = CustomerModel
        fields = [
            'customer_name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone',
            'email',
            'website',
            'business_industry',
            'nation',
            'user',
        ]
        widgets = {
            'customer_name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'address_1': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'address_2': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'city': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'state': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'zip_code': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'phone': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES,
            }),
            'email': EmailInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'website': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'business_industry': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-small',
            }),
            'nation': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-small',
            }),
        }
