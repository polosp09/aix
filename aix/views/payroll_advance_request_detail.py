from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.payroll_advance_request_detail import PayrollAdvanceRequestDetailForm
from aix.models.entity import EntityModel
from aix.models.payroll_advance_request_detail import PayrollAdvanceRequestDetailModel
from aix.views.mixins import LoginRequiredMixIn


class PayrollAdvanceRequestDetailModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/payroll_advance_request_detail.html'
    context_object_name = 'payroll_advance_request_details'
    PAGE_TITLE = _('PayrollAdvanceRequestDetail List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return PayrollAdvanceRequestDetailModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class PayrollAdvanceRequestDetailModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/payroll_advance_request_detail.html'
    PAGE_TITLE = _('Create New PayrollAdvanceRequestDetail')
    form_class = PayrollAdvanceRequestDetailForm
    context_object_name = 'payroll_advance_request_detail'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return PayrollAdvanceRequestDetailForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:payroll-advance-request-detail-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        payroll_advance_request_detail_model: PayrollAdvanceRequestDetailModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        payroll_advance_request_detail_model.entity = entity_model
        payroll_advance_request_detail_model.save()
        return super().form_valid(form)


class PayrollAdvanceRequestDetailModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/payroll_advance_request_detail.html'
    PAGE_TITLE = _('PayrollAdvanceRequestDetail Update')
    context_object_name = 'payroll_advance_request_detail'
    form_class = PayrollAdvanceRequestDetailForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'payroll_advance_request_detail_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return PayrollAdvanceRequestDetailModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:payroll-advance-request-detail-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 