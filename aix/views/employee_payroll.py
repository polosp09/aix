from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.employee_payroll import EmployeePayrollForm, EmployeePayrollAddForm
from aix.models.entity import EntityModel
from aix.models.employee_payroll import EmployeePayrollModel
from aix.views.mixins import LoginRequiredMixIn


class EmployeePayrollModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/employee_payroll.html'
    context_object_name = 'employee_payrolls'
    PAGE_TITLE = _('EmployeePayroll List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeePayrollModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EmployeePayrollModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/employee_payroll.html'
    PAGE_TITLE = _('Create New EmployeePayroll')
    form_class = EmployeePayrollForm
    context_object_name = 'employee_payroll'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeePayrollForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:employee-payroll-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        employee_payroll_model: EmployeePayrollModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        employee_payroll_model.entity = entity_model
        employee_payroll_model.save()
        return super().form_valid(form)


class EmployeePayrollModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/employee_payroll.html'
    PAGE_TITLE = _('EmployeePayroll Update')
    context_object_name = 'employee_payroll'
    form_class = EmployeePayrollForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'employee_payroll_pk'
    slug_field = 'uuid'

    def get_form(self, form_class=None):
        if 'employee_pk' in self.kwargs:
            return EmployeePayrollAddForm(**self.get_form_kwargs())
        return EmployeePayrollForm(**self.get_form_kwargs())

    def get_queryset(self):
        return EmployeePayrollModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        if 'employee_pk' in self.kwargs:
            return reverse('aix:employee-details',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'employee_pk': self.kwargs['employee_pk']
                        })
        return reverse('aix:employee-ayroll-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class EmployeePayrollModelAddView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/employee_payroll.html'
    PAGE_TITLE = _('Create New EmployeePayroll')
    form_class = EmployeePayrollAddForm
    context_object_name = 'employee_payroll'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeePayrollAddForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:employee-details',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'employee_pk': self.kwargs['employee_pk']
                       })

    def form_valid(self, form):
        employee_payroll_model: EmployeePayrollModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        employee_payroll_model.entity = entity_model
        employee_payroll_model.employee_id = self.kwargs['employee_pk']
        employee_payroll_model.save()
        return super().form_valid(form)