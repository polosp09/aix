
from django.forms import (ModelForm, DateInput, TextInput, Select,
                          CheckboxInput, BaseModelFormSet,
                          modelformset_factory, Textarea)
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from aix.settings import MANDO_FORM_INPUT_CLASSES
from aix.models import RouteSurveyModel, RouteSurveyInfoModel

class RouteSurveyInfoForm(ModelForm):
    class Meta:
        model = RouteSurveyInfoModel
        fields= ['route_code', 'south_coordinate', 'east_coordinate', 'distance_start', 'color', 'koc', 'kfi_description', 'photo', 'location', 'is_active',]

        widgets = {
            'route_code': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'distance_start': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'color': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'koc': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'kfi_description': Textarea(attrs={
                'class': 'textarea'
            }),
            # 'photo': Textarea(attrs={
            #     'class': 'textarea'
            # }),
            'is_active': CheckboxInput(attrs={'type': 'checkbox'})
        }

    def __init__(self,*args,**kwargs):
        super(RouteSurveyInfoForm,self).__init__(*args,**kwargs)

class RouteSurveyInfoAddForm(RouteSurveyInfoForm):
    class Meta(RouteSurveyInfoForm.Meta):
        fields = [
            'route_code', 
            'south_coordinate', 
            'east_coordinate', 
            'distance_start', 
            'color', 
            'koc', 
            'kfi_description', 
            'photo', 
            'is_active'
        ]

class BaseRouteSurveyItemFormset(BaseModelFormSet):

    def __init__(self, *args, entity_slug, user_model, route_survey_model: RouteSurveyModel, **kwargs):
        super().__init__(*args, **kwargs)
        self.USER_MODEL = user_model
        self.ENTITY_SLUG = entity_slug

RouteSurveyItemFormset = modelformset_factory(
    model=RouteSurveyInfoModel,
    form=RouteSurveyInfoForm,
    formset=BaseRouteSurveyItemFormset,
    can_delete=True,
    extra=5
)