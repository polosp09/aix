from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.requisition import RequisitionForm
from aix.models.entity import EntityModel
from aix.models.requisition import RequisitionModel
from aix.views.mixins import LoginRequiredMixIn


class RequisitionModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/requisition.html'
    context_object_name = 'requisitions'
    PAGE_TITLE = _('Requisition List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RequisitionModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class RequisitionModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/requisition.html'
    PAGE_TITLE = _('Create New Requisition')
    form_class = RequisitionForm
    context_object_name = 'requisition'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RequisitionForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:requisition-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        requisition_model: RequisitionModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        requisition_model.entity = entity_model
        requisition_model.save()
        return super().form_valid(form)


class RequisitionModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/requisition.html'
    PAGE_TITLE = _('Requisition Update')
    context_object_name = 'requisition'
    form_class = RequisitionForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'requisition_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return RequisitionModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:requisition-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 