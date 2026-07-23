from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.nation import NationForm
from aix.models.entity import EntityModel
from aix.models.nation import NationModel
from aix.views.mixins import LoginRequiredMixIn


class NationModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/nation.html'
    context_object_name = 'nations'
    PAGE_TITLE = _('Nation List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return NationModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class NationModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/nation.html'
    PAGE_TITLE = _('Create New Nation')
    form_class = NationForm
    context_object_name = 'nation'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return NationForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:nation-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        nation_model: NationModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        nation_model.entity = entity_model
        nation_model.save()
        return super().form_valid(form)


class NationModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/nation.html'
    PAGE_TITLE = _('Nation Update')
    context_object_name = 'nation'
    form_class = NationForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'nation_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return NationModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:nation-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 