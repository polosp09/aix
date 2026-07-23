from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.requisition_action import RequisitionActionForm
from aix.models.entity import EntityModel
from aix.models.requisition_action import RequisitionActionModel
from aix.views.mixins import LoginRequiredMixIn


class RequisitionActionModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/requisition_action.html'
    context_object_name = 'requisition_actions'
    PAGE_TITLE = _('RequisitionAction List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RequisitionActionModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class RequisitionActionModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/requisition_action.html'
    PAGE_TITLE = _('Create New RequisitionAction')
    form_class = RequisitionActionForm
    context_object_name = 'requisition_action'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RequisitionActionForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:requisition-action-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        requisition_action_model: RequisitionActionModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        requisition_action_model.entity = entity_model
        requisition_action_model.save()
        return super().form_valid(form)


class RequisitionActionModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/requisition_action.html'
    PAGE_TITLE = _('RequisitionAction Update')
    context_object_name = 'requisition_action'
    form_class = RequisitionActionForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'requisition_action_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return RequisitionActionModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:requisition-action-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 