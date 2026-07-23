from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.requisition_workflow import RequisitionWorkflowForm
from aix.models.entity import EntityModel
from aix.models.requisition_workflow import RequisitionWorkflowModel
from aix.views.mixins import LoginRequiredMixIn


class RequisitionWorkflowModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/requisition_workflow.html'
    context_object_name = 'requisition_workflows'
    PAGE_TITLE = _('RequisitionWorkflow List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RequisitionWorkflowModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class RequisitionWorkflowModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/requisition_workflow.html'
    PAGE_TITLE = _('Create New RequisitionWorkflow')
    form_class = RequisitionWorkflowForm
    context_object_name = 'requisition_workflow'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RequisitionWorkflowForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:requisition-workflow-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        requisition_workflow_model: RequisitionWorkflowModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        requisition_workflow_model.entity = entity_model
        requisition_workflow_model.save()
        return super().form_valid(form)


class RequisitionWorkflowModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/requisition_workflow.html'
    PAGE_TITLE = _('RequisitionWorkflow Update')
    context_object_name = 'requisition_workflow'
    form_class = RequisitionWorkflowForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'requisition_workflow_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return RequisitionWorkflowModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:requisition-workflow-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 