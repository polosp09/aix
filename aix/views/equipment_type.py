
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.equipment_type import EquipmentTypeForm
from aix.models.entity import EntityModel
from aix.models.equipment_type import EquipmentTypeModel
from aix.views.mixins import LoginRequiredMixIn


class EquipmentTypeModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/equipment/equipment_type.html'
    context_object_name = 'equipment_types'
    PAGE_TITLE = _('EquipmentType List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EquipmentTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EquipmentTypeModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/equipment/equipment_type.html'
    PAGE_TITLE = _('Create New EquipmentType')
    form_class = EquipmentTypeForm
    context_object_name = 'equipment_type'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EquipmentTypeForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:equipment-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        equipment_type_model: EquipmentTypeModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        equipment_type_model.entity = entity_model
        equipment_type_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
        )
        equipment_type_model.save()
        return super().form_valid(form)


class EquipmentTypeModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/equipment/equipment_type.html'
    PAGE_TITLE = _('EquipmentType Update')
    context_object_name = 'equipment_type'
    form_class = EquipmentTypeForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'equipment_type_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return EquipmentTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:equipment-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 