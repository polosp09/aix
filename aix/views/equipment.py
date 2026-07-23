
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.equipment import EquipmentForm
from aix.models.entity import EntityModel
from aix.models.equipment import EquipmentModel
from aix.views.mixins import LoginRequiredMixIn


class EquipmentModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/equipment/equipment.html'
    context_object_name = 'equipments'
    PAGE_TITLE = _('Equipment List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EquipmentModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EquipmentModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/equipment/equipment.html'
    PAGE_TITLE = _('Create New Equipment')
    form_class = EquipmentForm
    context_object_name = 'equipment'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EquipmentForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:equipment-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        equipment_model: EquipmentModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        equipment_model.entity = entity_model
        equipment_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
        )
        equipment_model.save()
        return super().form_valid(form)


class EquipmentModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/equipment/equipment.html'
    PAGE_TITLE = _('Equipment Update')
    context_object_name = 'equipment'
    form_class = EquipmentForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'equipment_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return EquipmentModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:equipment-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 