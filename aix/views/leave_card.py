from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.leave_card import LeaveCardForm, LeaveCardAddForm
from aix.models.entity import EntityModel
from aix.models.leave_card import LeaveCardModel
from aix.views.mixins import LoginRequiredMixIn


class LeaveCardModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/leave_card.html'
    context_object_name = 'leave_cards'
    PAGE_TITLE = _('LeaveCard List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LeaveCardModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class LeaveCardModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/leave_card.html'
    PAGE_TITLE = _('Create New LeaveCard')
    form_class = LeaveCardForm
    context_object_name = 'leave_card'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LeaveCardForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:leave-card-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        leave_card_model: LeaveCardModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        leave_card_model.entity = entity_model
        leave_card_model.save()
        return super().form_valid(form)


class LeaveCardModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/leave_card.html'
    PAGE_TITLE = _('LeaveCard Update')
    context_object_name = 'leave_card'
    form_class = LeaveCardForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'leave_card_pk'
    slug_field = 'uuid'

    def get_form(self, form_class=None):
        if 'employee_pk' in self.kwargs:
            return LeaveCardAddForm(**self.get_form_kwargs())
        return LeaveCardForm(**self.get_form_kwargs())

    def get_queryset(self):
        return LeaveCardModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        if 'employee_pk' in self.kwargs:
            return reverse('aix:employee-details',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'employee_pk': self.kwargs['employee_pk']
                        })
        return reverse('aix:leave-card-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class LeaveCardModelAddView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/leave_card.html'
    PAGE_TITLE = _('Create New LeaveCard')
    form_class = LeaveCardAddForm
    context_object_name = 'leave_card'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return LeaveCardAddForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:employee-details',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                            'employee_pk': self.kwargs['employee_pk']
                       })

    def form_valid(self, form):
        leave_card_model: LeaveCardModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        leave_card_model.entity = entity_model
        leave_card_model.employee_id = self.kwargs['employee_pk']
        leave_card_model.save()
        return super().form_valid(form)
