from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.employee_license_detail import EmployeeLicenseDetailForm, EmployeeLicenseDetailAddForm
from aix.models.entity import EntityModel
from aix.models.employee_license_detail import EmployeeLicenseDetailModel
from aix.views.mixins import LoginRequiredMixIn


class EmployeeLicenseDetailModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/employee_license_detail.html'
    context_object_name = 'employee_license_details'
    PAGE_TITLE = _('EmployeeLicenseDetail List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeLicenseDetailModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EmployeeLicenseDetailModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/employee_license_detail.html'
    PAGE_TITLE = _('Create New EmployeeLicenseDetail')
    form_class = EmployeeLicenseDetailForm
    context_object_name = 'employee_license_detail'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeLicenseDetailForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:employee-license-detail-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        employee_license_detail_model: EmployeeLicenseDetailModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        employee_license_detail_model.entity = entity_model
        employee_license_detail_model.save()
        return super().form_valid(form)


class EmployeeLicenseDetailModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/employee_license_detail.html'
    PAGE_TITLE = _('EmployeeLicenseDetail Update')
    context_object_name = 'employee_license_detail'
    form_class = EmployeeLicenseDetailForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'employee_license_detail_pk'
    slug_field = 'uuid'

    def get_form(self, form_class=None):
        if 'employee_pk' in self.kwargs:
            return EmployeeLicenseDetailAddForm(**self.get_form_kwargs())
        return EmployeeLicenseDetailForm(**self.get_form_kwargs())

    def get_queryset(self):
        return EmployeeLicenseDetailModel.objects.for_entity(
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
        return reverse('aix:employee-license-detail-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class EmployeeLicenseDetailModelAddView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/employee_license_detail.html'
    PAGE_TITLE = _('Create New EmployeeLicenseDetail')
    form_class = EmployeeLicenseDetailAddForm
    context_object_name = 'employee_license_detail'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeLicenseDetailAddForm.objects.for_entity(
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
        employee_license_detail_model: EmployeeLicenseDetailModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        employee_license_detail_model.entity = entity_model
        employee_license_detail_model.employee_id = self.kwargs['employee_pk']
        employee_license_detail_model.save()
        return super().form_valid(form)