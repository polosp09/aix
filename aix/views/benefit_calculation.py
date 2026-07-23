from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.benefit_calculation import BenefitCalculationForm
from aix.models.entity import EntityModel
from aix.models.benefit_calculation import BenefitCalculationModel
from aix.views.mixins import LoginRequiredMixIn


class BenefitCalculationModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/benefit_calculation.html'
    context_object_name = 'benefit_calculations'
    PAGE_TITLE = _('BenefitCalculation List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return BenefitCalculationModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class BenefitCalculationModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/benefit_calculation.html'
    PAGE_TITLE = _('Create New BenefitCalculation')
    form_class = BenefitCalculationForm
    context_object_name = 'benefit_calculation'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return BenefitCalculationForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:benefit-calculation-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        benefit_calculation_model: BenefitCalculationModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        benefit_calculation_model.entity = entity_model
        benefit_calculation_model.save()
        return super().form_valid(form)


class BenefitCalculationModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/benefit_calculation.html'
    PAGE_TITLE = _('BenefitCalculation Update')
    context_object_name = 'benefit_calculation'
    form_class = BenefitCalculationForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'benefit_calculation_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return BenefitCalculationModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:benefit-calculation-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 