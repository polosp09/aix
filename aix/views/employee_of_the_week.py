from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.employee_of_the_week import EmployeeOfTheWeekForm
from aix.models.entity import EntityModel
from aix.models.employee_of_the_week import EmployeeOfTheWeekModel
from aix.views.mixins import LoginRequiredMixIn


class EmployeeOfTheWeekModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/employee_of_the_week.html'
    context_object_name = 'employee_of_the_weeks'
    PAGE_TITLE = _('EmployeeOfTheWeek List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeOfTheWeekModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EmployeeOfTheWeekModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/employee_of_the_week.html'
    PAGE_TITLE = _('Create New EmployeeOfTheWeek')
    form_class = EmployeeOfTheWeekForm
    context_object_name = 'employee_of_the_week'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeOfTheWeekForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:employee-of-the-week-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        employee_of_the_week_model: EmployeeOfTheWeekModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        employee_of_the_week_model.entity = entity_model
        employee_of_the_week_model.save()
        return super().form_valid(form)


class EmployeeOfTheWeekModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/employee_of_the_week.html'
    PAGE_TITLE = _('EmployeeOfTheWeek Update')
    context_object_name = 'employee_of_the_week'
    form_class = EmployeeOfTheWeekForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'employee_of_the_week_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return EmployeeOfTheWeekModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:employee-of-the-week-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 