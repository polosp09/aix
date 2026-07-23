
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.immigration_detail import ImmigrationDetailForm
from aix.models.entity import EntityModel
from aix.models.immigration_detail import ImmigrationDetailModel
from aix.views.mixins import LoginRequiredMixIn


class ImmigrationDetailModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/immigration_detail.html'
    context_object_name = 'immigration_details'
    PAGE_TITLE = _('ImmigrationDetail List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return ImmigrationDetailModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class ImmigrationDetailModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/immigration_detail.html'
    PAGE_TITLE = _('Create New ImmigrationDetail')
    form_class = ImmigrationDetailForm
    context_object_name = 'immigration_detail'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return ImmigrationDetailForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:immigration-detail-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        immigration_detail_model: ImmigrationDetailModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        immigration_detail_model.entity = entity_model
        immigration_detail_model.save()
        return super().form_valid(form)


class ImmigrationDetailModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/immigration_detail.html'
    PAGE_TITLE = _('ImmigrationDetail Update')
    context_object_name = 'immigration_detail'
    form_class = ImmigrationDetailForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'immigration_detail_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return ImmigrationDetailModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:immigration-detail-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 