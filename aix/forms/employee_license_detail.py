from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import EmployeeLicenseDetailModel

class EmployeeLicenseDetailForm(ModelForm):
    class Meta:
        model = EmployeeLicenseDetailModel
        fields= ['issue_date', 'expiry_date', 'comment', 'license_type', 'employee', 'valid',]

        widgets = {
            'issue_date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('End Date (YYYY-MM-DD)...')
            }),
            'expiry_date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('End Date (YYYY-MM-DD)...')
            }),
            'license_type': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'comment': Textarea(attrs={
                'class': 'textarea'
            }),
            #'valid': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(EmployeeLicenseDetailForm,self).__init__(*args,**kwargs)



class EmployeeLicenseDetailAddForm(EmployeeLicenseDetailForm):
    class Meta(EmployeeLicenseDetailForm.Meta):
        fields = [
            'issue_date',
            'expiry_date',
            'valid',
            'comment',
            'license_type',
        ]