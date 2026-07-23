from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.education import EducationForm
from aix.models.entity import EntityModel
from aix.models.education import EducationModel
from aix.views.mixins import LoginRequiredMixIn


class EducationModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/hr/education.html'
    context_object_name = 'educations'
    PAGE_TITLE = _('Education List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EducationModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EducationModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/hr/education.html'
    PAGE_TITLE = _('Create New Education')
    form_class = EducationForm
    context_object_name = 'education'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EducationForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:education-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        education_model: EducationModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        education_model.entity = entity_model
        education_model.save()
        return super().form_valid(form)


class EducationModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/hr/education.html'
    PAGE_TITLE = _('Education Update')
    context_object_name = 'education'
    form_class = EducationForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'education_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return EducationModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:education-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 