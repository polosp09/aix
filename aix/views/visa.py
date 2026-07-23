from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.visa import VisaForm
from aix.models.entity import EntityModel
from aix.models.visa import VisaModel
from aix.views.mixins import LoginRequiredMixIn


class VisaModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/visa.html'
    context_object_name = 'visas'
    PAGE_TITLE = _('Visa List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return VisaModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class VisaModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/employees/visa.html'
    PAGE_TITLE = _('Create New Visa')
    form_class = VisaForm
    context_object_name = 'visa'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return VisaForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:visa-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        visa_model: VisaModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        visa_model.entity = entity_model
        visa_model.save()
        return super().form_valid(form)


class VisaModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/employees/visa.html'
    PAGE_TITLE = _('Visa Update')
    context_object_name = 'visa'
    form_class = VisaForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'visa_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return VisaModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:visa-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 