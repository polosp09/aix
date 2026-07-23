from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import BusinessIndustryModel

class BusinessIndustryForm(ModelForm):
    #name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'placeholder': 'Enter the name', 'id':'code', 'name', 'class':'form-control'}),max_length=50)
    #code=forms.CharField(label='Code',widget=forms.TextInput(attrs={'placeholder': 'Enter the Code', 'id':'class':'form-control'}),max_length=50)
    #description=forms.TextField(label='Description',widget=forms.TextInput(attrs={'placeholder': 'Enter the Description', 'id':'description', 'class':'form-control'}),max_length=50)


    class Meta:
        model = BusinessIndustryModel
        fields= ['code', 'name', 'description', 'is_active']

        widgets = {
            'code': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': 'textarea'
            }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }


    def __init__(self,*args,**kwargs):
        super(BusinessIndustryForm,self).__init__(*args,**kwargs)
        self.fields['is_active'].empty_label = "CheckBox"