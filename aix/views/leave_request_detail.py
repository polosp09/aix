from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.leave_request_detail import LeaveRequestDetailForm
from aix.models.entity import EntityModel
from aix.models.leave_request_detail import LeaveRequestDetailModel
from aix.views.mixins import LoginRequiredMixIn


class LeaveRequestDetailModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/leave_request_detail.html'
    context_object_name = 'leave_request_details'
    PAGE_TITLE = _('LeaveRequestDetail List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LeaveRequestDetailModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class LeaveRequestDetailModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/leave_request_detail.html'
    PAGE_TITLE = _('Create New LeaveRequestDetail')
    form_class = LeaveRequestDetailForm
    context_object_name = 'leave_request_detail'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LeaveRequestDetailForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:leave-request-detail-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        leave_request_detail_model: LeaveRequestDetailModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        leave_request_detail_model.entity = entity_model
        leave_request_detail_model.save()
        return super().form_valid(form)


class LeaveRequestDetailModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/leave_request_detail.html'
    PAGE_TITLE = _('LeaveRequestDetail Update')
    context_object_name = 'leave_request_detail'
    form_class = LeaveRequestDetailForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'leave_request_detail_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return LeaveRequestDetailModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:leave_request_detail-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 