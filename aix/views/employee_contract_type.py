from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.employee_contract_type import EmployeeContractTypeForm
from aix.models.entity import EntityModel
from aix.models.employee_contract_type import EmployeeContractTypeModel
from aix.views.mixins import LoginRequiredMixIn


class EmployeeContractTypeModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/employee_contract_type.html'
    context_object_name = 'employee_contract_types'
    PAGE_TITLE = _('EmployeeContractType List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeContractTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EmployeeContractTypeModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/employee_contract_type.html'
    PAGE_TITLE = _('Create New EmployeeContractType')
    form_class = EmployeeContractTypeForm
    context_object_name = 'employee_contract_type'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeContractTypeForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:employee-contract-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        employee_contract_type_model: EmployeeContractTypeModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        employee_contract_type_model.entity = entity_model
        employee_contract_type_model.save()
        return super().form_valid(form)


class EmployeeContractTypeModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/employee_contract_type.html'
    PAGE_TITLE = _('EmployeeContractType Update')
    context_object_name = 'employee_contract_type'
    form_class = EmployeeContractTypeForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'employee_contract_type_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return EmployeeContractTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:employee-contract-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 