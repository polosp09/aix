from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.payroll_advance_request_workflow import PayrollAdvanceRequestWorkflowForm
from aix.models.entity import EntityModel
from aix.models.payroll_advance_request_workflow import PayrollAdvanceRequestWorkflowModel
from aix.views.mixins import LoginRequiredMixIn


class PayrollAdvanceRequestWorkflowModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/payroll_advance_request_workflow.html'
    context_object_name = 'payroll_advance_request_workflows'
    PAGE_TITLE = _('PayrollAdvanceRequestWorkflow List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return PayrollAdvanceRequestWorkflowModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class PayrollAdvanceRequestWorkflowModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/payroll_advance_request_workflow.html'
    PAGE_TITLE = _('Create New PayrollAdvanceRequestWorkflow')
    form_class = PayrollAdvanceRequestWorkflowForm
    context_object_name = 'payroll_advance_request_workflow'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return PayrollAdvanceRequestWorkflowForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:payroll-advance-request-workflow-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        payroll_advance_request_workflow_model: PayrollAdvanceRequestWorkflowModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        payroll_advance_request_workflow_model.entity = entity_model
        payroll_advance_request_workflow_model.save()
        return super().form_valid(form)


class PayrollAdvanceRequestWorkflowModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/payroll_advance_request_workflow.html'
    PAGE_TITLE = _('PayrollAdvanceRequestWorkflow Update')
    context_object_name = 'payroll_advance_request_workflow'
    form_class = PayrollAdvanceRequestWorkflowForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'payroll_advance_request_workflow_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return PayrollAdvanceRequestWorkflowModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:payroll-advance-request-workflow-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 