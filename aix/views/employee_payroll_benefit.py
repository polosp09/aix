from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.employee_payroll_benefit import EmployeePayrollBenefitForm
from aix.models.entity import EntityModel
from aix.models.employee_payroll_benefit import EmployeePayrollBenefitModel
from aix.views.mixins import LoginRequiredMixIn


class EmployeePayrollBenefitModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/employee_payroll_benefit.html'
    context_object_name = 'employee_payroll_benefits'
    PAGE_TITLE = _('EmployeePayrollBenefit List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeePayrollBenefitModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EmployeePayrollBenefitModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/employee_payroll_benefit.html'
    PAGE_TITLE = _('Create New EmployeePayrollBenefit')
    form_class = EmployeePayrollBenefitForm
    context_object_name = 'employee_payroll_benefit'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeePayrollBenefitForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:employee-payroll-benefit-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        employee_payroll_benefit_model: EmployeePayrollBenefitModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        employee_payroll_benefit_model.entity = entity_model
        employee_payroll_benefit_model.save()
        return super().form_valid(form)


class EmployeePayrollBenefitModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/employee_payroll_benefit.html'
    PAGE_TITLE = _('EmployeePayrollBenefit Update')
    context_object_name = 'employee_payroll_benefit'
    form_class = EmployeePayrollBenefitForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'employee_payroll_benefit_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return EmployeePayrollBenefitModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:employee-payroll-benefit-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 