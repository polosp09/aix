from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from aix.forms.requisition_category import RequisitionCategoryForm
from aix.models.entity import EntityModel
from aix.models.requisition_category import RequisitionCategoryModel
from aix.views.mixins import LoginRequiredMixIn


class RequisitionCategoryModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/accounts/requisition_category.html'
    context_object_name = 'requisition_categorys'
    PAGE_TITLE = _('RequisitionCategory List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RequisitionCategoryModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class RequisitionCategoryModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/accounts/requisition_category.html'
    PAGE_TITLE = _('Create New RequisitionCategory')
    form_class = RequisitionCategoryForm
    context_object_name = 'requisition_category'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RequisitionCategoryForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:requisition-category-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        requisition_category_model: RequisitionCategoryModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        requisition_category_model.entity = entity_model
        requisition_category_model.save()
        return super().form_valid(form)


class RequisitionCategoryModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/accounts/requisition_category.html'
    PAGE_TITLE = _('RequisitionCategory Update')
    context_object_name = 'requisition_category'
    form_class = RequisitionCategoryForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'requisition_category_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return RequisitionCategoryModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:requisition-category-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 