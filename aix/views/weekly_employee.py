from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.weekly_employee import WeeklyEmployeeForm
from aix.models.entity import EntityModel
from aix.models.weekly_employee import WeeklyEmployeeModel
from aix.views.mixins import LoginRequiredMixIn


class WeeklyEmployeeModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/weekly_employee.html'
    context_object_name = 'weekly_employees'
    PAGE_TITLE = _('WeeklyEmployee List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WeeklyEmployeeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WeeklyEmployeeModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/weekly_employee.html'
    PAGE_TITLE = _('Create New WeeklyEmployee')
    form_class = WeeklyEmployeeForm
    context_object_name = 'weekly_employee'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WeeklyEmployeeForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:weekly-employee-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        weekly_employee_model: WeeklyEmployeeModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        weekly_employee_model.entity = entity_model
        weekly_employee_model.save()
        return super().form_valid(form)


class WeeklyEmployeeModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/weekly_employee.html'
    PAGE_TITLE = _('WeeklyEmployee Update')
    context_object_name = 'weekly_employee'
    form_class = WeeklyEmployeeForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'weekly_employee_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return WeeklyEmployeeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:weekly-employee-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 