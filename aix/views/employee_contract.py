from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.employee_contract import EmployeeContractForm, EmployeeContractAddForm
from aix.models.entity import EntityModel
from aix.models.employee_contract import EmployeeContractModel
from aix.views.mixins import LoginRequiredMixIn


class EmployeeContractModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/employee_contract.html'
    context_object_name = 'employee_contracts'
    PAGE_TITLE = _('EmployeeContract List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeContractModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EmployeeContractModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/employee_contract.html'
    PAGE_TITLE = _('Create New EmployeeContract')
    form_class = EmployeeContractForm
    context_object_name = 'employee_contract'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeContractForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:employee-contract-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        employee_contract_model: EmployeeContractModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        employee_contract_model.entity = entity_model
        employee_contract_model.save()
        return super().form_valid(form)


class EmployeeContractModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/employee_contract.html'
    PAGE_TITLE = _('EmployeeContract Update')
    context_object_name = 'employee_contract'
    form_class = EmployeeContractForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'employee_contract_pk'
    slug_field = 'uuid'

    def get_form(self, form_class=None):
        if 'employee_pk' in self.kwargs:
            return EmployeeContractAddForm(**self.get_form_kwargs())
        return EmployeeContractForm(**self.get_form_kwargs())

    def get_queryset(self):
        return EmployeeContractModel.objects.for_entity(
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
        return reverse('aix:employee-contract-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class EmployeeContractModelAddView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/employee_contract.html'
    PAGE_TITLE = _('Create New EmployeeContract')
    form_class = EmployeeContractAddForm
    context_object_name = 'employee_contract'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeContractAddForm.objects.for_entity(
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
        employee_contract_model: EmployeeContractModel = form.save(commit=False)
        entity_model = EntityModel.objects.get(slug__exact=self.kwargs['entity_slug'])
        employee_contract_model.entity = entity_model
        employee_contract_model.employee_id = self.kwargs['employee_pk']
        employee_contract_model.save()
        return super().form_valid(form)