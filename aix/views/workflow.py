from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.workflow import WorkflowForm
from aix.models.entity import EntityModel
from aix.models.workflow import WorkflowModel
from aix.views.mixins import LoginRequiredMixIn


class WorkflowModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/workflow.html'
    context_object_name = 'workflows'
    PAGE_TITLE = _('Workflow List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkflowModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WorkflowModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/workflow.html'
    PAGE_TITLE = _('Create New Workflow')
    form_class = WorkflowForm
    context_object_name = 'workflow'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkflowForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:workflow-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        workflow_model: WorkflowModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        workflow_model.entity = entity_model
        workflow_model.save()
        return super().form_valid(form)


class WorkflowModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/workflow.html'
    PAGE_TITLE = _('Workflow Update')
    context_object_name = 'workflow'
    form_class = WorkflowForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'workflow_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return WorkflowModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:workflow-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 