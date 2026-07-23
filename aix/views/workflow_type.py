from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.workflow_type import WorkflowTypeForm
from aix.models.entity import EntityModel
from aix.models.workflow_type import WorkflowTypeModel
from aix.views.mixins import LoginRequiredMixIn


class WorkflowTypeModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/workflow_type.html'
    context_object_name = 'workflow_types'
    PAGE_TITLE = _('WorkflowType List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkflowTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WorkflowTypeModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/workflow_type.html'
    PAGE_TITLE = _('Create New WorkflowType')
    form_class = WorkflowTypeForm
    context_object_name = 'workflow_type'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkflowTypeForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:workflow-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        workflow_type_model: WorkflowTypeModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        workflow_type_model.entity = entity_model
        workflow_type_model.save()
        return super().form_valid(form)


class WorkflowTypeModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/workflow_type.html'
    PAGE_TITLE = _('WorkflowType Update')
    context_object_name = 'workflow_type'
    form_class = WorkflowTypeForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'workflow_type_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return WorkflowTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:workflow-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 