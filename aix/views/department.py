
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.department import DepartmentForm
from aix.models.entity import EntityModel
from aix.models.department import DepartmentModel
from aix.views.mixins import LoginRequiredMixIn


class DepartmentModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/hr/department.html'
    context_object_name = 'departments'
    PAGE_TITLE = _('Department List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return DepartmentModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class DepartmentModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/hr/department.html'
    PAGE_TITLE = _('Create New Department')
    form_class = DepartmentForm
    context_object_name = 'department'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return DepartmentForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:department-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        department_model: DepartmentModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        department_model.entity = entity_model
        department_model.save()
        return super().form_valid(form)


class DepartmentModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/hr/department.html'
    PAGE_TITLE = _('Department Update')
    context_object_name = 'department'
    form_class = DepartmentForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'department_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return DepartmentModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:department-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 