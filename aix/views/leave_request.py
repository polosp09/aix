from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.leave_request import LeaveRequestForm
from aix.models.entity import EntityModel
from aix.models.leave_request import LeaveRequestModel
from aix.views.mixins import LoginRequiredMixIn


class LeaveRequestModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/leave_request.html'
    context_object_name = 'leave_requests'
    PAGE_TITLE = _('LeaveRequest List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LeaveRequestModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class LeaveRequestModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/leave_request.html'
    PAGE_TITLE = _('Create New LeaveRequest')
    form_class = LeaveRequestForm
    context_object_name = 'leave_request'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LeaveRequestForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:leave-request-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        leave_request_model: LeaveRequestModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        leave_request_model.entity = entity_model
        leave_request_model.save()
        return super().form_valid(form)


class LeaveRequestModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/leave_request.html'
    PAGE_TITLE = _('LeaveRequest Update')
    context_object_name = 'leave_request'
    form_class = LeaveRequestForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'leave_request_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return LeaveRequestModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:leave-request-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 