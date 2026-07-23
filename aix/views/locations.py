from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.locations import LocationForm
from aix.models.entity import EntityModel
from aix.models.locations import LocationModel
from aix.views.mixins import LoginRequiredMixIn


class LocationModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/location.html'
    context_object_name = 'locations'
    PAGE_TITLE = _('Location List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LocationModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class LocationModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/location.html'
    PAGE_TITLE = _('Create New Location')
    form_class = LocationForm
    context_object_name = 'location'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LocationForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:location-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        location_model: LocationModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        location_model.entity = entity_model
        location_model.save()
        return super().form_valid(form)


class LocationModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/location.html'
    PAGE_TITLE = _('Location Update')
    context_object_name = 'location'
    form_class = LocationForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'location_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return LocationModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:location-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 