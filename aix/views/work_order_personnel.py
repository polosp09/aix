from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from aix.forms.work_order_personnel import WorkOrderPersonnelForm, WorkOrderPersonnelAddForm
from aix.models.entity import EntityModel
from aix.models.work_order_personnel import WorkOrderPersonnelModel
from aix.views.mixins import LoginRequiredMixIn


class WorkOrderPersonnelModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/work-order-personnel.html'
    context_object_name = 'work_order_personnels'
    PAGE_TITLE = _('WorkOrderPersonnel List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderPersonnelModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WorkOrderPersonnelModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/work_order_personnel.html'
    PAGE_TITLE = _('Create New WorkOrderPersonnel')
    form_class = WorkOrderPersonnelForm
    context_object_name = 'work_order_personnel'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderPersonnelForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-personnel-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        work_order_personnel_model: WorkOrderPersonnelModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        work_order_personnel_model.entity = entity_model
        work_order_personnel_model.save()
        return super().form_valid(form)


class WorkOrderPersonnelModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/work_order_personnel.html'
    PAGE_TITLE = _('WorkOrderPersonnel Update')
    context_object_name = 'work_order_personnel'
    form_class = WorkOrderPersonnelForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'work_order_personnel_pk'
    slug_field = 'uuid'

    def get_form(self, form_class=None):
        if 'work_order_pk' in self.kwargs:
            return WorkOrderPersonnelAddForm(**self.get_form_kwargs())
        return EmployeeAssignmentForm(**self.get_form_kwargs())

    def get_queryset(self):
        return WorkOrderPersonnelModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        if 'work_order_pk' in self.kwargs:
            return reverse('aix:work-order-details',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'work_order_pk': self.kwargs['work_order_pk']
                        })
        return reverse('aix:work-order-personnel-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class WorkOrderPersonnelModelAddView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/work_order_personnel.html'
    PAGE_TITLE = _('Create New WorkOrderPersonnel')
    form_class = WorkOrderPersonnelAddForm
    context_object_name = 'work_order_personnel'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderPersonnelAddForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-details',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'work_order_pk': self.kwargs['work_order_pk']
                       })

    def form_valid(self, form):
        work_order_personnel_model: WorkOrderPersonnelModel = form.save(commit=False)
        entity_model_qs = EntityModel.objects.filter(slug__exact=self.kwargs['entity_slug'])
        entity_model = get_object_or_404(entity_model_qs)
        # work_order_personnel_model.entity = entity_model.instance,
        work_order_personnel_model.work_order_id = self.kwargs['work_order_pk']
        work_order_personnel_model.entity_id = entity_model.uuid
        work_order_personnel_model.save()
        return super().form_valid(form)



class WorkOrderPersonnelModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'work_order_personnel_pk'
    slug_field = 'uuid'
    context_object_name = 'work_order_personnel'
    #template_name = 'aix/advanced/work_order/work_order_detail.html'
    template_name = 'aix/app/operations/details/wo_personnel_detail.html'
    extra_context = {
        'hide_menu': True
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        wo_personnel_model: WorkOrderPersonnelModel = self.object
        title = f'Personnel {wo_personnel_model.code}'
        context['page_title'] = title
        context['header_title'] = title

        wo_personnel_forms = {}
        context['wo_personnel_forms'] = wo_personnel_forms
        
        return context

    def get_queryset(self):
        return WorkOrderPersonnelModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )