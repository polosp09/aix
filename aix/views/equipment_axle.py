
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.equipment_axle import EquipmentAxleForm
from aix.models.entity import EntityModel
from aix.models.equipment_axle import EquipmentAxleModel
from aix.views.mixins import LoginRequiredMixIn


class EquipmentAxleModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/hr/equipment_axle.html'
    context_object_name = 'equipment_axles'
    PAGE_TITLE = _('EquipmentAxle List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EquipmentAxleModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EquipmentAxleModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/hr/equipment_axle.html'
    PAGE_TITLE = _('Create New EquipmentAxle')
    form_class = EquipmentAxleForm
    context_object_name = 'equipment_axle'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EquipmentAxleForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:equipment_axle-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        equipment_axle_model: EquipmentAxleModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        equipment_axle_model.entity = entity_model
        equipment_axle_model.save()
        return super().form_valid(form)


class EquipmentAxleModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/hr/equipment_axle.html'
    PAGE_TITLE = _('EquipmentAxle Update')
    context_object_name = 'equipment_axle'
    form_class = EquipmentAxleForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'equipment_axle_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return EquipmentAxleModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:equipment_axle-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 