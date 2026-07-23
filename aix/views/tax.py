from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.tax import TaxForm
from aix.models.entity import EntityModel
from aix.models.tax import TaxModel
from aix.views.mixins import LoginRequiredMixIn


class TaxModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/tax.html'
    context_object_name = 'taxes'
    PAGE_TITLE = _('Tax List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return TaxModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class TaxModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/tax.html'
    PAGE_TITLE = _('Create New Tax')
    form_class = TaxForm
    context_object_name = 'tax'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return TaxForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:tax-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        tax_model: TaxModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        tax_model.entity = entity_model
        tax_model.save()
        return super().form_valid(form)


class TaxModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/tax.html'
    PAGE_TITLE = _('Tax Update')
    context_object_name = 'tax'
    form_class = TaxForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'tax_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return TaxModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:tax-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 