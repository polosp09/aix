from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import SkillModel

class SkillForm(ModelForm):
    class Meta:
        model = SkillModel
        fields= ['name', 'comment', 'years_of_experience', 'employee',]

        widgets = {
            'name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'years_of_experience': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'comment': Textarea(attrs={
                'class': 'textarea'
            })
        }

    def __init__(self,*args,**kwargs):
        super(SkillForm,self).__init__(*args,**kwargs)