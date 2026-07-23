from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.currency import CurrencyForm
from aix.models.entity import EntityModel
from aix.models.currency import CurrencyModel
from aix.views.mixins import LoginRequiredMixIn


class CurrencyModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/currency.html'
    context_object_name = 'currencys'
    PAGE_TITLE = _('Currency List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return CurrencyModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class CurrencyModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/currency.html'
    PAGE_TITLE = _('Create New Currency')
    form_class = CurrencyForm
    context_object_name = 'currency'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return CurrencyForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:currency-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        currency_model: CurrencyModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        currency_model.entity = entity_model
        currency_model.save()
        return super().form_valid(form)


class CurrencyModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/currency.html'
    PAGE_TITLE = _('Currency Update')
    context_object_name = 'currency'
    form_class = CurrencyForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'currency_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return CurrencyModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:currency-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 