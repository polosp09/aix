
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import NotificationModel

class NotificationForm(ModelForm):
    class Meta:
        model = NotificationModel
        fields= ['params', 'is_read', 'is_processed', 'channel', 'external_type_key', 'notify_on', 'employee', 'notification_external_type',]

        widgets = {
            'params': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'channel': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'external_type_key': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'notify_on': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'notification_external_type': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_read': CheckboxInput(attrs={'type': 'checkbox'}),
            'is_processed': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(NotificationForm,self).__init__(*args,**kwargs)