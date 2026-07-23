from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.employee_language import EmployeeLanguageForm, EmployeeLanguageAddForm
from aix.models.entity import EntityModel
from aix.models.employee_language import EmployeeLanguageModel
from aix.views.mixins import LoginRequiredMixIn


class EmployeeLanguageModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/employee_language.html'
    context_object_name = 'employee_languages'
    PAGE_TITLE = _('EmployeeLanguage List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeLanguageModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EmployeeLanguageModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/employee_language.html'
    PAGE_TITLE = _('Create New EmployeeLanguage')
    form_class = EmployeeLanguageForm
    context_object_name = 'employee_language'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeLanguageForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:employee-language-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        employee_language_model: EmployeeLanguageModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        employee_language_model.entity = entity_model
        employee_language_model.save()
        return super().form_valid(form)


class EmployeeLanguageModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/employee_language.html'
    PAGE_TITLE = _('EmployeeLanguage Update')
    context_object_name = 'employee_language'
    form_class = EmployeeLanguageForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'employee_language_pk'
    slug_field = 'uuid'

    def get_form(self, form_class=None):
        if 'employee_pk' in self.kwargs:
            return EmployeeLanguageAddForm(**self.get_form_kwargs())
        return EmployeeAssignmentForm(**self.get_form_kwargs())

    def get_queryset(self):
        return EmployeeLanguageModel.objects.for_entity(
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
        return reverse('aix:employee-language-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class EmployeeLanguageModelAddView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/employee_language.html'
    PAGE_TITLE = _('Create New EmployeeLanguage')
    form_class = EmployeeLanguageAddForm
    context_object_name = 'employee_language'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeLanguageAddForm.objects.for_entity(
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
        employee_language_model: EmployeeLanguageModel = form.save(commit=False)
        entity_model_qs = EntityModel.objects.filter(slug__exact=self.kwargs['entity_slug'])
        entity_model = get_object_or_404(entity_model_qs)
        # employee_language_model.entity = entity_model.instance,
        employee_language_model.employee_id = self.kwargs['employee_pk']
        employee_language_model.entity_id = entity_model.uuid
        employee_language_model.save()
        return super().form_valid(form)