from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from aix.forms.work_order_activity_transport import WorkOrderActivityTransportForm, WorkOrderActivityTransportAddForm
from aix.models import AssetModel
from aix.models.entity import EntityModel
from aix.models.employee import EmployeeModel
from aix.models.work_order_activity_personnel import WorkOrderActivityPersonnelModel
from aix.models.work_order_activity_transport import WorkOrderActivityTransportModel
from aix.models.work_order_task_asset import WorkOrderTaskAssetModel
from aix.models.work_order_asset import WorkOrderAssetModel
from aix.views.mixins import LoginRequiredMixIn


class WorkOrderActivityTransportModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/activities/details/activity_transport.html'
    context_object_name = 'work_order_activity_transports'
    PAGE_TITLE = _('WorkOrderActivityTransport List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderActivityTransportModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WorkOrderActivityTransportModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/activities/activity_transport.html'
    PAGE_TITLE = _('Create New WorkOrderActivityTransport')
    form_class = WorkOrderActivityTransportForm
    context_object_name = 'work_order_activity_transport'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderActivityTransportForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-activity-transport-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        work_order_activity_transport_model: WorkOrderActivityTransportModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        work_order_activity_transport_model.entity = entity_model
        work_order_activity_transport_model.save()
        return super().form_valid(form)


class WorkOrderActivityTransportModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/activities/activity_transport.html'
    PAGE_TITLE = _('WorkOrderActivityTransport Update')
    context_object_name = 'work_order_activity_transport'
    form_class = WorkOrderActivityTransportForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'work_order_activity_transport_pk'
    slug_field = 'uuid'

    def get_form(self, form_class=None):
        if 'work_order_activity_pk' in self.kwargs:
            entity_slug = self.kwargs['entity_slug']
            user_model = self.request.user
            transport_qs = WorkOrderActivityTransportModel.objects.for_entity(
                entity_slug=entity_slug,
                user_model=user_model
            )
            wo_transport_qs = WorkOrderAssetModel.objects.for_entity(
                entity_slug=entity_slug,
                user_model=user_model
            )
            # print(transport_qs.count(), self.kwargs['work_order_activity_pk'])
            if transport_qs.count() > 0:
                transports = transport_qs
            elif task_transport_qs.count() > 0:
                transports = task_transport_qs
            elif wo_transport_qs.count() > 0:
                transports = wo_transport_qs
            
            transport_list = AssetModel.objects.filter(uuid__in=transports.values_list('vehicle_id', flat=True))
            return WorkOrderActivityTransportAddForm(transports=transport_list, **self.get_form_kwargs())
        return EmployeeAssignmentForm(**self.get_form_kwargs())

    def get_queryset(self):
        return WorkOrderActivityTransportModel.objects.for_entity(
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
        return reverse('aix:work-order-transport-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class WorkOrderActivityTransportModelAddView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/activities/activity_transport.html'
    PAGE_TITLE = _('Create New WorkOrderActivityTransport')
    form_class = WorkOrderActivityTransportAddForm
    context_object_name = 'work_order_activity_transport'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderActivityTransportAddForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_form(self, form_class=None):
        entity_slug = self.kwargs['entity_slug']
        user_model = self.request.user
        transport_qs = WorkOrderActivityTransportModel.objects.for_entity(
            entity_slug=entity_slug,
            user_model=user_model
        )
        task_transport_qs = WorkOrderTaskAssetModel.objects.for_entity(
            entity_slug=entity_slug,
            user_model=user_model
        )
        wo_transport_qs = WorkOrderAssetModel.objects.for_entity(
            entity_slug=entity_slug,
            user_model=user_model
        )
        wo_personnel_qs = WorkOrderActivityPersonnelModel.objects.for_entity(
            entity_slug=entity_slug,
            user_model=user_model
        )
        # print(transport_qs.count(), self.kwargs['work_order_activity_pk'])
        if transport_qs.count() > 0:
            transports = transport_qs
        elif task_transport_qs.count() > 0:
            transports = task_transport_qs
        elif wo_transport_qs.count() > 0:
            transports = wo_transport_qs

        staffs = wo_personnel_qs
        
        transport_list = AssetModel.objects.filter(uuid__in=transports.values_list('asset_id', flat=True))
        staff_list = EmployeeModel.objects.filter(uuid__in=staffs.values_list('employee_id', flat=True))
        return WorkOrderActivityTransportAddForm(vehicles=transport_list, staff=staff_list, **self.get_form_kwargs())

    def get_success_url(self):
        return reverse('aix:work-order-activity-details',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'work_order_activity_pk': self.kwargs['work_order_activity_pk']
                       })

    def form_valid(self, form):
        work_order_activity_transport_model: WorkOrderActivityTransportModel = form.save(commit=False)
        entity_model_qs = EntityModel.objects.filter(slug__exact=self.kwargs['entity_slug'])
        entity_model = get_object_or_404(entity_model_qs)
        # work_order_activity_transport_model.entity = entity_model.instance,
        work_order_activity_transport_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
        )
        work_order_activity_transport_model.activity_id = self.kwargs['work_order_activity_pk']
        work_order_activity_transport_model.entity_id = entity_model.uuid
        # print(form.cleaned_data['transport'].transport.uuid)
        # work_order_activity_transport_model.transport_id = form.cleaned_data['transport'].transport.uuid
        work_order_activity_transport_model.save()
        return super().form_valid(form)

class WorkOrderActivityTransportModelDetailView(LoginRequiredMixIn, DetailView):
    template_name = 'aix/app/operations/activities/details/activity_transport_details.html'
    context_object_name = 'work_order_activity_transport'
    PAGE_TITLE = _('WorkOrderActivityTransport Details')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'work_order_activity_transport_pk'
    slug_field = 'uuid'
    dwn_report_file = False

    def get_queryset(self):
        return WorkOrderActivityTransportModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )
    def get_success_url(self):
        return reverse('aix:work-order-activity-transport-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                            'work_order_activity_transport_pk': self.kwargs['work_order_activity_transport_pk']
                       })
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['work_order_activity_transport'] = self.get_object()
        context['entity_slug'] = self.kwargs['entity_slug']

        transport_qs = WorkOrderActivityTransportModel.objects.for_activity(
            entity_slug=self.kwargs['entity_slug'],
            work_order_activity=self.get_object().activity
        )
        document_qs = WorkOrderActivityTransportModel.objects.for_activity(
            entity_slug=self.kwargs['entity_slug'],
            work_order_activity=self.get_object().activity
        )
        personnel_qs = WorkOrderActivityTransportModel.objects.for_activity(
            entity_slug=self.kwargs['entity_slug'],
            work_order_activity=self.get_object().activity
        )
        context['transports'] = transport_qs
        context['documents'] = document_qs
        context['personnels'] = personnel_qs
        return context

    def get(self, request, *args, **kwargs):
        if self.dwn_report_file:
            # Logic to handle downloading the report file
            pass
        return super().get(request, *args, **kwargs)