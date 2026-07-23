from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import LeaveRequestDetailModel

class LeaveRequestDetailForm(ModelForm):
    class Meta:
        model = LeaveRequestDetailModel
        fields= ['start_date', 'end_date', 'total_calendar_days_requested', 'total_work_days_requested', 'half_day_used', 'description', 'absence_type', 'leave_request',]

        widgets = {
            'start_date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('Start Date (YYYY-MM-DD)...')
            }),
            'end_date': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('End Date (YYYY-MM-DD)...')
            }),
            'total_calendar_days_requested': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'half_day_used': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            }),
            'absence_type': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'leave_request': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(LeaveRequestDetailForm,self).__init__(*args,**kwargs)