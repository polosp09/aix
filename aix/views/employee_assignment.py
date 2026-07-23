from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.employee_assignment import EmployeeAssignmentForm, EmployeeAssignmentAddForm
from aix.models.entity import EntityModel
from aix.models.employee_assignment import EmployeeAssignmentModel
from aix.views.mixins import LoginRequiredMixIn


class EmployeeAssignmentModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/employee_assignment.html'
    context_object_name = 'employee_assignments'
    PAGE_TITLE = _('EmployeeAssignment List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeAssignmentModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EmployeeAssignmentModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/employee_assignment.html'
    PAGE_TITLE = _('Create New EmployeeAssignment')
    form_class = EmployeeAssignmentForm
    context_object_name = 'employee_assignment'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeAssignmentForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:employee-assignment-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        employee_assignment_model: EmployeeAssignmentModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        employee_assignment_model.entity = entity_model
        employee_assignment_model.save()
        return super().form_valid(form)


class EmployeeAssignmentModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/employee_assignment.html'
    PAGE_TITLE = _('EmployeeAssignment Update')
    context_object_name = 'employee_assignment'
    form_class = EmployeeAssignmentForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'employee_assignment_pk'
    slug_field = 'uuid'

    def get_form(self, form_class=None):
        if 'employee_pk' in self.kwargs:
            return EmployeeAssignmentAddForm(**self.get_form_kwargs())
        return EmployeeAssignmentForm(**self.get_form_kwargs())

    def get_queryset(self):
        return EmployeeAssignmentModel.objects.for_entity(
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
        return reverse('aix:employee-assignment-list',
                    kwargs={
                        'entity_slug': self.kwargs['entity_slug']
                    })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class EmployeeAssignmentModelAddView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/employee_assignment.html'
    PAGE_TITLE = _('Create New EmployeeAssignment')
    form_class = EmployeeAssignmentAddForm
    context_object_name = 'employee_assignment'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeAssignmentAddForm.objects.for_entity(
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
        employee_assignment_model: EmployeeAssignmentModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        employee_assignment_model.entity = entity_model
        employee_assignment_model.employee_id = self.kwargs['employee_pk']
        employee_assignment_model.save()
        return super().form_valid(form)