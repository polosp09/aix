from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.absence_date import AbsenceDateForm
from aix.models.entity import EntityModel
from aix.models.absence_date import AbsenceDateModel
from aix.views.mixins import LoginRequiredMixIn


class AbsenceDateModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/absence_date.html'
    context_object_name = 'absence_dates'
    PAGE_TITLE = _('AbsenceDate List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return AbsenceDateModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class AbsenceDateModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/absence_date.html'
    PAGE_TITLE = _('Create New AbsenceDate')
    form_class = AbsenceDateForm
    context_object_name = 'absence_date'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return AbsenceDateForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:absence-date-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        absence_date_model: AbsenceDateModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        absence_date_model.entity = entity_model
        absence_date_model.save()
        return super().form_valid(form)


class AbsenceDateModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/absence_date.html'
    PAGE_TITLE = _('AbsenceDate Update')
    context_object_name = 'absence_date'
    form_class = AbsenceDateForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'absence_date_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return AbsenceDateModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:absence-date-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)