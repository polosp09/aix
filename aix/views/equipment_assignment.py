
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.equipment_assignment import EquipmentAssignmentForm
from aix.models.entity import EntityModel
from aix.models.equipment_assignment import EquipmentAssignmentModel
from aix.views.mixins import LoginRequiredMixIn


class EquipmentAssignmentModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/equipment_assignment.html'
    context_object_name = 'equipment_assignments'
    PAGE_TITLE = _('EquipmentAssignment List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EquipmentAssignmentModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EquipmentAssignmentModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/equipment_assignment.html'
    PAGE_TITLE = _('Create New EquipmentAssignment')
    form_class = EquipmentAssignmentForm
    context_object_name = 'equipment_assignment'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EquipmentAssignmentForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:equipment_assignment-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        equipment_assignment_model: EquipmentAssignmentModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        equipment_assignment_model.entity = entity_model
        equipment_type_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
        )
        equipment_assignment_model.save()
        return super().form_valid(form)


class EquipmentAssignmentModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/equipment_assignment.html'
    PAGE_TITLE = _('EquipmentAssignment Update')
    context_object_name = 'equipment_assignment'
    form_class = EquipmentAssignmentForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'equipment_assignment_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return EquipmentAssignmentModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:equipment_assignment-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 