from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.general_notification import GeneralNotificationForm
from aix.models.entity import EntityModel
from aix.models.general_notification import GeneralNotificationModel
from aix.views.mixins import LoginRequiredMixIn


class GeneralNotificationModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/general_notification_list.html'
    context_object_name = 'general_notifications'
    PAGE_TITLE = _('GeneralNotification List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return GeneralNotificationModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class GeneralNotificationModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/general_notification.html'
    PAGE_TITLE = _('Create New GeneralNotification')
    form_class = GeneralNotificationForm
    context_object_name = 'general_notification'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return GeneralNotificationForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:general-notification-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        general_notification_model: GeneralNotificationModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        general_notification_model.entity = entity_model
        general_notification_model.save()
        return super().form_valid(form)


class GeneralNotificationModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/general_notification.html'
    PAGE_TITLE = _('GeneralNotification Update')
    context_object_name = 'general_notification'
    form_class = GeneralNotificationForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'general_notification_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return GeneralNotificationModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:general-notification-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 