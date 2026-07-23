from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from aix.forms.work_order_activity_lifting import WorkOrderActivityLiftingForm, WorkOrderActivityLiftingAddForm
from aix.models import AssetModel
from aix.models.entity import EntityModel
from aix.models.employee import EmployeeModel
from aix.models.work_order_activity_lifting import WorkOrderActivityLiftingModel
from aix.models.work_order_task_asset import WorkOrderTaskAssetModel
from aix.models.work_order_asset import WorkOrderAssetModel
from aix.models.work_order_activity_personnel import WorkOrderActivityPersonnelModel
from aix.views.mixins import LoginRequiredMixIn


class WorkOrderActivityLiftingModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/activities/details/activity_lifting.html'
    context_object_name = 'work_order_activity_liftings'
    PAGE_TITLE = _('WorkOrderActivityLifting List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderActivityLiftingModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WorkOrderActivityLiftingModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/activities/activity_lifting.html'
    PAGE_TITLE = _('Create New WorkOrderActivityLifting')
    form_class = WorkOrderActivityLiftingForm
    context_object_name = 'work_order_activity_lifting'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderActivityLiftingForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-activity-lifting-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        work_order_activity_lifting_model: WorkOrderActivityLiftingModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        work_order_activity_lifting_model.entity = entity_model
        work_order_activity_lifting_model.save()
        return super().form_valid(form)


class WorkOrderActivityLiftingModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/activities/activity_lifting.html'
    PAGE_TITLE = _('WorkOrderActivityLifting Update')
    context_object_name = 'work_order_activity_lifting'
    form_class = WorkOrderActivityLiftingForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'work_order_activity_lifting_pk'
    slug_field = 'uuid'

    def get_form(self, form_class=None):
        if 'work_order_activity_pk' in self.kwargs:
            entity_slug = self.kwargs['entity_slug']
            user_model = self.request.user
            lifting_qs = WorkOrderActivityLiftingModel.objects.for_entity(
                entity_slug=entity_slug,
                user_model=user_model
            )
            wo_lifting_qs = WorkOrderAssetModel.objects.for_entity(
                entity_slug=entity_slug,
                user_model=user_model
            )
            wo_personnel_qs = WorkOrderActivityPersonnelModel.objects.for_entity(
                entity_slug=entity_slug,
                user_model=user_model
            )
            # print(lifting_qs.count(), self.kwargs['work_order_activity_pk'])
            if lifting_qs.count() > 0:
                liftings = lifting_qs
            elif task_lifting_qs.count() > 0:
                liftings = task_lifting_qs
            elif wo_lifting_qs.count() > 0:
                liftings = wo_lifting_qs
            
            lifting_list = AssetModel.objects.filter(uuid__in=liftings.values_list('equipment_id', flat=True))
            staffs = wo_personnel_qs
            staff_list = EmployeeModel.objects.filter(uuid__in=staffs.values_list('employee_id', flat=True))

            return WorkOrderActivityLiftingAddForm(assets=lifting_list, staff=staff_list, **self.get_form_kwargs())
        return WorkOrderActivityLiftingForm(**self.get_form_kwargs())

    def get_queryset(self):
        return WorkOrderActivityLiftingModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        if 'work_order_activity_pk' in self.kwargs:
            return reverse('aix:work-order-activity-details',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'work_order_activity_pk': self.kwargs['work_order_activity_pk']
                        })
        return reverse('aix:work-order-lifting-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class WorkOrderActivityLiftingModelAddView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/activities/activity_lifting.html'
    PAGE_TITLE = _('Create New WorkOrderActivityLifting')
    form_class = WorkOrderActivityLiftingAddForm
    context_object_name = 'work_order_activity_lifting'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderActivityLiftingAddForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_form(self, form_class=None):
        entity_slug = self.kwargs['entity_slug']
        user_model = self.request.user
        lifting_qs = WorkOrderActivityLiftingModel.objects.for_entity(
            entity_slug=entity_slug,
            user_model=user_model
        )
        task_lifting_qs = WorkOrderTaskAssetModel.objects.for_entity(
            entity_slug=entity_slug,
            user_model=user_model
        )
        wo_lifting_qs = WorkOrderAssetModel.objects.for_entity(
            entity_slug=entity_slug,
            user_model=user_model
        )
        wo_personnel_qs = WorkOrderActivityPersonnelModel.objects.for_entity(
            entity_slug=entity_slug,
            user_model=user_model
        )
        # print(lifting_qs.count(), self.kwargs['work_order_activity_pk'])
        if lifting_qs.count() > 0:
            liftings = lifting_qs
        elif task_lifting_qs.count() > 0:
            liftings = task_lifting_qs
        elif wo_lifting_qs.count() > 0:
            liftings = wo_lifting_qs
        print(lifting_qs, task_lifting_qs, wo_lifting_qs)
        lifting_list = AssetModel.objects.filter(uuid__in=liftings.values_list('equipment_id', flat=True))
        # for lifting in liftings:
        #     lifting_list.append(lifting.lifting)
        #     print(lifting.lifting)
        staffs = wo_personnel_qs
        staff_list = EmployeeModel.objects.filter(uuid__in=staffs.values_list('employee_id', flat=True))

        # activity_model = get_object_or_404(WorkOrderActivityLiftingModel, uuid=self.kwargs['work_order_activity_pk'])
        return WorkOrderActivityLiftingAddForm(assets=lifting_list, staff=staff_list, **self.get_form_kwargs())

    def get_success_url(self):
        return reverse('aix:work-order-activity-details',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'work_order_activity_pk': self.kwargs['work_order_activity_pk']
                       })

    def form_valid(self, form):
        work_order_activity_lifting_model: WorkOrderActivityLiftingModel = form.save(commit=False)
        entity_model_qs = EntityModel.objects.filter(slug__exact=self.kwargs['entity_slug'])
        entity_model = get_object_or_404(entity_model_qs)
        # work_order_activity_lifting_model.entity = entity_model.instance,
        work_order_activity_lifting_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
        )
        work_order_activity_lifting_model.activity_id = self.kwargs['work_order_activity_pk']
        work_order_activity_lifting_model.entity_id = entity_model.uuid
        # print(form.cleaned_data['lifting'].lifting.uuid)
        # work_order_activity_lifting_model.lifting_id = form.cleaned_data['lifting'].lifting.uuid
        work_order_activity_lifting_model.save()
        return super().form_valid(form)

