from django import forms
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import ReportModel

class ReportForm(ModelForm):
    class Meta:
        model = ReportModel
        fields= ['rpt_name', 'description', 'sort_by', 'order_by', 'order_by_dir', 'is_active',]

        widgets = {
            'rpt_name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            }),
            'sort_by': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'order_by': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'order_by_dir': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(ReportForm,self).__init__(*args,**kwargs)


ORDERBYDIR = (("ASC", "ASC"), ("DESC", "DESC"))
class ReporterForm(forms.Form):
    report_name = forms.CharField()
    sort_by = forms.CharField()
    order_by = forms.CharField()
    order_by_dir = forms.CharField()
