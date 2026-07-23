from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.workflow_action_type import WorkflowActionTypeForm
from aix.models.entity import EntityModel
from aix.models.workflow_action_type import WorkflowActionTypeModel
from aix.views.mixins import LoginRequiredMixIn


class WorkflowActionTypeModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/workflow_action_type.html'
    context_object_name = 'workflow_action_types'
    PAGE_TITLE = _('WorkflowActionType List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkflowActionTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WorkflowActionTypeModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/workflow_action_type.html'
    PAGE_TITLE = _('Create New WorkflowActionType')
    form_class = WorkflowActionTypeForm
    context_object_name = 'workflow_action_type'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkflowActionTypeForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:workflow-action-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        workflow_action_type_model: WorkflowActionTypeModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        workflow_action_type_model.entity = entity_model
        workflow_action_type_model.save()
        return super().form_valid(form)


class WorkflowActionTypeModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/workflow_action_type.html'
    PAGE_TITLE = _('WorkflowActionType Update')
    context_object_name = 'workflow_action_type'
    form_class = WorkflowActionTypeForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'workflow_action_type_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return WorkflowActionTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:workflow-action-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 