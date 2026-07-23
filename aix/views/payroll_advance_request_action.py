from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.payroll_advance_request_action import PayrollAdvanceRequestActionForm
from aix.models.entity import EntityModel
from aix.models.payroll_advance_request_action import PayrollAdvanceRequestActionModel
from aix.views.mixins import LoginRequiredMixIn


class PayrollAdvanceRequestActionModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/payroll_advance_request_action.html'
    context_object_name = 'payroll_advance_request_actions'
    PAGE_TITLE = _('PayrollAdvanceRequestAction List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return PayrollAdvanceRequestActionModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class PayrollAdvanceRequestActionModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/payroll_advance_request_action.html'
    PAGE_TITLE = _('Create New PayrollAdvanceRequestAction')
    form_class = PayrollAdvanceRequestActionForm
    context_object_name = 'payroll_advance_request_action'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return PayrollAdvanceRequestActionForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:payroll-advance-request-action-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        payroll_advance_request_action_model: PayrollAdvanceRequestActionModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        payroll_advance_request_action_model.entity = entity_model
        payroll_advance_request_action_model.save()
        return super().form_valid(form)


class PayrollAdvanceRequestActionModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/payroll_advance_request_action.html'
    PAGE_TITLE = _('PayrollAdvanceRequestAction Update')
    context_object_name = 'payroll_advance_request_action'
    form_class = PayrollAdvanceRequestActionForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'payroll_advance_request_action_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return PayrollAdvanceRequestActionModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:payroll-advance-request-action-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 