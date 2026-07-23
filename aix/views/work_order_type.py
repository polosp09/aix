
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.work_order_type import WorkOrderTypeForm
from aix.models.entity import EntityModel
from aix.models.work_order_type import WorkOrderTypeModel
from aix.views.mixins import LoginRequiredMixIn


class WorkOrderTypeModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/work_order_type.html'
    context_object_name = 'work_order_types'
    PAGE_TITLE = _('WorkOrderType List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WorkOrderTypeModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/work_order_type.html'
    PAGE_TITLE = _('Create New WorkOrderType')
    form_class = WorkOrderTypeForm
    context_object_name = 'work_order_type'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderTypeForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        work_order_type_model: WorkOrderTypeModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        work_order_type_model.entity = entity_model
        work_order_type_model.save()
        return super().form_valid(form)


class WorkOrderTypeModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/work_order_type.html'
    PAGE_TITLE = _('WorkOrderType Update')
    context_object_name = 'work_order_type'
    form_class = WorkOrderTypeForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'work_order_type_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return WorkOrderTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 