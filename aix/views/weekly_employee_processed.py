from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.weekly_employee_processed import WeeklyEmployeeProcessedForm
from aix.models.entity import EntityModel
from aix.models.weekly_employee_processed import WeeklyEmployeeProcessedModel
from aix.views.mixins import LoginRequiredMixIn


class WeeklyEmployeeProcessedModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/weekly_employee_processed.html'
    context_object_name = 'weekly_employee_processeds'
    PAGE_TITLE = _('WeeklyEmployeeProcessed List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WeeklyEmployeeProcessedModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WeeklyEmployeeProcessedModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/weekly_employee_processed.html'
    PAGE_TITLE = _('Create New WeeklyEmployeeProcessed')
    form_class = WeeklyEmployeeProcessedForm
    context_object_name = 'weekly_employee_processed'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WeeklyEmployeeProcessedForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:weekly-employee-processed-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        weekly_employee_processed_model: WeeklyEmployeeProcessedModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        weekly_employee_processed_model.entity = entity_model
        weekly_employee_processed_model.save()
        return super().form_valid(form)


class WeeklyEmployeeProcessedModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/weekly_employee_processed.html'
    PAGE_TITLE = _('WeeklyEmployeeProcessed Update')
    context_object_name = 'weekly_employee_processed'
    form_class = WeeklyEmployeeProcessedForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'weekly_employee_processed_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return WeeklyEmployeeProcessedModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:weekly-employee-processed-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 