from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.customer_location import CustomerLocationForm
from aix.models.entity import EntityModel
from aix.models.customer_location import CustomerLocationModel
from aix.views.mixins import LoginRequiredMixIn


class CustomerLocationModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/customer_location.html'
    context_object_name = 'customer_locations'
    PAGE_TITLE = _('Customer Location List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return CustomerLocationModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class CustomerLocationModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/customer_location.html'
    PAGE_TITLE = _('Create New Customer Location')
    form_class = CustomerLocationForm
    context_object_name = 'customer_location'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return CustomerLocationForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:customer-location-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        customer_location_model: CustomerLocationModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        customer_location_model.entity = entity_model
        customer_location_model.save()
        return super().form_valid(form)


class CustomerLocationModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/customer_location.html'
    PAGE_TITLE = _('Customer Location Update')
    context_object_name = 'customer_location'
    form_class = CustomerLocationForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'customer_location_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return CustomerLocationModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:customer-location-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 