from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.document_status import DocumentStatusForm
from aix.models.entity import EntityModel
from aix.models.document_status import DocumentStatusModel
from aix.views.mixins import LoginRequiredMixIn


class DocumentStatusModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/document_status.html'
    context_object_name = 'document_statuses'
    PAGE_TITLE = _('DocumentStatus List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return DocumentStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class DocumentStatusModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/document_status.html'
    PAGE_TITLE = _('Create New DocumentStatus')
    form_class = DocumentStatusForm
    context_object_name = 'document_status'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return DocumentStatusForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:document-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        document_status_model: DocumentStatusModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        document_status_model.entity = entity_model
        document_status_model.save()
        return super().form_valid(form)


class DocumentStatusModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/document_status.html'
    PAGE_TITLE = _('DocumentStatus Update')
    context_object_name = 'document_status'
    form_class = DocumentStatusForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'document_status_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return DocumentStatusModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:document-status-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 