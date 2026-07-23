from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import NotificationTrackerModel

class NotificationTrackerForm(ModelForm):
    class Meta:
        model = NotificationTrackerModel
        fields= ['next_notification',]

        widgets = {
            'next_notification': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            })
        }

    def __init__(self,*args,**kwargs):
        super(NotificationTrackerForm,self).__init__(*args,**kwargs)