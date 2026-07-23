from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.skill import SkillForm
from aix.models.entity import EntityModel
from aix.models.skill import SkillModel
from aix.views.mixins import LoginRequiredMixIn


class SkillModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/hr/skill.html'
    context_object_name = 'skills'
    PAGE_TITLE = _('Skill List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return SkillModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class SkillModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/hr/skill.html'
    PAGE_TITLE = _('Create New Skill')
    form_class = SkillForm
    context_object_name = 'skill'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return SkillForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:skill-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        skill_model: SkillModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        skill_model.entity = entity_model
        skill_model.save()
        return super().form_valid(form)


class SkillModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/hr/skill.html'
    PAGE_TITLE = _('Skill Update')
    context_object_name = 'skill'
    form_class = SkillForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'skill_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return SkillModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:skill-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 