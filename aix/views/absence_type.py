from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.absence_type import AbsenceTypeForm
from aix.models.entity import EntityModel
from aix.models.absence_type import AbsenceTypeModel
from aix.views.mixins import LoginRequiredMixIn


class AbsenceTypeModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/absence_type.html'
    context_object_name = 'absence_types'
    PAGE_TITLE = _('AbsenceType List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return AbsenceTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class AbsenceTypeModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/absence_type.html'
    PAGE_TITLE = _('Create New AbsenceType')
    form_class = AbsenceTypeForm
    context_object_name = 'absence_type'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return AbsenceTypeForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:absence-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        absence_type_model: AbsenceTypeModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        absence_type_model.entity = entity_model
        absence_type_model.save()
        return super().form_valid(form)


class AbsenceTypeModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/absence_type.html'
    PAGE_TITLE = _('AbsenceType Update')
    context_object_name = 'absence_type'
    form_class = AbsenceTypeForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'absence_type_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return AbsenceTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:absence-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)