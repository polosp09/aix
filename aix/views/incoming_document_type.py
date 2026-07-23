from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.incoming_document_type import IncomingDocumentTypeForm
from aix.models.entity import EntityModel
from aix.models.incoming_document_type import IncomingDocumentTypeModel
from aix.views.mixins import LoginRequiredMixIn


class IncomingDocumentTypeModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/incoming_document_type.html'
    context_object_name = 'incoming_document_types'
    PAGE_TITLE = _('IncomingDocumentType List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return IncomingDocumentTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class IncomingDocumentTypeModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/incoming_document_type.html'
    PAGE_TITLE = _('Create New IncomingDocumentType')
    form_class = IncomingDocumentTypeForm
    context_object_name = 'incoming_document_type'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return IncomingDocumentTypeForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:incoming-document-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        incoming_document_type_model: IncomingDocumentTypeModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        incoming_document_type_model.entity = entity_model
        incoming_document_type_model.save()
        return super().form_valid(form)


class IncomingDocumentTypeModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/incoming_document_type.html'
    PAGE_TITLE = _('IncomingDocumentType Update')
    context_object_name = 'incoming_document_type'
    form_class = IncomingDocumentTypeForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'incoming_document_type_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return IncomingDocumentTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:incoming-document-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 