"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from django.forms import (ModelForm, DateInput, TextInput, Select, BaseModelFormSet,
                          modelformset_factory, Textarea, BooleanField, ValidationError)
from django.utils.translation import gettext_lazy as _

from aix.models import (ItemModel, WorkOrderJobcardModel, ItemThroughModel, EntityUnitModel)
from aix.settings import MANDO_FORM_INPUT_CLASSES


class WorkOrderJobcardModelCreateForm(ModelForm):
    def __init__(self, *args, entity_slug, user_model, **kwargs):
        super().__init__(*args, **kwargs)
        self.ENTITY_SLUG = entity_slug
        self.USER_MODEL = user_model

    class Meta:
        model = WorkOrderJobcardModel
        fields = [
            'jcd_title',
            'jcd_date',
        ]
        widgets = {
            'jcd_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'jcd_title': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large',
                'placeholder': 'What this JOBCARD is about...'}),
            'work_order': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large',
                'placeholder': 'Work Order this JOBCARD falls...'})
        }
        labels = {
            'for_inventory': _('Is this an inventory jobcard?')
        }


class BaseWorkOrderJobcardModelUpdateForm(ModelForm):

    def __init__(self, *args, entity_slug, user_model, **kwargs):
        super().__init__(*args, **kwargs)
        self.ENTITY_SLUG = entity_slug
        self.USER_MODEL = user_model
        self.JCD_MODEL: WorkOrderJobcardModel = self.instance

    class Meta:
        model = WorkOrderJobcardModel
        fields = [
            'markdown_notes',
        ]
        widgets = {
            'jcd_title': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-large'
            }),
            'jcd_status': Select(attrs={'class': MANDO_FORM_INPUT_CLASSES}),
            'start_mileage': TextInput(attrs={'class': MANDO_FORM_INPUT_CLASSES}),
            'jcd_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'fulfillment_date': DateInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES,
                'placeholder': _('Fulfillment Date (YYYY-MM-DD)...')
            }),
            'scheduled_start_date': DateInput(attrs={
                'type': 'date',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'scheduled_start_time': DateInput(attrs={
                'type': 'time',
                'class': MANDO_FORM_INPUT_CLASSES
            }),
            'markdown_notes': Textarea(attrs={
                'class': 'textarea'
            })
        }
        labels = {
            'jcd_status': _('JOBCARD Status'),
            'fulfilled': _('Mark as Fulfilled'),
            'markdown_notes': _('JOBCARD Notes'),
            'jcd_date': _('Jobcard Date')
        }


class DraftWorkOrderJobcardModelUpdateForm(BaseWorkOrderJobcardModelUpdateForm):
    class Meta(BaseWorkOrderJobcardModelUpdateForm.Meta):
        fields = [
            'jcd_title',
            'jcd_date',
            'scheduled_start_date',
            'scheduled_start_time',
            'markdown_notes',
        ]


class ReviewWorkOrderJobcardModelUpdateForm(BaseWorkOrderJobcardModelUpdateForm):
    class Meta(BaseWorkOrderJobcardModelUpdateForm.Meta):
        fields = [
            'markdown_notes',
        ]


class ApprovedWorkOrderJobcardModelUpdateForm(BaseWorkOrderJobcardModelUpdateForm):
    class Meta(BaseWorkOrderJobcardModelUpdateForm.Meta):
        fields = [
            'markdown_notes',
        ]


class WorkOrderJobcardItemForm(ModelForm):
    create_invoice = BooleanField(required=False)

    class Meta:
        model = ItemThroughModel
        fields = [
            'item_model',
            'jcd_unit_cost',
            'jcd_quantity',
            'entity_unit',
            'jcd_item_status',
            'create_invoice',
        ]
        widgets = {
            'item_model': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-small',
            }),
            'entity_unit': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-small',
            }),
            'jcd_item_status': Select(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-small',
            }),
            'jcd_unit_cost': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-small',
            }),
            'jcd_quantity': TextInput(attrs={
                'class': MANDO_FORM_INPUT_CLASSES + ' is-small',
            })
        }

    def clean(self):
        cleaned_data = super(WorkOrderJobcardItemForm, self).clean()
        jcd_item_status = cleaned_data['jcd_item_status']
        jcd_item_model: ItemThroughModel = self.instance
        if 'jcd_item_status' in self.changed_data:
            jcd_model: WorkOrderJobcardModel = getattr(self, 'JCD_MODEL')
            if jcd_model.jcd_status == jcd_model.JCD_STATUS_APPROVED:
                if not jcd_item_status:
                    raise ValidationError('Cannot assign null status to approved PO.')
                if all([
                    self.instance.invoice_model_id,
                    # jcd_item_status == ItemThroughModel.STATUS_NOT_ORDERED
                ]):
                    raise ValidationError('Cannot assign not ordered status to a invoiced item. '
                                          'Void or delete invoice first')
            if all([
                jcd_item_status in [ItemThroughModel.STATUS_IN_TRANSIT, ItemThroughModel.STATUS_RECEIVED],
                not jcd_item_model.invoice_model_id
            ]):
                raise ValidationError(f'Cannot mark as {jcd_item_status.upper()}. '
                                      'Item must be invoiced first.')
        return cleaned_data


