from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.requisition_status import RequisitionStatusForm
from aix.models.entity import EntityModel
from aix.models.requisition_status import RequisitionStatusModel
from aix.views.mixins import LoginRequiredMixIn


class RequisitionStatusModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/requisition_status.html'
    context_object_name = 'requisition_statuss'
    PAGE_TITLE = _('RequisitionStatus List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RequisitionStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class RequisitionStatusModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/requisition_status.html'
    PAGE_TITLE = _('Create New RequisitionStatus')
    form_class = RequisitionStatusForm
    context_object_name = 'requisition_status'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RequisitionStatusForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:requisition-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        requisition_status_model: RequisitionStatusModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        requisition_status_model.entity = entity_model
        requisition_status_model.save()
        return super().form_valid(form)


class RequisitionStatusModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/requisition_status.html'
    PAGE_TITLE = _('RequisitionStatus Update')
    context_object_name = 'requisition_status'
    form_class = RequisitionStatusForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'requisition_status_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return RequisitionStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:requisition-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 