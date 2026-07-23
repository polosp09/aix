from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.incoming_document_handler import IncomingDocumentHandlerForm
from aix.models.entity import EntityModel
from aix.models.incoming_document_handler import IncomingDocumentHandlerModel
from aix.views.mixins import LoginRequiredMixIn


class IncomingDocumentHandlerModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/incoming_document_handler.html'
    context_object_name = 'incoming_document_handlers'
    PAGE_TITLE = _('IncomingDocumentHandler List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return IncomingDocumentHandlerModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class IncomingDocumentHandlerModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/incoming_document_handler.html'
    PAGE_TITLE = _('Create New IncomingDocumentHandler')
    form_class = IncomingDocumentHandlerForm
    context_object_name = 'incoming_document_handler'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return IncomingDocumentHandlerForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:incoming-document-handler-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        incoming_document_handler_model: IncomingDocumentHandlerModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        incoming_document_handler_model.entity = entity_model
        incoming_document_handler_model.save()
        return super().form_valid(form)


class IncomingDocumentHandlerModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/incoming_document_handler.html'
    PAGE_TITLE = _('IncomingDocumentHandler Update')
    context_object_name = 'incoming_document_handler'
    form_class = IncomingDocumentHandlerForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'incoming_document_handler_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return IncomingDocumentHandlerModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:incoming-document-handler-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 