
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.work_order_jobcard_status import WorkOrderJobcardStatusForm
from aix.models.entity import EntityModel
from aix.models.work_order_jobcard_status import WorkOrderJobcardStatusModel
from aix.views.mixins import LoginRequiredMixIn


class WorkOrderJobcardStatusModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/work_order_jobcard_status.html'
    context_object_name = 'work_order_jobcard_statuses'
    PAGE_TITLE = _('WorkOrderJobcardStatus List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderJobcardStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WorkOrderJobcardStatusModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/work_order_jobcard_status.html'
    PAGE_TITLE = _('Create New WorkOrderJobcardStatus')
    form_class = WorkOrderJobcardStatusForm
    context_object_name = 'work_order_jobcard_status'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderJobcardStatusForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-jobcard-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        work_order_jobcard_status_model: WorkOrderJobcardStatusModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        work_order_jobcard_status_model.entity = entity_model
        work_order_jobcard_status_model.save()
        return super().form_valid(form)


class WorkOrderJobcardStatusModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/work_order_jobcard_status.html'
    PAGE_TITLE = _('WorkOrderJobcardStatus Update')
    context_object_name = 'work_order_jobcard_status'
    form_class = WorkOrderJobcardStatusForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'work_order_jobcard_status_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return WorkOrderJobcardStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-jobcard-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 