class WorkOrderActivityLiftingModelDetailView(LoginRequiredMixIn, DetailView):
    template_name = 'aix/app/operations/activities/details/activity_lifting_details.html'
    context_object_name = 'work_order_activity_lifting'
    PAGE_TITLE = _('WorkOrderActivityLifting Details')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'work_order_activity_lifting_pk'
    slug_field = 'uuid'
    dwn_report_file = False

    def get_queryset(self):
        return WorkOrderActivityLiftingModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )
    def get_success_url(self):
        return reverse('aix:work-order-activity-lifting-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                            'work_order_activity_lifting_pk': self.kwargs['work_order_activity_lifting_pk']
                       })
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['work_order_activity_lifting'] = self.get_object()
        context['entity_slug'] = self.kwargs['entity_slug']

        lifting_qs = WorkOrderActivityLiftingModel.objects.for_activity(
            entity_slug=self.kwargs['entity_slug'],
            work_order_activity=self.get_object().activity
        )
        document_qs = WorkOrderActivityLiftingModel.objects.for_activity(
            entity_slug=self.kwargs['entity_slug'],
            work_order_activity=self.get_object().activity
        )
        personnel_qs = WorkOrderActivityLiftingModel.objects.for_activity(
            entity_slug=self.kwargs['entity_slug'],
            work_order_activity=self.get_object().activity
        )
        context['liftings'] = lifting_qs
        context['documents'] = document_qs
        context['personnels'] = personnel_qs
        return context

    def get(self, request, *args, **kwargs):
        if self.dwn_report_file:
            # Logic to handle downloading the report file
            pass
        return super().get(request, *args, **kwargs)