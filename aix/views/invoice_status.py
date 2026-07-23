from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.invoice_status import InvoiceStatusForm
from aix.models.entity import EntityModel
from aix.models.invoice_status import InvoiceStatusModel
from aix.views.mixins import LoginRequiredMixIn


class InvoiceStatusModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/invoice_status.html'
    context_object_name = 'invoice_statuses'
    PAGE_TITLE = _('InvoiceStatus List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return InvoiceStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class InvoiceStatusModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/invoice_status.html'
    PAGE_TITLE = _('Create New InvoiceStatus')
    form_class = InvoiceStatusForm
    context_object_name = 'invoice_status'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return InvoiceStatusForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:invoice-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        invoice_status_model: InvoiceStatusModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        invoice_status_model.entity = entity_model
        invoice_status_model.save()
        return super().form_valid(form)


class InvoiceStatusModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/invoice_status.html'
    PAGE_TITLE = _('InvoiceStatus Update')
    context_object_name = 'invoice_status'
    form_class = InvoiceStatusForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'invoice_status_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return InvoiceStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:invoice-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 