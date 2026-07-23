from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.benefit_type import BenefitTypeForm
from aix.models.entity import EntityModel
from aix.models.benefit_type import BenefitTypeModel
from aix.views.mixins import LoginRequiredMixIn


class BenefitTypeModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/benefit_type.html'
    context_object_name = 'benefit_types'
    PAGE_TITLE = _('BenefitType List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return BenefitTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class BenefitTypeModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/benefit_type.html'
    PAGE_TITLE = _('Create New BenefitType')
    form_class = BenefitTypeForm
    context_object_name = 'benefit_type'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return BenefitTypeForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:benefit-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        benefit_type_model: BenefitTypeModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        benefit_type_model.entity = entity_model
        benefit_type_model.save()
        return super().form_valid(form)


class BenefitTypeModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/benefit_type.html'
    PAGE_TITLE = _('BenefitType Update')
    context_object_name = 'benefit_type'
    form_class = BenefitTypeForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'benefit_type_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return BenefitTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:benefit-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 