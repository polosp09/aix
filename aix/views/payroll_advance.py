from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.payroll_advance import PayrollAdvanceForm
from aix.models.entity import EntityModel
from aix.models.payroll_advance import PayrollAdvanceModel
from aix.views.mixins import LoginRequiredMixIn


class PayrollAdvanceModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/payroll_advance.html'
    context_object_name = 'payroll_advances'
    PAGE_TITLE = _('PayrollAdvance List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return PayrollAdvanceModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class PayrollAdvanceModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/payroll_advance.html'
    PAGE_TITLE = _('Create New PayrollAdvance')
    form_class = PayrollAdvanceForm
    context_object_name = 'payroll_advance'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return PayrollAdvanceForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:payroll-advance-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        payroll_advance_model: PayrollAdvanceModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        payroll_advance_model.entity = entity_model
        payroll_advance_model.save()
        return super().form_valid(form)


class PayrollAdvanceModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/payroll_advance.html'
    PAGE_TITLE = _('PayrollAdvance Update')
    context_object_name = 'payroll_advance'
    form_class = PayrollAdvanceForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'payroll_advance_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return PayrollAdvanceModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:payroll-advance-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 