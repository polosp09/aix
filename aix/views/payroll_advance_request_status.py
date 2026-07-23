from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.payroll_advance_request_status import PayrollAdvanceRequestStatusForm
from aix.models.entity import EntityModel
from aix.models.payroll_advance_request_status import PayrollAdvanceRequestStatusModel
from aix.views.mixins import LoginRequiredMixIn


class PayrollAdvanceRequestStatusModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/payroll_advance_request_status.html'
    context_object_name = 'payroll_advance_request_statuses'
    PAGE_TITLE = _('PayrollAdvanceRequestStatus List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return PayrollAdvanceRequestStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class PayrollAdvanceRequestStatusModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/payroll_advance_request_status.html'
    PAGE_TITLE = _('Create New PayrollAdvanceRequestStatus')
    form_class = PayrollAdvanceRequestStatusForm
    context_object_name = 'payroll_advance_request_status'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return PayrollAdvanceRequestStatusForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:payroll-advance-request-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        payroll_advance_request_status_model: PayrollAdvanceRequestStatusModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        payroll_advance_request_status_model.entity = entity_model
        payroll_advance_request_status_model.save()
        return super().form_valid(form)


class PayrollAdvanceRequestStatusModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/payroll_advance_request_status.html'
    PAGE_TITLE = _('PayrollAdvanceRequestStatus Update')
    context_object_name = 'payroll_advance_request_status'
    form_class = PayrollAdvanceRequestStatusForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'payroll_advance_request_status_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return PayrollAdvanceRequestStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:payroll-advance-request-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 