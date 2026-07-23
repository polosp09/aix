
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.notification import NotificationForm
from aix.models.entity import EntityModel
from aix.models.notification import NotificationModel
from aix.views.mixins import LoginRequiredMixIn


class NotificationModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/notification.html'
    context_object_name = 'notifications'
    PAGE_TITLE = _('Notification List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return NotificationModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class NotificationModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/notification.html'
    PAGE_TITLE = _('Create New Notification')
    form_class = NotificationForm
    context_object_name = 'notification'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return NotificationForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:notification-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        notification_model: NotificationModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        notification_model.entity = entity_model
        notification_model.save()
        return super().form_valid(form)


class NotificationModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/notification.html'
    PAGE_TITLE = _('Notification Update')
    context_object_name = 'notification'
    form_class = NotificationForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'notification_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return NotificationModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:notification-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 