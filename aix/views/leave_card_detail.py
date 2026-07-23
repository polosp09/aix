from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.leave_card_detail import LeaveCardDetailForm
from aix.models.entity import EntityModel
from aix.models.leave_card_detail import LeaveCardDetailModel
from aix.views.mixins import LoginRequiredMixIn


class LeaveCardDetailModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/leave_card_detail.html'
    context_object_name = 'leave_card_details'
    PAGE_TITLE = _('LeaveCardDetail List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LeaveCardDetailModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class LeaveCardDetailModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/leave_card_detail.html'
    PAGE_TITLE = _('Create New LeaveCardDetail')
    form_class = LeaveCardDetailForm
    context_object_name = 'leave_card_detail'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LeaveCardDetailForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:leave-card-detail-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        leave_card_detail_model: LeaveCardDetailModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        leave_card_detail_model.entity = entity_model
        leave_card_detail_model.save()
        return super().form_valid(form)


class LeaveCardDetailModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/leave_card_detail.html'
    PAGE_TITLE = _('LeaveCardDetail Update')
    context_object_name = 'leave_card_detail'
    form_class = LeaveCardDetailForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'leave_card_detail_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return LeaveCardDetailModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:leave-card-detail-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 