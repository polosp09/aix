from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.dependant import DependantForm
from aix.models.entity import EntityModel
from aix.models.dependant import DependantModel
from aix.views.mixins import LoginRequiredMixIn


class DependantModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/dependant.html'
    context_object_name = 'dependants'
    PAGE_TITLE = _('Dependant List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return DependantModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class DependantModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/dependant.html'
    PAGE_TITLE = _('Create New Dependant')
    form_class = DependantForm
    context_object_name = 'dependant'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return DependantForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:dependant-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        dependant_model: DependantModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        dependant_model.entity = entity_model
        dependant_model.save()
        return super().form_valid(form)


class DependantModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/dependant.html'
    PAGE_TITLE = _('Dependant Update')
    context_object_name = 'dependant'
    form_class = DependantForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'dependant_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return DependantModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:dependant-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 