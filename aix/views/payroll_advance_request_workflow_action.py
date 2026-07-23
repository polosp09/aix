from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.payroll_advance_request_workflow_action import PayrollAdvanceRequestWorkflowActionForm
from aix.models.entity import EntityModel
from aix.models.payroll_advance_request_workflow_action import PayrollAdvanceRequestWorkflowActionModel
from aix.views.mixins import LoginRequiredMixIn


class PayrollAdvanceRequestWorkflowActionModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/payroll_advance_request_workflow_action.html'
    context_object_name = 'payroll_advance_request_workflow_actions'
    PAGE_TITLE = _('PayrollAdvanceRequestWorkflowAction List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return PayrollAdvanceRequestWorkflowActionModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class PayrollAdvanceRequestWorkflowActionModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/payroll_advance_request_workflow_action.html'
    PAGE_TITLE = _('Create New PayrollAdvanceRequestWorkflowAction')
    form_class = PayrollAdvanceRequestWorkflowActionForm
    context_object_name = 'payroll_advance_request_workflow_action'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return PayrollAdvanceRequestWorkflowActionForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:payroll-advance-request-workflow-action-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        payroll_advance_request_workflow_action_model: PayrollAdvanceRequestWorkflowActionModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        payroll_advance_request_workflow_action_model.entity = entity_model
        payroll_advance_request_workflow_action_model.save()
        return super().form_valid(form)


class PayrollAdvanceRequestWorkflowActionModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/payroll_advance_request_workflow_action.html'
    PAGE_TITLE = _('PayrollAdvanceRequestWorkflowAction Update')
    context_object_name = 'payroll_advance_request_workflow_action'
    form_class = PayrollAdvanceRequestWorkflowActionForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'payroll_advance_request_workflow_action_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return PayrollAdvanceRequestWorkflowActionModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:payroll-advance-request-workflow-action-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 