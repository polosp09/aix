from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.benefit import BenefitForm
from aix.models.entity import EntityModel
from aix.models.benefit import BenefitModel
from aix.views.mixins import LoginRequiredMixIn


class BenefitModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/benefit.html'
    context_object_name = 'benefits'
    PAGE_TITLE = _('Benefit List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return BenefitModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class BenefitModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/benefit.html'
    PAGE_TITLE = _('Create New Benefit')
    form_class = BenefitForm
    context_object_name = 'benefit'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return BenefitForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:benefit-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        benefit_model: BenefitModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        benefit_model.entity = entity_model
        benefit_model.save()
        return super().form_valid(form)


class BenefitModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/benefit.html'
    PAGE_TITLE = _('Benefit Update')
    context_object_name = 'benefit'
    form_class = BenefitForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'benefit_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return BenefitModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:benefit-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 