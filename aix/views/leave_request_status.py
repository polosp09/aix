from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.leave_request_status import LeaveRequestStatusForm
from aix.models.entity import EntityModel
from aix.models.leave_request_status import LeaveRequestStatusModel
from aix.views.mixins import LoginRequiredMixIn


class LeaveRequestStatusModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/leave_request_status.html'
    context_object_name = 'leave_request_statuses'
    PAGE_TITLE = _('LeaveRequestStatus List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LeaveRequestStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class LeaveRequestStatusModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/leave_request_status.html'
    PAGE_TITLE = _('Create New LeaveRequestStatus')
    form_class = LeaveRequestStatusForm
    context_object_name = 'leave_request_status'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LeaveRequestStatusForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:leave-request-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        leave_request_status_model: LeaveRequestStatusModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        leave_request_status_model.entity = entity_model
        leave_request_status_model.save()
        return super().form_valid(form)


class LeaveRequestStatusModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/leave_request_status.html'
    PAGE_TITLE = _('LeaveRequestStatus Update')
    context_object_name = 'leave_request_status'
    form_class = LeaveRequestStatusForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'leave_request_status_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return LeaveRequestStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:leave-request-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 