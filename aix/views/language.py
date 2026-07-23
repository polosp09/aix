from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.language import LanguageForm
from aix.models.entity import EntityModel
from aix.models.language import LanguageModel
from aix.views.mixins import LoginRequiredMixIn


class LanguageModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/language.html'
    context_object_name = 'languages'
    PAGE_TITLE = _('Language List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LanguageModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class LanguageModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/language.html'
    PAGE_TITLE = _('Create New Language')
    form_class = LanguageForm
    context_object_name = 'language'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LanguageForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:language-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        language_model: LanguageModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        language_model.entity = entity_model
        language_model.save()
        return super().form_valid(form)


class LanguageModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/language.html'
    PAGE_TITLE = _('Language Update')
    context_object_name = 'language'
    form_class = LanguageForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'language_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return LanguageModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:language-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 