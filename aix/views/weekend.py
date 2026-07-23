from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.weekend import WeekendForm
from aix.models.entity import EntityModel
from aix.models.weekend import WeekendModel
from aix.views.mixins import LoginRequiredMixIn


class WeekendModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/weekend.html'
    context_object_name = 'weekends'
    PAGE_TITLE = _('Weekend List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WeekendModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WeekendModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/weekend.html'
    PAGE_TITLE = _('Create New Weekend')
    form_class = WeekendForm
    context_object_name = 'weekend'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WeekendForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:weekend-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        weekend_model: WeekendModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        weekend_model.entity = entity_model
        weekend_model.save()
        return super().form_valid(form)


class WeekendModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/weekend.html'
    PAGE_TITLE = _('Weekend Update')
    context_object_name = 'weekend'
    form_class = WeekendForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'weekend_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return WeekendModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:weekend-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 