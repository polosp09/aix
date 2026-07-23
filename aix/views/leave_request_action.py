from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.leave_request_action import LeaveRequestActionForm
from aix.models.entity import EntityModel
from aix.models.leave_request_action import LeaveRequestActionModel
from aix.views.mixins import LoginRequiredMixIn


class LeaveRequestActionModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/leave_request_action.html'
    context_object_name = 'leave_request_actions'
    PAGE_TITLE = _('LeaveRequestAction List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LeaveRequestActionModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class LeaveRequestActionModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/leave_request_action.html'
    PAGE_TITLE = _('Create New LeaveRequestAction')
    form_class = LeaveRequestActionForm
    context_object_name = 'leave_request_action'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LeaveRequestActionForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:leave-request-action-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        leave_request_action_model: LeaveRequestActionModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        leave_request_action_model.entity = entity_model
        leave_request_action_model.save()
        return super().form_valid(form)


class LeaveRequestActionModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/leave_request_action.html'
    PAGE_TITLE = _('LeaveRequestAction Update')
    context_object_name = 'leave_request_action'
    form_class = LeaveRequestActionForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'leave_request_action_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return LeaveRequestActionModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:leave-request-action-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 