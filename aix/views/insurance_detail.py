from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.insurance_detail import InsuranceDetailForm
from aix.models.entity import EntityModel
from aix.models.insurance_detail import InsuranceDetailModel
from aix.views.mixins import LoginRequiredMixIn


class InsuranceDetailModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/insurance_detail.html'
    context_object_name = 'insurance_details'
    PAGE_TITLE = _('InsuranceDetail List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return InsuranceDetailModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class InsuranceDetailModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/insurance_detail.html'
    PAGE_TITLE = _('Create New InsuranceDetail')
    form_class = InsuranceDetailForm
    context_object_name = 'insurance_detail'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return InsuranceDetailForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:insurance-detail-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        insurance_detail_model: InsuranceDetailModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        insurance_detail_model.entity = entity_model
        insurance_detail_model.save()
        return super().form_valid(form)


class InsuranceDetailModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/insurance_detail.html'
    PAGE_TITLE = _('InsuranceDetail Update')
    context_object_name = 'insurance_detail'
    form_class = InsuranceDetailForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'insurance_detail_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return InsuranceDetailModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:insurance-detail-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 