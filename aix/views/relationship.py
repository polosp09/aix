from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.relationship import RelationshipForm
from aix.models.entity import EntityModel
from aix.models.relationship import RelationshipModel
from aix.views.mixins import LoginRequiredMixIn


class RelationshipModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/hr/relationship.html'
    context_object_name = 'relationships'
    PAGE_TITLE = _('Relationship List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RelationshipModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class RelationshipModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/hr/relationship.html'
    PAGE_TITLE = _('Create New Relationship')
    form_class = RelationshipForm
    context_object_name = 'relationship'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RelationshipForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:relationship-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        relationship_model: RelationshipModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        relationship_model.entity = entity_model
        relationship_model.save()
        return super().form_valid(form)


class RelationshipModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/hr/relationship.html'
    PAGE_TITLE = _('Relationship Update')
    context_object_name = 'relationship'
    form_class = RelationshipForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'relationship_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return RelationshipModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:relationship-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 