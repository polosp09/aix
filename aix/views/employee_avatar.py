from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.employee_avatar import EmployeeAvatarForm
from aix.models.entity import EntityModel
from aix.models.employee_avatar import EmployeeAvatarModel
from aix.views.mixins import LoginRequiredMixIn


class EmployeeAvatarModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/employee_avatar.html'
    context_object_name = 'employee_avatars'
    PAGE_TITLE = _('EmployeeAvatar List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeAvatarModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EmployeeAvatarModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/employee_avatar.html'
    PAGE_TITLE = _('Create New EmployeeAvatar')
    form_class = EmployeeAvatarForm
    context_object_name = 'employee_avatar'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EmployeeAvatarForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:employee-avatar-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        employee_avatar_model: EmployeeAvatarModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        employee_avatar_model.entity = entity_model
        employee_avatar_model.save()
        return super().form_valid(form)


class EmployeeAvatarModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/employee_avatar.html'
    PAGE_TITLE = _('EmployeeAvatar Update')
    context_object_name = 'employee_avatar'
    form_class = EmployeeAvatarForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'employee_avatar_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return EmployeeAvatarModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:employee-avatar-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 