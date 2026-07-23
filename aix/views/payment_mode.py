from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.payment_mode import PaymentModeForm
from aix.models.entity import EntityModel
from aix.models.payment_mode import PaymentModeModel
from aix.views.mixins import LoginRequiredMixIn


class PaymentModeModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/payment_mode.html'
    context_object_name = 'payment_modes'
    PAGE_TITLE = _('PaymentMode List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return PaymentModeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class PaymentModeModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/payment_mode.html'
    PAGE_TITLE = _('Create New PaymentMode')
    form_class = PaymentModeForm
    context_object_name = 'payment_mode'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return PaymentModeForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:payment-mode-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        payment_mode_model: PaymentModeModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        payment_mode_model.entity = entity_model
        payment_mode_model.save()
        return super().form_valid(form)


class PaymentModeModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/payment_mode.html'
    PAGE_TITLE = _('PaymentMode Update')
    context_object_name = 'payment_mode'
    form_class = PaymentModeForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'payment_mode_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return PaymentModeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:payment-mode-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 