from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.leave_request_workflow import LeaveRequestWorkflowForm
from aix.models.entity import EntityModel
from aix.models.leave_request_workflow import LeaveRequestWorkflowModel
from aix.views.mixins import LoginRequiredMixIn


class LeaveRequestWorkflowModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/leave_request_workflow.html'
    context_object_name = 'leave_request_workflows'
    PAGE_TITLE = _('LeaveRequestWorkflow List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LeaveRequestWorkflowModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class LeaveRequestWorkflowModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/leave_request_workflow.html'
    PAGE_TITLE = _('Create New LeaveRequestWorkflow')
    form_class = LeaveRequestWorkflowForm
    context_object_name = 'leave_request_workflow'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LeaveRequestWorkflowForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:leave-request-workflow-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        leave_request_workflow_model: LeaveRequestWorkflowModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        leave_request_workflow_model.entity = entity_model
        leave_request_workflow_model.save()
        return super().form_valid(form)


class LeaveRequestWorkflowModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/leave_request_workflow.html'
    PAGE_TITLE = _('LeaveRequestWorkflow Update')
    context_object_name = 'leave_request_workflow'
    form_class = LeaveRequestWorkflowForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'leave_request_workflow_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return LeaveRequestWorkflowModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:leave-request-workflow-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 