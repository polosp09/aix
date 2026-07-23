"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from django.forms import ModelForm, TextInput, EmailInput

from aix.forms.utils import validate_cszc
from aix.models.vendor import VendorModel
from aix.settings import MANDO_FORM_INPUT_CLASSES


class VendorModelForm(ModelForm):

    def clean(self):
        validate_cszc(self.cleaned_data)

    class Meta:
        model = VendorModel
        fields = [
            'vendor_name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'country',
            'phone',
            'email',
            'website',
        ]
        widgets = {
            'vendor_name': TextInput(attrs={
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
            'country': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'phone': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'email': EmailInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'website': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
        }
