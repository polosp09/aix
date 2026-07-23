from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.document_type import DocumentTypeForm
from aix.models.entity import EntityModel
from aix.models.document_type import DocumentTypeModel
from aix.views.mixins import LoginRequiredMixIn


class DocumentTypeModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/document_type.html'
    context_object_name = 'document_types'
    PAGE_TITLE = _('DocumentType List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return DocumentTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class DocumentTypeModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/document_type.html'
    PAGE_TITLE = _('Create New DocumentType')
    form_class = DocumentTypeForm
    context_object_name = 'document_type'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return DocumentTypeForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:document-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        document_type_model: DocumentTypeModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        document_type_model.entity = entity_model
        document_type_model.save()
        return super().form_valid(form)


class DocumentTypeModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/document_type.html'
    PAGE_TITLE = _('DocumentType Update')
    context_object_name = 'document_type'
    form_class = DocumentTypeForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'document_type_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return DocumentTypeModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:document-type-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 