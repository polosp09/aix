from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.incoming_document import IncomingDocumentForm
from aix.models.entity import EntityModel
from aix.models.incoming_document import IncomingDocumentModel
from aix.views.mixins import LoginRequiredMixIn


class IncomingDocumentModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/incoming_document.html'
    context_object_name = 'incoming_documents'
    PAGE_TITLE = _('IncomingDocument List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return IncomingDocumentModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class IncomingDocumentModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/incoming_document.html'
    PAGE_TITLE = _('Create New IncomingDocument')
    form_class = IncomingDocumentForm
    context_object_name = 'incoming_document'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return IncomingDocumentForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:incoming-document-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        incoming_document_model: IncomingDocumentModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        incoming_document_model.entity = entity_model
        incoming_document_model.save()
        return super().form_valid(form)


class IncomingDocumentModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/incoming_document.html'
    PAGE_TITLE = _('IncomingDocument Update')
    context_object_name = 'incoming_document'
    form_class = IncomingDocumentForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'incoming_document_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return IncomingDocumentModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:incoming-document-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 