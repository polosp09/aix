from django.forms import ModelForm, TextInput, Textarea
from django.utils.translation import gettext_lazy as _

from aix.models.coa import ChartOfAccountModel
from aix.settings import MANDO_FORM_INPUT_CLASSES


class ChartOfAccountsModelForm(ModelForm):
    class Meta:
        model = ChartOfAccountModel
        fields = [
            # 'slug',
            'name',
            'description'
        ]
        labels = {
            'slug': _('CoA ID'),
            'name': _('Name'),
            'description': _('Description'),
        }
        widgets = {
            # 'slug': TextInput(attrs={
            #     'class': MANDO_FORM_INPUT_CLASSES
            # }),
            'name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
        }


class ChartOfAccountsModelUpdateForm(ModelForm):
    class Meta:
        model = ChartOfAccountModel
        fields = [
            'name',
            'locked'
        ]
        labels = {
            'name': _('Name'),
            'description': _('Description'),
        }
        widgets = {
            'name': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'description': Textarea(attrs={
                'class': MANDO_FORM_INPUT_CLASSES
            }),
        }
