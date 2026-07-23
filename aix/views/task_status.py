from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.task_status import TaskStatusForm
from aix.models.entity import EntityModel
from aix.models.task_status import TaskStatusModel
from aix.views.mixins import LoginRequiredMixIn


class TaskStatusModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/task_status.html'
    context_object_name = 'task_statuses'
    PAGE_TITLE = _('TaskStatus List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return TaskStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class TaskStatusModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/task_status.html'
    PAGE_TITLE = _('Create New TaskStatus')
    form_class = TaskStatusForm
    context_object_name = 'task_status'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return TaskStatusForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:task-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        task_status_model: TaskStatusModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        task_status_model.entity = entity_model
        task_status_model.save()
        return super().form_valid(form)


class TaskStatusModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/task_status.html'
    PAGE_TITLE = _('TaskStatus Update')
    context_object_name = 'task_status'
    form_class = TaskStatusForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'task_status_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return TaskStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:task-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 