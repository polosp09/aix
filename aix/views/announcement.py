from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.announcement import AnnouncementForm
from aix.models.entity import EntityModel
from aix.models.announcement import AnnouncementModel
from aix.views.mixins import LoginRequiredMixIn


class AnnouncementModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/announcement.html'
    context_object_name = 'announcements'
    PAGE_TITLE = _('Announcement List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return AnnouncementModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class AnnouncementModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/announcement.html'
    PAGE_TITLE = _('Create New Announcement')
    form_class = AnnouncementForm
    context_object_name = 'announcement'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return AnnouncementForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:announcement-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        announcement_model: AnnouncementModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        announcement_model.entity = entity_model
        announcement_model.save()
        return super().form_valid(form)


class AnnouncementModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/announcement.html'
    PAGE_TITLE = _('Announcement Update')
    context_object_name = 'announcement'
    form_class = AnnouncementForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'announcement_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return AnnouncementModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:announcement-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 