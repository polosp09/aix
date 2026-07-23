from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.workflow_status import WorkflowStatusForm
from aix.models.entity import EntityModel
from aix.models.workflow_status import WorkflowStatusModel
from aix.views.mixins import LoginRequiredMixIn


class WorkflowStatusModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/workflow_status.html'
    context_object_name = 'workflow_statuss'
    PAGE_TITLE = _('WorkflowStatus List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkflowStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WorkflowStatusModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/workflow_status.html'
    PAGE_TITLE = _('Create New WorkflowStatus')
    form_class = WorkflowStatusForm
    context_object_name = 'workflow_status'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkflowStatusForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:workflow-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        workflow_status_model: WorkflowStatusModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        workflow_status_model.entity = entity_model
        workflow_status_model.save()
        return super().form_valid(form)


class WorkflowStatusModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/workflow_status.html'
    PAGE_TITLE = _('WorkflowStatus Update')
    context_object_name = 'workflow_status'
    form_class = WorkflowStatusForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'workflow_status_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return WorkflowStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:workflow-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 