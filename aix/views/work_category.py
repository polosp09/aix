
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.work_category import WorkCategoryForm
from aix.models.entity import EntityModel
from aix.models.work_category import WorkCategoryModel
from aix.views.mixins import LoginRequiredMixIn


class WorkCategoryModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/work_category.html'
    context_object_name = 'work_categorys'
    PAGE_TITLE = _('WorkCategory List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkCategoryModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WorkCategoryModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/work_category.html'
    PAGE_TITLE = _('Create New WorkCategory')
    form_class = WorkCategoryForm
    context_object_name = 'work_category'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkCategoryForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-category-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        work_category_model: WorkCategoryModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        work_category_model.entity = entity_model
        work_category_model.save()
        return super().form_valid(form)


class WorkCategoryModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/work_category.html'
    PAGE_TITLE = _('WorkCategory Update')
    context_object_name = 'work_category'
    form_class = WorkCategoryForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'work_category_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return WorkCategoryModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-category-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 