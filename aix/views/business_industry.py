from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.business_industry import BusinessIndustryForm
from aix.models.entity import EntityModel
from aix.models.business_industry import BusinessIndustryModel
from aix.views.mixins import LoginRequiredMixIn


class BusinessIndustryModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/business_industry.html'
    context_object_name = 'business_industries'
    PAGE_TITLE = _('BusinessIndustry List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return BusinessIndustryModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class BusinessIndustryModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/business_industry.html'
    PAGE_TITLE = _('Create New BusinessIndustry')
    form_class = BusinessIndustryForm
    context_object_name = 'business_industry'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return BusinessIndustryForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:business-industry-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        business_industry_model: BusinessIndustryModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        business_industry_model.entity = entity_model
        business_industry_model.save()
        return super().form_valid(form)


class BusinessIndustryModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/business_industry.html'
    PAGE_TITLE = _('BusinessIndustry Update')
    context_object_name = 'business_industry'
    form_class = BusinessIndustryForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'business_industry_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return BusinessIndustryModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:business-industry-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 