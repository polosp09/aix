from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import GeneralNotificationModel

class GeneralNotificationForm(ModelForm):
    class Meta:
        model = GeneralNotificationModel
        fields= ['link', 'parameter', 'extra_parameter', 'title', 'date', 'employee', 'notification_external_type', 'is_read',]

        widgets = {
            'link': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'parameter': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'extra_parameter': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'title': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('Date (YYYY-MM-DD)...')
            }),
            'employee': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'notification_external_type': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_read': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(GeneralNotificationForm,self).__init__(*args,**kwargs)