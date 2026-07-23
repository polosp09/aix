from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.invoice_type import InvoiceTypeForm
from aix.models.entity import EntityModel
from aix.models.invoice_type import InvoiceTypeModel
from aix.views.mixins import LoginRequiredMixIn


class InvoiceTypeModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/invoice_type.html'
    context_object_name = 'invoice_types'
    PAGE_TITLE = _('InvoiceType List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return InvoiceTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class InvoiceTypeModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/invoice_type.html'
    PAGE_TITLE = _('Create New InvoiceType')
    form_class = InvoiceTypeForm
    context_object_name = 'invoice_type'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return InvoiceTypeForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:invoice-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        invoice_type_model: InvoiceTypeModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        invoice_type_model.entity = entity_model
        invoice_type_model.save()
        return super().form_valid(form)


class InvoiceTypeModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/invoice_type.html'
    PAGE_TITLE = _('InvoiceType Update')
    context_object_name = 'invoice_type'
    form_class = InvoiceTypeForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'invoice_type_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return InvoiceTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:invoice-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 