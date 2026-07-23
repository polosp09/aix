from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.invoice_action import InvoiceActionForm
from aix.models.entity import EntityModel
from aix.models.invoice_action import InvoiceActionModel
from aix.views.mixins import LoginRequiredMixIn


class InvoiceActionModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/invoice_action.html'
    context_object_name = 'invoice_actions'
    PAGE_TITLE = _('InvoiceAction List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return InvoiceActionModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class InvoiceActionModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/invoice_action.html'
    PAGE_TITLE = _('Create New InvoiceAction')
    form_class = InvoiceActionForm
    context_object_name = 'invoice_action'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return InvoiceActionForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:invoice-action-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        invoice_action_model: InvoiceActionModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        invoice_action_model.entity = entity_model
        invoice_action_model.save()
        return super().form_valid(form)


class InvoiceActionModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/invoice_action.html'
    PAGE_TITLE = _('InvoiceAction Update')
    context_object_name = 'invoice_action'
    form_class = InvoiceActionForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'invoice_action_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return InvoiceActionModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:invoice-action-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 