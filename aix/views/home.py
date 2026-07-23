"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from django.urls import reverse
from django.utils.timezone import localtime, localdate
from django.utils.translation import gettext as _
from django.views.generic import RedirectView, ListView

from aix.models.asset import AssetModel
from aix.models.customer import CustomerModel
from aix.models.entity import EntityModel
from aix.models.employee import EmployeeModel
from aix.models.invoice import InvoiceModel
from aix.models.kpipob import KpiPobModel
from aix.models.kpionoff import KpiOnOffModel
from aix.models.kpiops import KpiOpsModel
from aix.models.kpihse import KpiHseModel
from aix.models.user_allocation import UserAllocationModel
from aix.models.work_order_asset import WorkOrderAssetModel
from aix.models.work_order_jobcard import WorkOrderJobcardModel
from aix.models.work_order_personnel import WorkOrderPersonnelModel
from aix.models.work_order_task import WorkOrderTaskModel
from aix.models.work_order_task_asset import WorkOrderTaskAssetModel
from aix.models.work_order_task_personnel import WorkOrderTaskPersonnelModel
from aix.models.work_order import WorkOrderModel
from aix.views.mixins import LoginRequiredMixIn, SessionConfigurationMixIn


class RootUrlView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse('aix:login')
        return reverse('aix:home')


class DasboardView(LoginRequiredMixIn, ListView):
    template_name = 'aix/home.html'
    PAGE_TITLE = _('My Dashboard')
    context_object_name = 'entities'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_subtitle'] = self.request.user.get_full_name()
        context['header_subtitle_icon'] = 'ei:user'
        return context

    def get_queryset(self):
        return EntityModel.objects.for_user(
            user_model=self.request.user
        )


class HRDasboardView(LoginRequiredMixIn, ListView):
    template_name = 'aix/home_staff.html'
    PAGE_TITLE = _('Staff Dashboard')
    context_object_name = 'entities'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_subtitle'] = self.request.user.get_full_name()
        context['header_subtitle_icon'] = 'ei:user'
        return context

    def get_queryset(self):
        return EntityModel.objects.for_user(
            user_model=self.request.user
        ).order_by('-updated')


class StaffDasboardView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/employees/details/employee_details.html'
    PAGE_TITLE = _('Staff Dashboard')
    context_object_name = 'entities'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_subtitle'] = self.request.user.get_full_name()
        context['header_subtitle_icon'] = 'ei:user'
        return context

    def get_queryset(self):
        return EmployeeModel.objects.for_user(
            user_model=self.request.user
        ).order_by('-updated')

