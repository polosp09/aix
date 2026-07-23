
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import EmployeeModel

class EmployeeForm(ModelForm):
    # OPTIONS_STATUS = (('0', 'False'), ('1', 'True'),)
    # OPTIONS_SALUTATIONS = (('Mr', 'Mr'), ('Mis', 'Mis'), ('Mrs', 'Mrs'),) #('Mr', 'Mis', 'Mrs')
    # OPTIONS_MARITAL_STATUS =(('Single', 'Single'), ('Married', 'Married'),) #('Single', 'Married')
    # OPTIONS_GENDER = (('Male', 'Male'), ('Female', 'Female'),) #('Male', 'Female')
    # initials=forms.CharField(label='initials',widget=forms.TextInput(attrs={'placeholder': 'Enter the File Name', 'id':'file_name', 'class':'form-control'}),max_length=50)
    # first_name=forms.CharField(label='First Name',widget=forms.TextInput(attrs={'placeholder': 'Enter the First Name', 'id':'first_name', 'class':'form-control'}),max_length=50)
    # middle_name=forms.CharField(label='Middle Name',widget=forms.TextInput(attrs={'placeholder': 'Enter the Court File Name', 'id':'court_file_number', 'class':'form-control'}),max_length=50)
    # last_name=forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'placeholder': 'Enter the Plaintiff', 'id':'plaintiff', 'class':'form-control'}),max_length=50)
    # telephone=forms.CharField(label='Telephone',widget=forms.TextInput(attrs={'placeholder': 'Enter the Defendant', 'id':'defendant', 'class':'form-control'}),max_length=50)

    # code=forms.CharField(label='Code',widget=forms.TextInput(attrs={'placeholder': 'Enter the Shelf', 'id':'shelf', 'class':'form-control'}),max_length=50)
    # id_number=forms.CharField(label='ID Number',widget=forms.TextInput(attrs={'placeholder': 'Enter the File Details', 'id':'class':'form-control'}),max_length=50)
    # nssf_number=forms.CharField(label='NSSF Number',widget=forms.TextInput(attrs={'placeholder': 'Enter the Closed Comment', 'id':'id_number', 'class':'form-control'}),max_length=50)
    # tin_number=forms.CharField(label='TIN Number',widget=forms.TextInput(attrs={'placeholder': 'Enter the Closed Comment', 'id':'nssf_number', 'class':'form-control'}),max_length=50)
    # height=forms.CharField(label='Height',widget=forms.TextInput(attrs={'placeholder': 'Enter the Closed Comment', 'id':'tin_number', 'class':'form-control'}),max_length=50)
    # blood_group=forms.CharField(label='Blood-Group',widget=forms.TextInput(attrs={'placeholder': 'Enter the Closed Comment', 'id':'height', 'class':'form-control'}),max_length=50)
    # personal_email=forms.CharField(label='Personal Email',widget=forms.TextInput(attrs={'placeholder': 'Enter the Closed Comment', 'id':'blood_group', 'class':'form-control'}),max_length=50)
    # permanent_address=forms.CharField(label='Permarnent Address',widget=forms.TextInput(attrs={'placeholder': 'Enter the Closed Comment', 'id':'personal_email', 'class':'form-control'}),max_length=50)
    # present_address=forms.CharField(label='Present Address',widget=forms.TextInput(attrs={'placeholder': 'Enter the Closed Comment', 'id':'present_address', 'class':'form-control'}),max_length=50)
    # is_address_same=forms.ChoiceField(label='Is Same Address?',choices=OPTIONS_STATUS)
    # office_number=forms.CharField(label='Office Phone Number',widget=forms.TextInput(attrs={'placeholder': 'Enter the Closed Comment', 'id':'office_number', 'class':'form-control'}),max_length=50)
    # mobile_number=forms.CharField(label='Mobile Phone Number',widget=forms.TextInput(attrs={'placeholder': 'Enter the mobile_number', 'id':'mobile_number', 'class':'form-control'}),max_length=50)
    # date_of_birth=forms.DateField(widget=forms.DateInput(attrs={'type' : 'date', 'max' : datetime.datetime.now().date()}))
    # salutation=forms.ChoiceField(choices=OPTIONS_SALUTATIONS)
    # marital_status=forms.ChoiceField(choices=OPTIONS_MARITAL_STATUS)
    # gender=forms.ChoiceField(choices=OPTIONS_GENDER)

    class Meta:
        model = EmployeeModel
        fields= ['idnumber', 
            'name', 
            'designation', 
            'nationality',
            'gender',
            'dateofbirth',
            'contactnumber', 
            'emergencycontact', 
            'contractstartdate', 
            'locationsite', 
            'passportidno',
            'permitissuedate',
            'permitexpirydate',
            'medicalstartdate',
            'medicalexpirydate',
            'operatorstartdate',
            'operatorexpirydate',
            'defensivestartdate',
            'defensiveexpirydate',
            'category',
            'wostatus',
            'status',
            'imageurl',]

        widgets = {
            'idnumber': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'designation': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'nationality': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'gender': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'dateofbirth': DateInput(attrs={
                'type' : 'date',
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('D.O.B (YYYY-MM-DD)...')
            }),
            'contactnumber': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'emergencycontact': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'contractstartdate': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'locationsite': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'passportidno': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'permitissuedate': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'permitexpirydate': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'medicalstartdate': Textarea(attrs={
                'class': 'textarea'
            }),
            'medicalexpirydate': Textarea(attrs={
                'class': 'textarea'
            }),
            'operatorstartdate': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'operatorexpirydate': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            # 'is_address_same': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)