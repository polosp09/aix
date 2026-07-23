from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.notification_external_type import NotificationExternalTypeForm
from aix.models.entity import EntityModel
from aix.models.notification_external_type import NotificationExternalTypeModel
from aix.views.mixins import LoginRequiredMixIn


class NotificationExternalTypeModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/notification_external_type.html'
    context_object_name = 'notification_external_types'
    PAGE_TITLE = _('NotificationExternalType List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return NotificationExternalTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class NotificationExternalTypeModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/notification_external_type.html'
    PAGE_TITLE = _('Create New NotificationExternalType')
    form_class = NotificationExternalTypeForm
    context_object_name = 'notification_external_type'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return NotificationExternalTypeForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:notification-external-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        notification_external_type_model: NotificationExternalTypeModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        notification_external_type_model.entity = entity_model
        notification_external_type_model.save()
        return super().form_valid(form)


class NotificationExternalTypeModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/notification_external_type.html'
    PAGE_TITLE = _('NotificationExternalType Update')
    context_object_name = 'notification_external_type'
    form_class = NotificationExternalTypeForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'notification_external_type_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return NotificationExternalTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:notification-external-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 