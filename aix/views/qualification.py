from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.qualification import QualificationForm
from aix.models.entity import EntityModel
from aix.models.qualification import QualificationModel
from aix.views.mixins import LoginRequiredMixIn


class QualificationModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/hr/qualification.html'
    context_object_name = 'qualifications'
    PAGE_TITLE = _('Qualification List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return QualificationModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class QualificationModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/hr/qualification.html'
    PAGE_TITLE = _('Create New Qualification')
    form_class = QualificationForm
    context_object_name = 'qualification'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return QualificationForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:qualification-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        qualification_model: QualificationModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        qualification_model.entity = entity_model
        qualification_model.save()
        return super().form_valid(form)


class QualificationModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/hr/qualification.html'
    PAGE_TITLE = _('Qualification Update')
    context_object_name = 'qualification'
    form_class = QualificationForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'qualification_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return QualificationModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:qualification-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 