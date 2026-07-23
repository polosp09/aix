from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.marital_status import MaritalStatusForm
from aix.models.entity import EntityModel
from aix.models.marital_status import MaritalStatusModel
from aix.views.mixins import LoginRequiredMixIn


class MaritalStatusModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/marital_status.html'
    context_object_name = 'marital_statuses'
    PAGE_TITLE = _('MaritalStatus List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return MaritalStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class MaritalStatusModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/marital_status.html'
    PAGE_TITLE = _('Create New MaritalStatus')
    form_class = MaritalStatusForm
    context_object_name = 'marital_status'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return MaritalStatusForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:marital-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        marital_status_model: MaritalStatusModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        marital_status_model.entity = entity_model
        marital_status_model.save()
        return super().form_valid(form)


class MaritalStatusModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/marital_status.html'
    PAGE_TITLE = _('MaritalStatus Update')
    context_object_name = 'marital_status'
    form_class = MaritalStatusForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'marital_status_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return MaritalStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:marital-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 