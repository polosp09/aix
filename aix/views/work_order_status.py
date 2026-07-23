
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.work_order_status import WorkOrderStatusForm
from aix.models.entity import EntityModel
from aix.models.work_order_status import WorkOrderStatusModel
from aix.views.mixins import LoginRequiredMixIn


class WorkOrderStatusModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/work_order_status.html'
    context_object_name = 'work_order_statuses'
    PAGE_TITLE = _('WorkOrderStatus List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WorkOrderStatusModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/work_order_status.html'
    PAGE_TITLE = _('Create New WorkOrderStatus')
    form_class = WorkOrderStatusForm
    context_object_name = 'work_order_status'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderStatusForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        work_order_status_model: WorkOrderStatusModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        work_order_status_model.entity = entity_model
        work_order_status_model.save()
        return super().form_valid(form)


class WorkOrderStatusModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/work_order_status.html'
    PAGE_TITLE = _('WorkOrderStatus Update')
    context_object_name = 'work_order_status'
    form_class = WorkOrderStatusForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'work_order_status_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return WorkOrderStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 