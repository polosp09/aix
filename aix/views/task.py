from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.task import TaskForm
from aix.models.entity import EntityModel
from aix.models.task import TaskModel
from aix.views.mixins import LoginRequiredMixIn


class TaskModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/task.html'
    context_object_name = 'tasks'
    PAGE_TITLE = _('Task List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return TaskModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class TaskModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/task.html'
    PAGE_TITLE = _('Create New Task')
    form_class = TaskForm
    context_object_name = 'task'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return TaskForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:task-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        task_model: TaskModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        task_model.entity = entity_model
        task_model.save()
        return super().form_valid(form)


class TaskModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/task.html'
    PAGE_TITLE = _('Task Update')
    context_object_name = 'task'
    form_class = TaskForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'task_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return TaskModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:task-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 