
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.equipment_join import EquipmentJoinForm
from aix.models.entity import EntityModel
from aix.models.equipment_join import EquipmentJoinModel
from aix.views.mixins import LoginRequiredMixIn


class EquipmentJoinModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/hr/equipment_join.html'
    context_object_name = 'equipment_joins'
    PAGE_TITLE = _('EquipmentJoin List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EquipmentJoinModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EquipmentJoinModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/hr/equipment_join.html'
    PAGE_TITLE = _('Create New EquipmentJoin')
    form_class = EquipmentJoinForm
    context_object_name = 'equipment_join'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EquipmentJoinForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:equipment_join-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        equipment_join_model: EquipmentJoinModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        equipment_join_model.entity = entity_model
        equipment_join_model.save()
        return super().form_valid(form)


class EquipmentJoinModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/hr/equipment_join.html'
    PAGE_TITLE = _('EquipmentJoin Update')
    context_object_name = 'equipment_join'
    form_class = EquipmentJoinForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'equipment_join_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return EquipmentJoinModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:equipment_join-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 