from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.payroll_advance_request import PayrollAdvanceRequestForm
from aix.models.entity import EntityModel
from aix.models.payroll_advance_request import PayrollAdvanceRequestModel
from aix.views.mixins import LoginRequiredMixIn


class PayrollAdvanceRequestModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/payroll_advance_request.html'
    context_object_name = 'payroll_advance_requests'
    PAGE_TITLE = _('PayrollAdvanceRequest List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return PayrollAdvanceRequestModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class PayrollAdvanceRequestModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/payroll_advance_request.html'
    PAGE_TITLE = _('Create New PayrollAdvanceRequest')
    form_class = PayrollAdvanceRequestForm
    context_object_name = 'payroll_advance_request'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return PayrollAdvanceRequestForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:payroll-advance-request-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        payroll_advance_request_model: PayrollAdvanceRequestModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        payroll_advance_request_model.entity = entity_model
        payroll_advance_request_model.save()
        return super().form_valid(form)


class PayrollAdvanceRequestModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/payroll_advance_request.html'
    PAGE_TITLE = _('PayrollAdvanceRequest Update')
    context_object_name = 'payroll_advance_request'
    form_class = PayrollAdvanceRequestForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'payroll_advance_request_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return PayrollAdvanceRequestModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:payroll-advance-request-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 