class aixDasboardView(LoginRequiredMixIn, ListView):
    template_name = 'aix/home_aix.html'
    PAGE_TITLE = _('aix Dashboard')
    context_object_name = 'entities'
    loc_date = localdate()
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'year': loc_date.year,
        'month': loc_date.month,
        'hide_menu': True,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_subtitle'] = self.request.user.get_full_name()
        context['header_subtitle_icon'] = 'ei:user'
        entity_slug = 'total-energies-uganda-7ssoulyf'
        self.kwargs['entity_slug'] = entity_slug
        # for group in self.request.user.groups.all:
        #     if group.name == 'Admins':
        #         context['usr_group'] = 'Admins'
        #     if group.name == 'TotalProjectManager':
        #         context['usr_group'] = 'TotalProjectManager'
        #     if group.name == 'ProjectManager':
        #         context['usr_group'] = 'ProjectManager'
        #     if group.name == 'Supervisor':
        #         context['usr_group'] = 'Supervisor'
        #     if group.name == 'Clerks':
        #         context['usr_group'] = 'Clerks'
        usr_groups = self.request.user.groups.all()
        context['usr_group'] = usr_groups
        context['usr_groups'] = usr_groups
        self.kwargs['usr_group'] = context['usr_group']

        customer_model: CustomerModel = 'f9246d4b44c440169ea3ac8e979129e0'
        wo_qs = WorkOrderModel.objects.for_customer(
                entity_slug=entity_slug,
                customer=customer_model
            )
        context['work_orders'] = wo_qs

        allocation_qs = UserAllocationModel.objects.for_allocation(
                entity_slug=entity_slug,
                allocation=self.request.user
            )
        
        if allocation_qs.count:
            is_wo = allocation_qs.exclude(work_order=None)
            is_task = allocation_qs.exclude(task=None)
            if is_wo:
                context['wo_router'] = 1
                context['wos'] = is_wo
                for wo in is_wo:
                    context['wo_value'] = wo.work_order.uuid
                    context['wo_number'] = wo.work_order.order_no
            if is_task:
                context['task_router'] = 1
                context['tasks'] = is_task
                for tsk in is_task:
                    context['task_value'] = tsk.task.uuid
                    context['task_number'] = tsk.task.tripno
                # asset_qs = AssetModel.objects.for_entity(
                #         entity_slug=entity_slug,
                #         user_model=self.request.user
                #     )
                # context['assets'] = asset_qs
                
                # wo_task_qs = WorkOrderTaskModel.objects.for_entity(
                #         entity_slug=entity_slug,
                #         user_model=self.request.user,
                #     )
                # context['wo_tasks'] = wo_task_qs.count
                # wo_task_asset_qs = WorkOrderTaskAssetModel.objects.for_entity(
                #         entity_slug=entity_slug,
                #         user_model=self.request.user
                #     )
                # context['task_assets'] = asset_qs.count
                # wo_task_personnel_qs = WorkOrderTaskPersonnelModel.objects.for_entity(
                #         entity_slug=entity_slug,
                #         user_model=self.request.user
                #     )
                # context['task_personnel'] = wo_task_personnel_qs.count
                # wo_asset_qs = WorkOrderAssetModel.objects.for_entity(
                #         entity_slug=entity_slug,
                #         user_model=self.request.user
                #     )
                # context['wo_assets'] = wo_asset_qs.count
                # wo_personnel_qs = WorkOrderPersonnelModel.objects.for_entity(
                #         entity_slug=entity_slug,
                #         user_model=self.request.user
                #     )
                # context['wo_personnel'] = wo_personnel_qs.count
                # invoice_qs = InvoiceModel.objects.for_entity(
                #         entity_slug=entity_slug,
                #         user_model=self.request.user
                #     )
                # context['invoices'] = invoice_qs.count
                # jcd_qs = WorkOrderJobcardModel.objects.for_entity(
                #         entity_slug=entity_slug,
                #         user_model=self.request.user
                #     )
                # context['jcds'] = jcd_qs.count
                # wo_qs = jcd_qs.select_related('work_order')        
                # kpi_pob_qs = KpiPobModel.objects.for_entity(
                #         entity_slug=entity_slug,
                #         user_model=self.request.user,
                #     )
                # context['kpi_pobs'] = kpi_pob_qs.count
                # kpi_onoff_qs = KpiOnOffModel.objects.for_entity(
                #         entity_slug=entity_slug,
                #         user_model=self.request.user,
                #     )
                # context['kpi_onoffs'] = kpi_onoff_qs.count
                # kpi_ops_qs = KpiOpsModel.objects.for_entity(
                #         entity_slug=entity_slug,
                #         user_model=self.request.user
                #     )
                # context['kpi_ops'] = kpi_ops_qs.count
                # kpi_hse_qs = KpiHseModel.objects.for_entity(
                #         entity_slug=entity_slug,
                #         user_model=self.request.user
                #     )
                # context['kpi_hses'] = kpi_hse_qs.count

        else:
            wo_qs = WorkOrderModel.objects.for_customer(
                    entity_slug=entity_slug,
                    customer=customer_model
                )
            context['work_orders'] = wo_qs
            asset_qs = AssetModel.objects.for_entity(
                    entity_slug=entity_slug,
                    user_model=self.request.user
                )
            context['assets'] = asset_qs
            
            wo_task_qs = WorkOrderTaskModel.objects.for_entity(
                    entity_slug=entity_slug,
                    user_model=self.request.user,
                )
            context['wo_tasks'] = wo_task_qs.count
            wo_task_asset_qs = WorkOrderTaskAssetModel.objects.for_entity(
                    entity_slug=entity_slug,
                    user_model=self.request.user
                )
            context['task_assets'] = asset_qs.count
            wo_task_personnel_qs = WorkOrderTaskPersonnelModel.objects.for_entity(
                    entity_slug=entity_slug,
                    user_model=self.request.user
                )
            context['task_personnel'] = wo_task_personnel_qs.count
            wo_asset_qs = WorkOrderAssetModel.objects.for_entity(
                    entity_slug=entity_slug,
                    user_model=self.request.user
                )
            context['wo_assets'] = wo_asset_qs.count
            wo_personnel_qs = WorkOrderPersonnelModel.objects.for_entity(
                    entity_slug=entity_slug,
                    user_model=self.request.user
                )
            context['wo_personnel'] = wo_personnel_qs.count
            invoice_qs = InvoiceModel.objects.for_entity(
                    entity_slug=entity_slug,
                    user_model=self.request.user
                )
            context['invoices'] = invoice_qs.count
            jcd_qs = WorkOrderJobcardModel.objects.for_entity(
                    entity_slug=entity_slug,
                    user_model=self.request.user
                )
            context['jcds'] = jcd_qs.count
            wo_qs = jcd_qs.select_related('work_order')        
            kpi_pob_qs = KpiPobModel.objects.for_entity(
                    entity_slug=entity_slug,
                    user_model=self.request.user,
                )
            context['kpi_pobs'] = kpi_pob_qs.count
            kpi_onoff_qs = KpiOnOffModel.objects.for_entity(
                    entity_slug=entity_slug,
                    user_model=self.request.user,
                )
            context['kpi_onoffs'] = kpi_onoff_qs.count
            kpi_ops_qs = KpiOpsModel.objects.for_entity(
                    entity_slug=entity_slug,
                    user_model=self.request.user
                )
            context['kpi_ops'] = kpi_ops_qs.count
            kpi_hse_qs = KpiHseModel.objects.for_entity(
                    entity_slug=entity_slug,
                    user_model=self.request.user
                )
            context['kpi_hses'] = kpi_hse_qs.count
            # context['entity_slug'] = entity_slug

        return context

    def get_queryset(self):
        return EntityModel.objects.for_user(
            user_model=self.request.user
        ).order_by('-updated')


