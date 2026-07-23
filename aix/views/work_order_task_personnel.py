from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.work_order_task_personnel import WorkOrderTaskPersonnelForm, WorkOrderTaskPersonnelAddForm
from aix.models.entity import EntityModel
from aix.models.work_order_task_personnel import WorkOrderTaskPersonnelModel
from aix.views.mixins import LoginRequiredMixIn


class WorkOrderTaskPersonnelModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/task/details/task_personnel.html'
    context_object_name = 'work_order_task_personnels'
    PAGE_TITLE = _('WorkOrderTaskPersonnel List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderTaskPersonnelModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WorkOrderTaskPersonnelModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/task/task_personnel.html'
    PAGE_TITLE = _('Create New WorkOrderTaskPersonnel')
    form_class = WorkOrderTaskPersonnelForm
    context_object_name = 'work_order_task_personnel'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderTaskPersonnelForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-task-personnel-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        work_order_task_personnel_model: WorkOrderTaskPersonnelModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        work_order_task_personnel_model.entity = entity_model
        work_order_task_personnel_model.task_id = self.kwargs['work_order_task_pk']
        work_order_task_personnel_model.save()
        return super().form_valid(form)


class WorkOrderTaskPersonnelModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/task/task_personnel.html'
    PAGE_TITLE = _('WorkOrderTaskPersonnel Update')
    context_object_name = 'work_order_task_personnel'
    form_class = WorkOrderTaskPersonnelForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'work_order_task_personnel_pk'
    slug_field = 'uuid'

    def get_form(self, form_class=None):
        if 'work_order_task_pk' in self.kwargs:
            return WorkOrderTaskPersonnelAddForm(**self.get_form_kwargs())
        return EmployeeAssignmentForm(**self.get_form_kwargs())

    def get_queryset(self):
        return WorkOrderTaskPersonnelModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        if 'work_order_task_pk' in self.kwargs:
            return reverse('aix:work-order-task-details',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'work_order_task_pk': self.kwargs['work_order_task_pk']
                        })
        return reverse('aix:work-order-task-personnel-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class WorkOrderTaskPersonnelModelAddView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/task/task_personnel.html'
    PAGE_TITLE = _('Create New WorkOrderTaskPersonnel')
    form_class = WorkOrderTaskPersonnelAddForm
    context_object_name = 'work_order_task_personnel'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderTaskPersonnelAddForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-task-details',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'work_order_task_pk': self.kwargs['work_order_task_pk']
                       })

    def form_valid(self, form):
        work_order_task_personnel_model: WorkOrderTaskPersonnelModel = form.save(commit=False)
        entity_model_qs = EntityModel.objects.filter(slug__exact=self.kwargs['entity_slug'])
        entity_model = get_object_or_404(entity_model_qs)
        # work_order_task_personnel_model.entity = entity_model.instance,
        work_order_task_personnel_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
        )
        work_order_task_personnel_model.task_id = self.kwargs['work_order_task_pk']
        work_order_task_personnel_model.entity_id = entity_model.uuid
        work_order_task_personnel_model.save()
        return super().form_valid(form)