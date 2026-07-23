from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.requisition_flow_type import RequisitionFlowTypeForm
from aix.models.entity import EntityModel
from aix.models.requisition_flow_type import RequisitionFlowTypeModel
from aix.views.mixins import LoginRequiredMixIn


class RequisitionFlowTypeModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/requisition_flow_type.html'
    context_object_name = 'requisition_flow_types'
    PAGE_TITLE = _('RequisitionFlowType List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RequisitionFlowTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class RequisitionFlowTypeModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/requisition_flow_type.html'
    PAGE_TITLE = _('Create New RequisitionFlowType')
    form_class = RequisitionFlowTypeForm
    context_object_name = 'requisition_flow_type'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RequisitionFlowTypeForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:requisition-flow-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        requisition_flow_type_model: RequisitionFlowTypeModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        requisition_flow_type_model.entity = entity_model
        requisition_flow_type_model.save()
        return super().form_valid(form)


class RequisitionFlowTypeModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/requisition_flow_type.html'
    PAGE_TITLE = _('RequisitionFlowType Update')
    context_object_name = 'requisition_flow_type'
    form_class = RequisitionFlowTypeForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'requisition_flow_type_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return RequisitionFlowTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:requisition-flow-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 