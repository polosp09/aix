from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import EmployeeLanguageModel

class EmployeeLanguageForm(ModelForm):
    class Meta:
        model = EmployeeLanguageModel
        fields= ['read', 'write', 'speak', 'language', 'employee',]

        widgets = {
            # 'read': TextInput(attrs={
            #     'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            # }),
            # 'write': TextInput(attrs={
            #     'class': MANDO_FORM_INPUT_CLASSES
            # }),
            # 'speak': TextInput(attrs={
            #     'class': MANDO_FORM_INPUT_CLASSES
            # }),
            'language': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(EmployeeLanguageForm,self).__init__(*args,**kwargs)


class EmployeeLanguageAddForm(EmployeeLanguageForm):
    class Meta(EmployeeLanguageForm.Meta):
        fields = [
            'read',
            'write',
            'speak',
            'language',
        ]