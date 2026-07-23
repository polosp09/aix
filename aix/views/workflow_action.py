from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.workflow_action import WorkflowActionForm
from aix.models.entity import EntityModel
from aix.models.workflow_action import WorkflowActionModel
from aix.views.mixins import LoginRequiredMixIn


class WorkflowActionModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/workflow_action.html'
    context_object_name = 'workflow_actions'
    PAGE_TITLE = _('WorkflowAction List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkflowActionModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WorkflowActionModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/workflow_action.html'
    PAGE_TITLE = _('Create New WorkflowAction')
    form_class = WorkflowActionForm
    context_object_name = 'workflow_action'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkflowActionForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:workflow-action-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        workflow_action_model: WorkflowActionModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        workflow_action_model.entity = entity_model
        workflow_action_model.save()
        return super().form_valid(form)


class WorkflowActionModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/workflow_action.html'
    PAGE_TITLE = _('WorkflowAction Update')
    context_object_name = 'workflow_action'
    form_class = WorkflowActionForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'workflow_action_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return WorkflowActionModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:workflow-action-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 