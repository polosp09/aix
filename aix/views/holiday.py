from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.holiday import HolidayForm
from aix.models.entity import EntityModel
from aix.models.holiday import HolidayModel
from aix.views.mixins import LoginRequiredMixIn


class HolidayModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/holiday.html'
    context_object_name = 'holidays'
    PAGE_TITLE = _('Holiday List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return HolidayModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class HolidayModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/holiday.html'
    PAGE_TITLE = _('Create New Holiday')
    form_class = HolidayForm
    context_object_name = 'holiday'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return HolidayForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:holiday-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        holiday_model: HolidayModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        holiday_model.entity = entity_model
        holiday_model.save()
        return super().form_valid(form)


class HolidayModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/holiday.html'
    PAGE_TITLE = _('Holiday Update')
    context_object_name = 'holiday'
    form_class = HolidayForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'holiday_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return HolidayModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:holiday-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 