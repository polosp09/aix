from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.currency_rate import CurrencyRateForm
from aix.models.entity import EntityModel
from aix.models.currency_rate import CurrencyRateModel
from aix.views.mixins import LoginRequiredMixIn


class CurrencyRateModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/currency_rate.html'
    context_object_name = 'currency_rates'
    PAGE_TITLE = _('CurrencyRate List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return CurrencyRateModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class CurrencyRateModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/currency_rate.html'
    PAGE_TITLE = _('Create New CurrencyRate')
    form_class = CurrencyRateForm
    context_object_name = 'currency_rate'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return CurrencyRateForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:currency-rate-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        currency_rate_model: CurrencyRateModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        currency_rate_model.entity = entity_model
        currency_rate_model.save()
        return super().form_valid(form)


class CurrencyRateModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/currency_rate.html'
    PAGE_TITLE = _('CurrencyRate Update')
    context_object_name = 'currency_rate'
    form_class = CurrencyRateForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'currency_rate_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return CurrencyRateModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:currency-rate-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 