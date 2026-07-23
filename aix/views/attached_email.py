"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from uuid import uuid4

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from aix.models.mixins import SlugNameMixIn, CreateUpdateMixIn, SlugNameMixIn
from django.db.models import Q

from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.attached_email import AttachedEmailForm
from aix.models.entity import EntityModel
from aix.models.attached_email import AttachedEmailModel
from aix.views.mixins import LoginRequiredMixIn


class AttachedEmailModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/attached_email.html'
    context_object_name = 'attached_emails'
    PAGE_TITLE = _('AttachedEmail List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return AttachedEmailModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class AttachedEmailModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/attached_email.html'
    PAGE_TITLE = _('Create New AttachedEmail')
    form_class = AttachedEmailForm
    context_object_name = 'attached_email'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return AttachedEmailForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:attached-email-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        attached_email_model: AttachedEmailModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        attached_email_model.entity = entity_model
        attached_email_model.save()
        return super().form_valid(form)


class AttachedEmailModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/attached_email.html'
    PAGE_TITLE = _('AttachedEmail Update')
    context_object_name = 'attached_email'
    form_class = AttachedEmailForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'attached_email_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return AttachedEmailModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:attached-email-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 