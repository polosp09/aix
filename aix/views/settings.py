from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.models.entity import EntityModel
from aix.views.mixins import LoginRequiredMixIn


class SettingsListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/settings.html'
    context_object_name = 'settings'
    PAGE_TITLE = _('Settings List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EntityModel.objects.for_user(
            user_model=self.request.user
        )



class SettingsModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/settings.html'
    PAGE_TITLE = _('Create New Settings')
    
    context_object_name = 'settings'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    


class SettingsModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/settings.html'
    PAGE_TITLE = _('Settings Update')
    context_object_name = 'settings'
    
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'settings_pk'
    slug_field = 'uuid'

    