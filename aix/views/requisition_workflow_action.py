from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.requisition_workflow_action import RequisitionWorkflowActionForm
from aix.models.entity import EntityModel
from aix.models.requisition_workflow_action import RequisitionWorkflowActionModel
from aix.views.mixins import LoginRequiredMixIn


class RequisitionWorkflowActionModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/requisition_workflow_action.html'
    context_object_name = 'requisition_workflow_actions'
    PAGE_TITLE = _('RequisitionWorkflowAction List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RequisitionWorkflowActionModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class RequisitionWorkflowActionModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/requisition_workflow_action.html'
    PAGE_TITLE = _('Create New RequisitionWorkflowAction')
    form_class = RequisitionWorkflowActionForm
    context_object_name = 'requisition_workflow_action'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RequisitionWorkflowActionForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:requisition-workflow-action-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        requisition_workflow_action_model: RequisitionWorkflowActionModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        requisition_workflow_action_model.entity = entity_model
        requisition_workflow_action_model.save()
        return super().form_valid(form)


class RequisitionWorkflowActionModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/requisition_workflow_action.html'
    PAGE_TITLE = _('RequisitionWorkflowAction Update')
    context_object_name = 'requisition_workflow_action'
    form_class = RequisitionWorkflowActionForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'requisition_workflow_action_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return RequisitionWorkflowActionModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:requisition-workflow-action-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 