from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from aix.forms.work_order_activity_personnel import WorkOrderActivityPersonnelForm, WorkOrderActivityPersonnelAddForm
from aix.models.entity import EntityModel
from aix.models.work_order_activity_personnel import WorkOrderActivityPersonnelModel
from aix.views.mixins import LoginRequiredMixIn


class WorkOrderActivityPersonnelModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/activities/details/activity_personnel.html'
    context_object_name = 'work_order_activity_personnels'
    PAGE_TITLE = _('WorkOrderActivityPersonnel List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderActivityPersonnelModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WorkOrderActivityPersonnelModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/activities/activity_personnel.html'
    PAGE_TITLE = _('Create New WorkOrderActivityPersonnel')
    form_class = WorkOrderActivityPersonnelForm
    context_object_name = 'work_order_activity_personnel'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderActivityPersonnelForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-activity-personnel-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        work_order_activity_personnel_model: WorkOrderActivityPersonnelModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        work_order_activity_personnel_model.entity = entity_model
        work_order_activity_personnel_model.activity_id = self.kwargs['work_order_activity_pk']
        work_order_activity_personnel_model.save()
        return super().form_valid(form)


class WorkOrderActivityPersonnelModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/activities/activity_personnel.html'
    PAGE_TITLE = _('WorkOrderActivityPersonnel Update')
    context_object_name = 'work_order_activity_personnel'
    form_class = WorkOrderActivityPersonnelForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'work_order_activity_personnel_pk'
    slug_field = 'uuid'

    def get_form(self, form_class=None):
        if 'work_order_activity_pk' in self.kwargs:
            return WorkOrderActivityPersonnelAddForm(**self.get_form_kwargs())
        return EmployeeAssignmentForm(**self.get_form_kwargs())

    def get_queryset(self):
        return WorkOrderActivityPersonnelModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        if 'work_order_activity_pk' in self.kwargs:
            return reverse('aix:work-order-activity-details',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'work_order_activity_pk': self.kwargs['work_order_activity_pk']
                        })
        return reverse('aix:work-order-activity-personnel-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class WorkOrderActivityPersonnelModelAddView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/activities/activity_personnel.html'
    PAGE_TITLE = _('Create New WorkOrderActivityPersonnel')
    form_class = WorkOrderActivityPersonnelAddForm
    context_object_name = 'work_order_activity_personnel'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderActivityPersonnelAddForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-activity-details',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'work_order_activity_pk': self.kwargs['work_order_activity_pk']
                       })

    def form_valid(self, form):
        work_order_activity_personnel_model: WorkOrderActivityPersonnelModel = form.save(commit=False)
        entity_model_qs = EntityModel.objects.filter(slug__exact=self.kwargs['entity_slug'])
        entity_model = get_object_or_404(entity_model_qs)
        # work_order_activity_personnel_model.entity = entity_model.instance,
        work_order_activity_personnel_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
        )
        work_order_activity_personnel_model.activity_id = self.kwargs['work_order_activity_pk']
        work_order_activity_personnel_model.entity_id = entity_model.uuid
        work_order_activity_personnel_model.save()
        return super().form_valid(form)

class WorkOrderActivityPersonnelModelDetailView(LoginRequiredMixIn, DetailView):
    template_name = 'aix/app/operations/activities/details/activity_personnel_details.html'
    context_object_name = 'work_order_activity_personnel'
    PAGE_TITLE = _('WorkOrderActivityPersonnel Details')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'work_order_activity_personnel_pk'
    slug_field = 'uuid'
    dwn_report_file = False

    def get_queryset(self):
        return WorkOrderActivityPersonnelModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data here if needed
        return context

    def get_success_url(self):
        return reverse('aix:work-order-activity-personnel-details',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                            'work_order_activity_personnel_pk': self.kwargs['work_order_activity_personnel_pk']
                       })
    def get(self, request, *args, **kwargs):
        if self.dwn_report_file:
            # Logic to handle downloading the report file
            pass
        return super().get(request, *args, **kwargs)