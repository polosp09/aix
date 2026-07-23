from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from aix.forms.work_order_activity_document import WorkOrderActivityDocumentForm, WorkOrderActivityDocumentAddForm
from aix.models.entity import EntityModel
from aix.models.work_order_activity_document import WorkOrderActivityDocumentModel
from aix.views.mixins import LoginRequiredMixIn


class WorkOrderActivityDocumentModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/activities/details/activity_document.html'
    context_object_name = 'work_order_activity_documents'
    PAGE_TITLE = _('WorkOrderActivityDocument List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderActivityDocumentModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WorkOrderActivityDocumentModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/activities/activity_document.html'
    PAGE_TITLE = _('Create New WorkOrderActivityDocument')
    form_class = WorkOrderActivityDocumentForm
    context_object_name = 'work_order_activity_document'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderActivityDocumentForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-activity-document-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        work_order_activity_document_model: WorkOrderActivityDocumentModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        work_order_activity_document_model.entity = entity_model
        work_order_activity_document_model.save()
        return super().form_valid(form)


class WorkOrderActivityDocumentModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/activities/activity_document.html'
    PAGE_TITLE = _('WorkOrderActivityDocument Update')
    context_object_name = 'work_order_activity_document'
    form_class = WorkOrderActivityDocumentForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'work_order_activity_document_pk'
    slug_field = 'uuid'

    def get_form(self, form_class=None):
        if 'work_order_activity_pk' in self.kwargs:
            return WorkOrderActivityDocumentAddForm(**self.get_form_kwargs())
        return EmployeeAssignmentForm(**self.get_form_kwargs())

    def get_queryset(self):
        return WorkOrderActivityDocumentModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        if 'work_order_activity_pk' in self.kwargs:
            return reverse('aix:work-order-activity-details',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'work_order_activity_pk': self.kwargs['work_order_activity_pk']
                        })
        return reverse('aix:work-order-document-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class WorkOrderActivityDocumentModelAddView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/activities/activity_document.html'
    PAGE_TITLE = _('Create New WorkOrderActivityDocument')
    form_class = WorkOrderActivityDocumentAddForm
    context_object_name = 'work_order_activity_document'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderActivityDocumentAddForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-activity-details',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'work_order_activity_pk': self.kwargs['work_order_activity_pk']
                       })

    def form_valid(self, form):
        work_order_activity_document_model: WorkOrderActivityDocumentModel = form.save(commit=False)
        entity_model_qs = EntityModel.objects.filter(slug__exact=self.kwargs['entity_slug'])
        entity_model = get_object_or_404(entity_model_qs)
        # work_order_activity_document_model.entity = entity_model.instance,
        work_order_activity_document_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
        )
        work_order_activity_document_model.activity_id = self.kwargs['work_order_activity_pk']
        work_order_activity_document_model.entity_id = entity_model.uuid
        work_order_activity_document_model.save()
        return super().form_valid(form)

class WorkOrderActivityDocumentModelDetailView(LoginRequiredMixIn, DetailView):
    template_name = 'aix/app/operations/activities/activity_document_details.html'
    context_object_name = 'work_order_activity_document'
    PAGE_TITLE = _('WorkOrderActivityDocument Details')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'work_order_activity_document_pk'
    slug_field = 'uuid'
    dwn_report_file = False

    def get_queryset(self):
        return WorkOrderActivityDocumentModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        document_qs = self.object.document_set.all()
        context['documents'] = document_qs
        return context
    def get_success_url(self):
        if 'work_order_activity_pk' in self.kwargs:
            return reverse('aix:work-order-activity-details',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'work_order_activity_pk': self.kwargs['work_order_activity_pk']
                        })
    def get(self, request, *args, **kwargs):
        if self.dwn_report_file:
            # Logic to handle downloading the report file
            pass
        return super().get(request, *args, **kwargs)