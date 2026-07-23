from django.forms import ModelForm, TextInput, ValidationError
from django.utils.translation import gettext_lazy as _

from aix.models import EntityUnitModel
from aix.settings import MANDO_FORM_INPUT_CLASSES


class EntityUnitModelCreateForm(ModelForm):
    def __init__(self, *args, entity_slug, user_model, **kwargs):
        super().__init__(*args, **kwargs)
        self.ENTITY_SLUG = entity_slug
        self.USER_MODEL = user_model

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 10:
            raise ValidationError(_('Unit name must be at least 10 characters long'))
        return name

    class Meta:
        model = EntityUnitModel
        fields = [
            'name'
        ]
        widgets = {
            'name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
        }


class EntityUnitModelUpdateForm(EntityUnitModelCreateForm):
    pass
