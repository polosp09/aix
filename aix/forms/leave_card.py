from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import LeaveCardModel

class LeaveCardForm(ModelForm):
    class Meta:
        model = LeaveCardModel
        fields= ['start_date', 'end_date', 'employee', ]

        widgets = {
            'employee': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
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
            'description': Textarea(attrs={
                'class': 'textarea'
            }),
            'parent_id': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_dirty': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(LeaveCardForm,self).__init__(*args,**kwargs)

class LeaveCardAddForm(LeaveCardForm):
    class Meta(LeaveCardForm.Meta):
        fields = [
            'start_date',
            'end_date',
        ]