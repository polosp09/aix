
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import RouteSurveyModel
from django.contrib.gis import forms
from mapwidgets.widgets import GoogleMapPointFieldWidget, MapboxPointFieldWidget

class RouteSurveyForm(ModelForm):
    class Meta:
        model = RouteSurveyModel
        fields= ['name', 'start_date', 'end_date', 'purpose', 'bo1', 'bo2', 'bo3', 'is_active', 'start_gps', 'via_gps', 'end_gps', 'location',]

        widgets = {
            'name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'start_date': TextInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'end_date': TextInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            # 'start_place': TextInput(attrs={
            #     'class': MANDO_FORM_INPUT_CLASSES
            # }),
            # 'via_place': TextInput(attrs={
            #     'class': MANDO_FORM_INPUT_CLASSES
            # }),
            # 'end_place': TextInput(attrs={
            #     'class': MANDO_FORM_INPUT_CLASSES
            # }),
            # 'start_gps': TextInput(attrs={
            #     'class': MANDO_FORM_INPUT_CLASSES
            # }),
            # 'via_gps': TextInput(attrs={
            #     'class': MANDO_FORM_INPUT_CLASSES
            # }),
            # 'end_gps': TextInput(attrs={
            #     'class': MANDO_FORM_INPUT_CLASSES
            # }),
            # 'end_gps': GoogleMapPointFieldWidget,
            'purpose': Textarea(attrs={
                'rows': 3,
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'bo1': Textarea(attrs={
                'rows': 3,
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'bo2': Textarea(attrs={
                'rows': 3,
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'bo3': Textarea(attrs={
                'rows': 3,
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'eq_manufacturer': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'eq_type': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'general_notes': Textarea(attrs={
                'class': MANDO_FORM_INPUT_CLASSES,
                'rows': 2
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(RouteSurveyForm,self).__init__(*args,**kwargs)