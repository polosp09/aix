from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.leave_card_carried_over import LeaveCardCarriedOverForm
from aix.models.entity import EntityModel
from aix.models.leave_card_carried_over import LeaveCardCarriedOverModel
from aix.views.mixins import LoginRequiredMixIn


class LeaveCardCarriedOverModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/leave_card_carried_over.html'
    context_object_name = 'leave_card_carried_overs'
    PAGE_TITLE = _('LeaveCardCarriedOver List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LeaveCardCarriedOverModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class LeaveCardCarriedOverModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/leave_card_carried_over.html'
    PAGE_TITLE = _('Create New LeaveCardCarriedOver')
    form_class = LeaveCardCarriedOverForm
    context_object_name = 'leave_card_carried_over'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LeaveCardCarriedOverForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:leave-card-carried-over-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        leave_card_carried_over_model: LeaveCardCarriedOverModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        leave_card_carried_over_model.entity = entity_model
        leave_card_carried_over_model.save()
        return super().form_valid(form)


class LeaveCardCarriedOverModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/leave_card_carried_over.html'
    PAGE_TITLE = _('LeaveCardCarriedOver Update')
    context_object_name = 'leave_card_carried_over'
    form_class = LeaveCardCarriedOverForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'leave_card_carried_over_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return LeaveCardCarriedOverModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:leave-card-carried-over-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 