class BaseWorkOrderJobcardItemFormset(BaseModelFormSet):

    def __init__(self, *args, entity_slug, user_model, jcd_model: WorkOrderJobcardModel, **kwargs):
        super().__init__(*args, **kwargs)
        self.USER_MODEL = user_model
        self.ENTITY_SLUG = entity_slug
        self.JCD_MODEL = jcd_model

        items_qs = ItemModel.objects.for_jcd(
            entity_slug=self.ENTITY_SLUG,
            user_model=self.USER_MODEL
        )

        unit_qs = EntityUnitModel.objects.for_entity(
            entity_slug=self.ENTITY_SLUG,
            user_model=self.USER_MODEL
        )

        for form in self.forms:
            form.JCD_MODEL = self.JCD_MODEL
            form.fields['item_model'].queryset = items_qs
            form.fields['entity_unit'].queryset = unit_qs
            if not self.JCD_MODEL.can_edit_items():
                form.fields['jcd_unit_cost'].disabled = True
                form.fields['jcd_quantity'].disabled = True
                form.fields['entity_unit'].disabled = True
                form.fields['item_model'].disabled = True
                form.fields['jcd_item_status'].disabled = True
                if not self.JCD_MODEL.is_approved() or self.JCD_MODEL.is_fulfilled():
                    form.fields['jcd_item_status'].disabled = False
                    form.fields['jcd_item_status'].widget.attrs['class'] += form.instance.get_jcd_status_css_class()
            # JOBCARD is Draft
            else:
                form.fields['jcd_item_status'].disabled = True


CanDeleteWorkOrderJobcardItemFormset = modelformset_factory(
    model=ItemThroughModel,
    form=WorkOrderJobcardItemForm,
    formset=BaseWorkOrderJobcardItemFormset,
    can_delete=True,
    extra=5
)

CanEditWorkOrderJobcardItemFormset = modelformset_factory(
    model=ItemThroughModel,
    form=WorkOrderJobcardItemForm,
    formset=BaseWorkOrderJobcardItemFormset,
    can_delete=True,
    extra=5
)

ReadOnlyWorkOrderJobcardItemFormset = modelformset_factory(
    model=ItemThroughModel,
    form=WorkOrderJobcardItemForm,
    formset=BaseWorkOrderJobcardItemFormset,
    can_delete=False,
    extra=0
)


def get_jcd_item_formset(jcd_model: WorkOrderJobcardModel):
    if jcd_model.is_draft():
        return CanEditWorkOrderJobcardItemFormset
    return ReadOnlyWorkOrderJobcardItemFormset
