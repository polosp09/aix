from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.task_assignee import TaskAssigneeForm
from aix.models.entity import EntityModel
from aix.models.task_assignee import TaskAssigneeModel
from aix.views.mixins import LoginRequiredMixIn


class TaskAssigneeModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/task_assignee.html'
    context_object_name = 'task_assignees'
    PAGE_TITLE = _('TaskAssignee List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return TaskAssigneeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class TaskAssigneeModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/task_assignee.html'
    PAGE_TITLE = _('Create New TaskAssignee')
    form_class = TaskAssigneeForm
    context_object_name = 'task_assignee'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return TaskAssigneeForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:task-assignee-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        task_assignee_model: TaskAssigneeModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        task_assignee_model.entity = entity_model
        task_assignee_model.save()
        return super().form_valid(form)


class TaskAssigneeModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/task_assignee.html'
    PAGE_TITLE = _('TaskAssignee Update')
    context_object_name = 'task_assignee'
    form_class = TaskAssigneeForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'task_assignee_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return TaskAssigneeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:task-assignee-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 