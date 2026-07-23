
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.equipment_manufacturer import EquipmentManufacturerForm
from aix.models.entity import EntityModel
from aix.models.equipment_manufacturer import EquipmentManufacturerModel
from aix.views.mixins import LoginRequiredMixIn


class EquipmentManufacturerModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/equipment/equipment_manufacturer.html'
    context_object_name = 'equipment_manufacturers'
    PAGE_TITLE = _('EquipmentManufacturer List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EquipmentManufacturerModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EquipmentManufacturerModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/equipment/equipment_manufacturer.html'
    PAGE_TITLE = _('Create New EquipmentManufacturer')
    form_class = EquipmentManufacturerForm
    context_object_name = 'equipment_manufacturer'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EquipmentManufacturerForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:equipment-manufacturer-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        equipment_manufacturer_model: EquipmentManufacturerModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        equipment_manufacturer_model.entity = entity_model
        equipment_manufacturer_model.save()
        return super().form_valid(form)


class EquipmentManufacturerModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/equipment/equipment_manufacturer.html'
    PAGE_TITLE = _('EquipmentManufacturer Update')
    context_object_name = 'equipment_manufacturer'
    form_class = EquipmentManufacturerForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'equipment_manufacturer_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return EquipmentManufacturerModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:equipment-manufacturer-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 