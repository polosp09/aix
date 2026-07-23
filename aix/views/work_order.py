
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView, RedirectView
from django.views.generic.detail import SingleObjectMixin
from django.db.models import Q, Count, Sum

from aix.forms.document import DocumentForm
from aix.forms.work_order import WorkOrderForm
from aix.models.customer import CustomerModel
from aix.models.document import DocumentModel
from aix.models.entity import EntityModel
from aix.models.equipment import EquipmentModel
from aix.models.invoice import InvoiceModel
from aix.models.work_order import WorkOrderModel
from aix.models.work_order_asset import WorkOrderAssetModel
from aix.models.work_order_jobcard import WorkOrderJobcardModel
from aix.models.work_order_personnel import WorkOrderPersonnelModel
from aix.models.work_order_task import WorkOrderTaskModel
from aix.models.work_order_task_asset import WorkOrderTaskAssetModel
from aix.models.work_order_task_personnel import WorkOrderTaskPersonnelModel
from aix.models.kpipob import KpiPobModel
from aix.models.kpionoff import KpiOnOffModel
from aix.models.kpiops import KpiOpsModel
from aix.models.kpihse import KpiHseModel
from aix.views.mixins import LoginRequiredMixIn

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
from xhtml2pdf import pisa

import pandas as pd
from jinja2 import Environment, FileSystemLoader


class WorkOrderModelDashboardView(LoginRequiredMixIn, ListView):
    # template_name = 'aix/app/operations/work_order.html'
    template_name = 'aix/app/dashboards/work_order.html'
    context_object_name = 'work_orders'
    PAGE_TITLE = _('WorkOrder List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        customer_qs = CustomerModel.objects.all()
        user_id = self.request.user.id
        # user_id = 'f9246d4b44c440169ea3ac8e979129e0'
        # print(user_id)
        # customer_model: CustomerModel = get_object_or_404(customer_qs, uuid__exact=user_id)
        # customer_model: CustomerModel = get_object_or_404(customer_qs, user__id=user_id)
        customer_model: CustomerModel = customer_qs.filter().first()
        title = f'Customer {customer_model.customer_name}'
        context['page_title'] = title
        context['header_title'] = title

        invoice_qs = InvoiceModel.objects.for_entity_owed(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                customer=customer_model
            ).select_related('ledger__entity')
        
        inv_amt_invoiced = self.get_total_invoiced(invoice_qs)
        inv_amt_paid = self.get_total_paid(invoice_qs)

        context['is_advanced'] = True
        context['invoices'] = self.get_incoice_list(customer_model)
        context['total_invoiced'] = inv_amt_invoiced
        context['total_paid'] = inv_amt_paid
        context['total_owed'] = self.get_total_owed(inv_amt_invoiced, inv_amt_paid)
        context['total_paid_invoices'] = self.get_total_no_invoices(invoice_qs, 'cleared')
        context['total_owed_invoices'] = self.get_total_no_invoices(invoice_qs, 'pending')
        
        wo_task_qs = WorkOrderTaskModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        wo_task_asset_qs = WorkOrderTaskAssetModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        wo_task_personnel_qs = WorkOrderTaskPersonnelModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        wo_asset_qs = WorkOrderAssetModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        wo_personnel_qs = WorkOrderPersonnelModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        invoice_qs = InvoiceModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        jcd_qs = WorkOrderJobcardModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        wo_qs = jcd_qs.select_related('work_order')        
        kpi_pob_qs = KpiPobModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        kpi_onoff_qs = KpiOnOffModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        kpi_ops_qs = KpiOpsModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        kpi_hse_qs = KpiHseModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        
        agg_pob = KpiPobModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )

        ops_qs = kpi_ops_qs.select_related('task__work_order')
        
        hse_digest = {}
        hse_digest['fat'] = kpi_hse_qs.aggregate(Sum('fat'))
        hse_digest['lti'] = kpi_hse_qs.aggregate(Sum('lti'))
        hse_digest['rwdc'] = kpi_hse_qs.aggregate(Sum('rwdc'))
        hse_digest['mtc'] = kpi_hse_qs.aggregate(Sum('mtc'))
        hse_digest['fac'] = kpi_hse_qs.aggregate(Sum('fac'))
        hse_digest['hipo'] = kpi_hse_qs.aggregate(Sum('hipo'))
        hse_digest['envdam'] = kpi_hse_qs.aggregate(Sum('envdam'))
        hse_digest['nmi'] = kpi_hse_qs.aggregate(Sum('nmi'))
        hse_digest['matloss'] = kpi_hse_qs.aggregate(Sum('matloss'))
        hse_digest['ptw'] = kpi_hse_qs.aggregate(Sum('ptw'))
        hse_digest['tbt'] = kpi_hse_qs.aggregate(Sum('tbt'))
        hse_digest['hht'] = kpi_hse_qs.aggregate(Sum('hht'))
        hse_digest['drills'] = kpi_hse_qs.aggregate(Sum('drills'))
        hse_digest['audit'] = kpi_hse_qs.aggregate(Sum('audit'))
        hse_digest['reporting_cards'] = kpi_hse_qs.aggregate(Sum('reporting_cards'))
        hse_digest['safety_initiative'] = kpi_hse_qs.aggregate(Sum('safety_initiative'))
        context['hse_digest'] = hse_digest
        
        ops_digest = {}
        ops_digest['hrs_ops'] = ops_qs.filter(trip_code="OPS-TR").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_rep'] = ops_qs.filter(trip_code="OPS-REP").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_lf'] = ops_qs.filter(trip_code="OPS-LF").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_stb'] = ops_qs.filter(trip_code="STB").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_brkd'] = ops_qs.filter(trip_code="BRKD").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_offhire'] = ops_qs.filter(trip_code="OFFHIRE").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_trips'] = ops_qs.aggregate(Sum('trip_activity'))
        ops_digest['ton_cargo'] = ops_qs.aggregate(Sum('section2_ton_cargo'))
        ops_digest['no_lifts'] = ops_qs.aggregate(Sum('section2_time_taken'))
        ops_digest['ton_lifts'] = ops_qs.aggregate(Sum('section2_time_taken'))
        ops_digest['no_routine'] = ops_qs.aggregate(Sum('no_routine'))
        ops_digest['no_simple'] = ops_qs.aggregate(Sum('no_simple'))
        ops_digest['no_complicated'] = ops_qs.aggregate(Sum('no_complicated'))
        ops_digest['no_complex'] = ops_qs.aggregate(Sum('no_complex'))
        ops_digest['ton_routine'] = ops_qs.aggregate(Sum('ton_routine'))
        ops_digest['ton_simple'] = ops_qs.aggregate(Sum('ton_simple'))
        ops_digest['ton_complicated'] = ops_qs.aggregate(Sum('ton_complicated'))
        ops_digest['ton_complex'] = ops_qs.aggregate(Sum('ton_complex'))

        ops_digest['llt_dsb'] = ops_qs.aggregate(Sum('llt_dsb'))
        ops_digest['llt_tgi'] = ops_qs.aggregate(Sum('llt_tgi'))
        ops_digest['llt_rig1'] = ops_qs.aggregate(Sum('llt_rig1'))
        ops_digest['llt_rig2'] = ops_qs.aggregate(Sum('llt_rig2'))
        ops_digest['llt_rig3'] = ops_qs.aggregate(Sum('llt_rig3'))
        ops_digest['llt_other'] = ops_qs.aggregate(Sum('llt_other'))

        ops_digest['tlt_dsb'] = ops_qs.aggregate(Sum('tlt_dsb'))
        ops_digest['tlt_tgi'] = ops_qs.aggregate(Sum('tlt_tgi'))
        ops_digest['tlt_rig1'] = ops_qs.aggregate(Sum('tlt_rig1'))
        ops_digest['tlt_rig2'] = ops_qs.aggregate(Sum('tlt_rig2'))
        ops_digest['tlt_rig3'] = ops_qs.aggregate(Sum('tlt_rig3'))
        ops_digest['tlt_other'] = ops_qs.aggregate(Sum('tlt_other'))

        ops_digest['dnt_dsb'] = ops_qs.aggregate(Sum('dnt_dsb'))
        ops_digest['dnt_tgi'] = ops_qs.aggregate(Sum('dnt_tgi'))
        ops_digest['dnt_rig1'] = ops_qs.aggregate(Sum('dnt_rig1'))
        ops_digest['dnt_rig2'] = ops_qs.aggregate(Sum('dnt_rig2'))
        ops_digest['dnt_rig3'] = ops_qs.aggregate(Sum('dnt_rig3'))
        ops_digest['dnt_other'] = ops_qs.aggregate(Sum('dnt_other'))
        
        ops_digest['kms_passed'] = ops_qs.aggregate(Sum('kms_passed'))
        ops_digest['consol_fuel'] = ops_qs.aggregate(Sum('consol_fuel'))
            
        wo_digest = {}
        wo_digest['ops_digest'] = ops_digest
        wo_digest['wo_qs'] = wo_qs
        wo_digest['wo_asset_qs'] = wo_asset_qs
        wo_digest['wo_personnel_qs'] = wo_personnel_qs
        wo_digest['wo_task_qs'] = wo_task_qs
        wo_digest['wo_task_asset_qs'] = wo_task_asset_qs
        wo_digest['wo_task_personnel_qs'] = wo_task_personnel_qs
        wo_digest['jcd_qs'] = jcd_qs
        wo_digest['invoices'] = invoice_qs
        wo_digest['kpi_pob_qs'] = kpi_pob_qs
        wo_digest['kpi_onoff_qs'] = kpi_onoff_qs
        wo_digest['kpi_ops_qs'] = kpi_ops_qs
        #count
        wo_digest['ops_digest_count'] = len(ops_digest)
        wo_digest['wo_qs_count'] = wo_qs.count()
        wo_digest['wo_asset_qs_count'] = wo_asset_qs.count()
        wo_digest['wo_personnel_qs_count'] = wo_personnel_qs.count()
        wo_digest['wo_task_qs_count'] = wo_task_qs.count()
        wo_digest['wo_task_asset_qs_count'] = wo_task_asset_qs.count()
        wo_digest['wo_task_personnel_qs_count'] = wo_task_personnel_qs.count()
        wo_digest['jcd_qs_count'] = jcd_qs.count()
        wo_digest['invoices_count'] = invoice_qs.count()

        # Statistics
        wo_digest['stat_nox_tasks'] = wo_task_qs.count
        wo_digest['stat_nox_assets'] = wo_asset_qs.count
        wo_digest['stat_nox_personnel'] = wo_personnel_qs.count
        wo_digest['stat_nox_task_asset'] = wo_task_asset_qs.count
        wo_digest['stat_nox_task_personnel'] = wo_task_personnel_qs.count
        wo_digest['stat_nox_onoff'] = kpi_onoff_qs.count
        wo_digest['stat_nox_onoff'] = kpi_onoff_qs.count
        wo_digest['stat_nox_onoff_SN'] = kpi_onoff_qs.filter(allocation="SN")
        wo_digest['stat_nox_onoff_NN'] = kpi_onoff_qs.filter(allocation="NN")
        wo_digest['stat_nox_ops'] = kpi_ops_qs
        wo_digest['stat_nox_ops_TR'] = kpi_ops_qs.filter(trip_code="OPS-TR")
        wo_digest['stat_nox_ops_REP'] = kpi_ops_qs.filter(trip_code="OPS-REP")
        wo_digest['stat_nox_ops_LF'] = kpi_ops_qs.filter(trip_code="OPS-LF")
        wo_digest['stat_nox_ops_STB'] = kpi_ops_qs.filter(trip_code="STB")
        wo_digest['stat_nox_ops_BRKD'] = kpi_ops_qs.filter(trip_code="BRKD")
        wo_digest['stat_nox_ops_OFFHIRE'] = kpi_ops_qs.filter(trip_code="OFFHIRE")
        wo_digest['stat_nox_pob'] = agg_pob.count
        wo_digest['stat_nox_pob_MH'] = agg_pob.count
        wo_digest['stat_nox_pob_SN'] = agg_pob.filter(allocation="SN").count
        wo_digest['stat_nox_pob_NN'] = agg_pob.filter(allocation="NN").count
        wo_digest['stat_nox_pobs_MH'] = agg_pob.count
        wo_digest['stat_nox_pobs_SN'] = agg_pob.filter(allocation="SN").count
        wo_digest['stat_nox_pobs_NN'] = agg_pob.filter(allocation="NN").count

        context['wo_digest'] = wo_digest

        return context

    def get_queryset(self):
        return WorkOrderModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')

    def get_incoice_list(self, cust):
        return InvoiceModel.objects.for_work_order(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
            work_order=cust
        )
        
    def get_total_invoiced(self, invoice_qs):        
        #tot_amt_owed = list ((inv['amount_due'], v) for inv, v in invoice_qs)
        tot_amt_invoiced = 0
        for inv in invoice_qs:
            tot_amt_invoiced += inv.amount_due
        return tot_amt_invoiced

    def get_total_paid(self, invoice_qs):
        tot_amt_paid = 0
        for inv in invoice_qs:
            tot_amt_paid += inv.amount_paid
        return tot_amt_paid

    def get_total_owed(self, amt_invoiced=0, amt_paid=0):
        return amt_invoiced - amt_paid

    def get_total_no_invoices(self, invoice_qs, invoice_state=None):
        tot_number = 0
        for inv in invoice_qs:
            if invoice_state == 'cleared' and (inv.amount_paid >= inv.amount_due):
                tot_number += 1
            if invoice_state == 'pending' and (inv.amount_due >= inv.amount_paid):
                tot_number += 1
        return tot_number


class WorkOrderModelListView(LoginRequiredMixIn, ListView):
    # template_name = 'aix/app/operations/work_order.html'
    template_name = 'aix/app/operations/work_order.html'
    context_object_name = 'work_orders'
    PAGE_TITLE = _('WorkOrder List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        customer_qs = CustomerModel.objects.all()
        user_id = self.request.user.id
        # user_id = 'f9246d4b44c440169ea3ac8e979129e0'
        # print(user_id)
        # customer_model: CustomerModel = get_object_or_404(customer_qs, uuid__exact=user_id)
        # customer_model: CustomerModel = get_object_or_404(customer_qs, user__id=user_id)
        customer_model: CustomerModel = customer_qs.filter().first()
        title = f'Customer {customer_model.customer_name}'
        context['page_title'] = title
        context['header_title'] = title

        invoice_qs = InvoiceModel.objects.for_entity_owed(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                customer=customer_model
            ).select_related('ledger__entity')
        
        inv_amt_invoiced = self.get_total_invoiced(invoice_qs)
        inv_amt_paid = self.get_total_paid(invoice_qs)

        context['is_advanced'] = True
        context['invoices'] = self.get_incoice_list(customer_model)
        context['total_invoiced'] = inv_amt_invoiced
        context['total_paid'] = inv_amt_paid
        context['total_owed'] = self.get_total_owed(inv_amt_invoiced, inv_amt_paid)
        context['total_paid_invoices'] = self.get_total_no_invoices(invoice_qs, 'cleared')
        context['total_owed_invoices'] = self.get_total_no_invoices(invoice_qs, 'pending')
        
        wo_task_qs = WorkOrderTaskModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        wo_task_asset_qs = WorkOrderTaskAssetModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        wo_task_personnel_qs = WorkOrderTaskPersonnelModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        wo_asset_qs = WorkOrderAssetModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        wo_personnel_qs = WorkOrderPersonnelModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        wo_equipment_qs = EquipmentModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        invoice_qs = InvoiceModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        jcd_qs = WorkOrderJobcardModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        jcd_qs = jcd_qs.select_related('work_order')        
        kpi_pob_qs = KpiPobModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        kpi_onoff_qs = KpiOnOffModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        kpi_ops_qs = KpiOpsModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        kpi_hse_qs = KpiHseModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        
        agg_pob = KpiPobModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )

        ops_qs = kpi_ops_qs.select_related('task__work_order')
        wo_qs = self.get_queryset()
        
        hse_digest = {}
        hse_digest['fat'] = kpi_hse_qs.aggregate(Sum('fat'))
        hse_digest['lti'] = kpi_hse_qs.aggregate(Sum('lti'))
        hse_digest['rwdc'] = kpi_hse_qs.aggregate(Sum('rwdc'))
        hse_digest['mtc'] = kpi_hse_qs.aggregate(Sum('mtc'))
        hse_digest['fac'] = kpi_hse_qs.aggregate(Sum('fac'))
        hse_digest['hipo'] = kpi_hse_qs.aggregate(Sum('hipo'))
        hse_digest['envdam'] = kpi_hse_qs.aggregate(Sum('envdam'))
        hse_digest['nmi'] = kpi_hse_qs.aggregate(Sum('nmi'))
        hse_digest['matloss'] = kpi_hse_qs.aggregate(Sum('matloss'))
        hse_digest['ptw'] = kpi_hse_qs.aggregate(Sum('ptw'))
        hse_digest['tbt'] = kpi_hse_qs.aggregate(Sum('tbt'))
        hse_digest['hht'] = kpi_hse_qs.aggregate(Sum('hht'))
        hse_digest['drills'] = kpi_hse_qs.aggregate(Sum('drills'))
        hse_digest['audit'] = kpi_hse_qs.aggregate(Sum('audit'))
        hse_digest['reporting_cards'] = kpi_hse_qs.aggregate(Sum('reporting_cards'))
        hse_digest['safety_initiative'] = kpi_hse_qs.aggregate(Sum('safety_initiative'))
        context['hse_digest'] = hse_digest
        
        ops_digest = {}
        ops_digest['hrs_ops'] = ops_qs.filter(trip_code="OPS-TR").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_rep'] = ops_qs.filter(trip_code="OPS-REP").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_lf'] = ops_qs.filter(trip_code="OPS-LF").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_stb'] = ops_qs.filter(trip_code="STB").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_brkd'] = ops_qs.filter(trip_code="BRKD").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_offhire'] = ops_qs.filter(trip_code="OFFHIRE").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_trips'] = ops_qs.aggregate(Sum('trip_activity'))
        ops_digest['ton_cargo'] = ops_qs.aggregate(Sum('section2_ton_cargo'))
        ops_digest['no_lifts'] = ops_qs.aggregate(Sum('section2_time_taken'))
        ops_digest['ton_lifts'] = ops_qs.aggregate(Sum('section2_time_taken'))
        ops_digest['no_routine'] = ops_qs.aggregate(Sum('no_routine'))
        ops_digest['no_simple'] = ops_qs.aggregate(Sum('no_simple'))
        ops_digest['no_complicated'] = ops_qs.aggregate(Sum('no_complicated'))
        ops_digest['no_complex'] = ops_qs.aggregate(Sum('no_complex'))
        ops_digest['ton_routine'] = ops_qs.aggregate(Sum('ton_routine'))
        ops_digest['ton_simple'] = ops_qs.aggregate(Sum('ton_simple'))
        ops_digest['ton_complicated'] = ops_qs.aggregate(Sum('ton_complicated'))
        ops_digest['ton_complex'] = ops_qs.aggregate(Sum('ton_complex'))

        ops_digest['llt_dsb'] = ops_qs.aggregate(Sum('llt_dsb'))
        ops_digest['llt_tgi'] = ops_qs.aggregate(Sum('llt_tgi'))
        ops_digest['llt_rig1'] = ops_qs.aggregate(Sum('llt_rig1'))
        ops_digest['llt_rig2'] = ops_qs.aggregate(Sum('llt_rig2'))
        ops_digest['llt_rig3'] = ops_qs.aggregate(Sum('llt_rig3'))
        ops_digest['llt_other'] = ops_qs.aggregate(Sum('llt_other'))

        ops_digest['tlt_dsb'] = ops_qs.aggregate(Sum('tlt_dsb'))
        ops_digest['tlt_tgi'] = ops_qs.aggregate(Sum('tlt_tgi'))
        ops_digest['tlt_rig1'] = ops_qs.aggregate(Sum('tlt_rig1'))
        ops_digest['tlt_rig2'] = ops_qs.aggregate(Sum('tlt_rig2'))
        ops_digest['tlt_rig3'] = ops_qs.aggregate(Sum('tlt_rig3'))
        ops_digest['tlt_other'] = ops_qs.aggregate(Sum('tlt_other'))

        ops_digest['dnt_dsb'] = ops_qs.aggregate(Sum('dnt_dsb'))
        ops_digest['dnt_tgi'] = ops_qs.aggregate(Sum('dnt_tgi'))
        ops_digest['dnt_rig1'] = ops_qs.aggregate(Sum('dnt_rig1'))
        ops_digest['dnt_rig2'] = ops_qs.aggregate(Sum('dnt_rig2'))
        ops_digest['dnt_rig3'] = ops_qs.aggregate(Sum('dnt_rig3'))
        ops_digest['dnt_other'] = ops_qs.aggregate(Sum('dnt_other'))
        
        ops_digest['kms_passed'] = ops_qs.aggregate(Sum('kms_passed'))
        ops_digest['consol_fuel'] = ops_qs.aggregate(Sum('consol_fuel'))

            
        wo_digest = {}
        wo_digest['ops_digest'] = ops_digest
        wo_digest['wo_qs'] = wo_qs
        wo_digest['wo_asset_qs'] = wo_asset_qs
        wo_digest['wo_personnel_qs'] = wo_personnel_qs
        wo_digest['wo_task_qs'] = wo_task_qs
        wo_digest['wo_task_asset_qs'] = wo_task_asset_qs
        wo_digest['wo_task_personnel_qs'] = wo_task_personnel_qs
        wo_digest['jcd_qs'] = jcd_qs
        wo_digest['invoices'] = invoice_qs
        wo_digest['kpi_pob_qs'] = kpi_pob_qs
        wo_digest['kpi_onoff_qs'] = kpi_onoff_qs
        wo_digest['kpi_ops_qs'] = kpi_ops_qs
        #count
        wo_digest['ops_digest_count'] = len(ops_digest)
        wo_digest['wo_qs_count'] = wo_qs.count()
        wo_digest['wo_asset_qs_count'] = wo_asset_qs.count()
        wo_digest['wo_personnel_qs_count'] = wo_personnel_qs.count()
        wo_digest['wo_equipment_qs'] = wo_equipment_qs
        wo_digest['wo_task_qs_count'] = wo_task_qs.count()
        wo_digest['wo_task_asset_qs_count'] = wo_task_asset_qs.count()
        wo_digest['wo_task_personnel_qs_count'] = wo_task_personnel_qs.count()
        wo_digest['jcd_qs_count'] = jcd_qs.count()
        wo_digest['invoices_count'] = invoice_qs.count()
        wo_digest['wo_active'] = wo_qs.filter(is_active=True)
        wo_digest['wo_inactive'] = wo_qs.filter(is_active=False)
        wo_digest['wo_asset_active'] = wo_asset_qs.filter(wostatus='ALLOCATED')
        wo_digest['wo_personnel_active'] = wo_personnel_qs.filter(wostatus='ALLOCATED')
        wo_digest['wo_asset_inactive'] = wo_asset_qs.filter(wostatus=None)
        wo_digest['wo_personnel_inactive'] = wo_personnel_qs.filter(wostatus=None)
        wo_digest['wo_equipment_active'] = wo_equipment_qs.filter(status='ALLOCATED')
        wo_digest['wo_equipment_inactive'] = wo_equipment_qs.filter(status=None)

        # Statistics
        wo_digest['stat_nox_tasks'] = wo_task_qs.count
        wo_digest['stat_nox_assets'] = wo_asset_qs.count
        wo_digest['stat_nox_personnel'] = wo_personnel_qs.count
        wo_digest['stat_nox_task_asset'] = wo_task_asset_qs.count
        wo_digest['stat_nox_task_personnel'] = wo_task_personnel_qs.count
        wo_digest['stat_nox_onoff'] = kpi_onoff_qs.count
        wo_digest['stat_nox_onoff'] = kpi_onoff_qs.count
        wo_digest['stat_nox_onoff_SN'] = kpi_onoff_qs.filter(allocation="SN")
        wo_digest['stat_nox_onoff_NN'] = kpi_onoff_qs.filter(allocation="NN")
        wo_digest['stat_nox_ops'] = kpi_ops_qs
        wo_digest['stat_nox_ops_TR'] = kpi_ops_qs.filter(trip_code="OPS-TR")
        wo_digest['stat_nox_ops_REP'] = kpi_ops_qs.filter(trip_code="OPS-REP")
        wo_digest['stat_nox_ops_LF'] = kpi_ops_qs.filter(trip_code="OPS-LF")
        wo_digest['stat_nox_ops_STB'] = kpi_ops_qs.filter(trip_code="STB")
        wo_digest['stat_nox_ops_BRKD'] = kpi_ops_qs.filter(trip_code="BRKD")
        wo_digest['stat_nox_ops_OFFHIRE'] = kpi_ops_qs.filter(trip_code="OFFHIRE")
        wo_digest['stat_nox_pob'] = agg_pob.count
        wo_digest['stat_nox_pob_MH'] = agg_pob.count
        wo_digest['stat_nox_pob_SN'] = agg_pob.filter(allocation="SN").count
        wo_digest['stat_nox_pob_NN'] = agg_pob.filter(allocation="NN").count
        wo_digest['stat_nox_pobs_MH'] = agg_pob.count
        wo_digest['stat_nox_pobs_SN'] = agg_pob.filter(allocation="SN").count
        wo_digest['stat_nox_pobs_NN'] = agg_pob.filter(allocation="NN").count

        context['wo_digest'] = wo_digest

        return context

    def get_queryset(self):
        return WorkOrderModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')

    def get_incoice_list(self, cust):
        return InvoiceModel.objects.for_work_order(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
            work_order=cust
        )
        
    def get_total_invoiced(self, invoice_qs):        
        #tot_amt_owed = list ((inv['amount_due'], v) for inv, v in invoice_qs)
        tot_amt_invoiced = 0
        for inv in invoice_qs:
            tot_amt_invoiced += inv.amount_due
        return tot_amt_invoiced

    def get_total_paid(self, invoice_qs):
        tot_amt_paid = 0
        for inv in invoice_qs:
            tot_amt_paid += inv.amount_paid
        return tot_amt_paid

    def get_total_owed(self, amt_invoiced=0, amt_paid=0):
        return amt_invoiced - amt_paid

    def get_total_no_invoices(self, invoice_qs, invoice_state=None):
        tot_number = 0
        for inv in invoice_qs:
            if invoice_state == 'cleared' and (inv.amount_paid >= inv.amount_due):
                tot_number += 1
            if invoice_state == 'pending' and (inv.amount_due >= inv.amount_paid):
                tot_number += 1
        return tot_number


class WorkOrderModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/work_order.html'
    PAGE_TITLE = _('Create New WorkOrder')
    form_class = WorkOrderForm
    context_object_name = 'work_order'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill',
        'hide_menu': True
    }

    def get_queryset(self):
        return WorkOrderForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        work_order_model: WorkOrderModel = form.save(commit=False)
        customer_qs = CustomerModel.objects.all()
        # user_id = 'f9246d4b44c440169ea3ac8e979129e0'
        # customer_model: CustomerModel = get_object_or_404(customer_qs, uuid__exact=user_id)
        customer_model: CustomerModel = customer_qs.filter().first()
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        work_order_model.entity = entity_model
        work_order_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
        )
        work_order_model.customer = customer_model
        work_order_model.save()
        form.send(email=self.request.user.email, work_order=work_order_model)
        return super().form_valid(form)

class WorkOrderModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/work_order.html'
    PAGE_TITLE = _('WorkOrder Update')
    context_object_name = 'work_order'
    form_class = WorkOrderForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill',
        'hide_menu': True
    }
    slug_url_kwarg = 'work_order_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return WorkOrderModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class WorkOrderModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'work_order_pk'
    slug_field = 'uuid'
    context_object_name = 'work_order'
    #template_name = 'aix/advanced/work_order/work_order_detail.html'
    template_name = 'aix/app/operations/details/wo_details.html'
    extra_context = {
        'hide_menu': True
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        work_order_model: WorkOrderModel = self.object
        customer_model: CustomerModel = work_order_model.customer
        title = f'Customer {customer_model.customer_name}'
        context['page_title'] = title
        context['header_title'] = title

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
        # self.kwargs['usr_group'] = context['usr_group']
        context['usr_group'] = self.request.user.groups

        invoice_qs = InvoiceModel.objects.for_entity_owed(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                customer=customer_model
            ).select_related('ledger__entity')
        
        inv_amt_invoiced = self.get_total_invoiced(invoice_qs)
        inv_amt_paid = self.get_total_paid(invoice_qs)

        context['is_advanced'] = True
        context['invoices'] = self.get_incoice_list(work_order_model.customer)
        context['total_invoiced'] = inv_amt_invoiced
        context['total_paid'] = inv_amt_paid
        context['total_owed'] = self.get_total_owed(inv_amt_invoiced, inv_amt_paid)
        context['total_paid_invoices'] = self.get_total_no_invoices(invoice_qs, 'cleared')
        context['total_owed_invoices'] = self.get_total_no_invoices(invoice_qs, 'pending')
        
        wo_task_qs = WorkOrderTaskModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                work_order=work_order_model
            )
        wo_task_asset_qs = WorkOrderTaskAssetModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                work_order=work_order_model
            )
        wo_task_personnel_qs = WorkOrderTaskPersonnelModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                work_order=work_order_model
            )
        wo_asset_qs = WorkOrderAssetModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                work_order=work_order_model
            )
        wo_personnel_qs = WorkOrderPersonnelModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                work_order=work_order_model
            )
        invoice_qs = InvoiceModel.objects.for_work_order_detail(
                entity_slug=self.kwargs['entity_slug'],
                work_order=work_order_model
            )
        jcd_qs = WorkOrderJobcardModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                work_order=work_order_model
            )
        document_qs = DocumentModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                work_order=work_order_model
            )
        wo_qs = jcd_qs.select_related('work_order')
        wo_work_order_qs = WorkOrderModel.objects.for_customer(
                entity_slug=self.kwargs['entity_slug'],
                customer=customer_model
            )
        
        kpi_pob_qs = KpiPobModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        kpi_onoff_qs = KpiOnOffModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        kpi_ops_qs = KpiOpsModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                work_order=work_order_model
            )
        # agg_pob = WorkOrderModel.objects.annotate(pobs=Subquery(
        #             KpiPobModel.objects.filter(work_order=work_order_model)
        #         )
        #     )
        
        agg_pob = KpiPobModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                work_order=work_order_model
            )

        ops_qs = kpi_ops_qs.select_related('task__work_order')

        ops_digest = {}
        ops_digest['hrs_ops'] = ops_qs.filter(trip_code="OPS-TR").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_rep'] = ops_qs.filter(trip_code="OPS-REP").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_lf'] = ops_qs.filter(trip_code="OPS-LF").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_stb'] = ops_qs.filter(trip_code="STB").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_brkd'] = ops_qs.filter(trip_code="BRKD").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_offhire'] = ops_qs.filter(trip_code="OFFHIRE").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_trips'] = ops_qs.aggregate(Sum('trip_activity'))
        ops_digest['ton_cargo'] = ops_qs.aggregate(Sum('section2_ton_cargo'))
        ops_digest['no_lifts'] = ops_qs.aggregate(Sum('section2_time_taken'))
        ops_digest['ton_lifts'] = ops_qs.aggregate(Sum('section2_time_taken'))
        ops_digest['no_routine'] = ops_qs.aggregate(Sum('no_routine'))
        ops_digest['no_simple'] = ops_qs.aggregate(Sum('no_simple'))
        ops_digest['no_complicated'] = ops_qs.aggregate(Sum('no_complicated'))
        ops_digest['no_complex'] = ops_qs.aggregate(Sum('no_complex'))
        ops_digest['ton_routine'] = ops_qs.aggregate(Sum('ton_routine'))
        ops_digest['ton_simple'] = ops_qs.aggregate(Sum('ton_simple'))
        ops_digest['ton_complicated'] = ops_qs.aggregate(Sum('ton_complicated'))
        ops_digest['ton_complex'] = ops_qs.aggregate(Sum('ton_complex'))

        ops_digest['llt_dsb'] = ops_qs.aggregate(Sum('llt_dsb'))
        ops_digest['llt_tgi'] = ops_qs.aggregate(Sum('llt_tgi'))
        ops_digest['llt_rig1'] = ops_qs.aggregate(Sum('llt_rig1'))
        ops_digest['llt_rig2'] = ops_qs.aggregate(Sum('llt_rig2'))
        ops_digest['llt_rig3'] = ops_qs.aggregate(Sum('llt_rig3'))
        ops_digest['llt_other'] = ops_qs.aggregate(Sum('llt_other'))

        ops_digest['tlt_dsb'] = ops_qs.aggregate(Sum('tlt_dsb'))
        ops_digest['tlt_tgi'] = ops_qs.aggregate(Sum('tlt_tgi'))
        ops_digest['tlt_rig1'] = ops_qs.aggregate(Sum('tlt_rig1'))
        ops_digest['tlt_rig2'] = ops_qs.aggregate(Sum('tlt_rig2'))
        ops_digest['tlt_rig3'] = ops_qs.aggregate(Sum('tlt_rig3'))
        ops_digest['tlt_other'] = ops_qs.aggregate(Sum('tlt_other'))

        ops_digest['dnt_dsb'] = ops_qs.aggregate(Sum('dnt_dsb'))
        ops_digest['dnt_tgi'] = ops_qs.aggregate(Sum('dnt_tgi'))
        ops_digest['dnt_rig1'] = ops_qs.aggregate(Sum('dnt_rig1'))
        ops_digest['dnt_rig2'] = ops_qs.aggregate(Sum('dnt_rig2'))
        ops_digest['dnt_rig3'] = ops_qs.aggregate(Sum('dnt_rig3'))
        ops_digest['dnt_other'] = ops_qs.aggregate(Sum('dnt_other'))
        
        ops_digest['kms_passed'] = ops_qs.aggregate(Sum('kms_passed'))
        ops_digest['consol_fuel'] = ops_qs.aggregate(Sum('consol_fuel'))
            
        wo_digest = {}
        wo_digest['ops_digest'] = ops_digest
        wo_digest['wo_qs'] = wo_qs
        wo_digest['wo_asset_qs'] = wo_asset_qs
        wo_digest['wo_personnel_qs'] = wo_personnel_qs
        wo_digest['wo_document_qs'] = document_qs
        wo_digest['wo_task_qs'] = wo_task_qs
        wo_digest['wo_task_asset_qs'] = wo_task_asset_qs
        wo_digest['wo_task_personnel_qs'] = wo_task_personnel_qs
        wo_digest['wo_work_order_qs'] = wo_work_order_qs
        wo_digest['jcd_qs'] = jcd_qs
        wo_digest['invoices'] = invoice_qs
        wo_digest['kpi_pob_qs'] = kpi_pob_qs
        wo_digest['kpi_onoff_qs'] = kpi_onoff_qs
        wo_digest['kpi_ops_qs'] = kpi_ops_qs

        # Statistics
        wo_digest['stat_nox_tasks'] = wo_task_qs.count
        wo_digest['stat_nox_assets'] = wo_asset_qs.count
        wo_digest['stat_nox_personnel'] = wo_personnel_qs.count
        wo_digest['stat_nox_task_asset'] = wo_task_asset_qs.count
        wo_digest['stat_nox_task_personnel'] = wo_task_personnel_qs.count
        wo_digest['stat_nox_onoff'] = kpi_onoff_qs.count
        wo_digest['stat_nox_onoff'] = kpi_onoff_qs.count
        wo_digest['stat_nox_onoff_SN'] = kpi_onoff_qs.filter(allocation="SN")
        wo_digest['stat_nox_onoff_NN'] = kpi_onoff_qs.filter(allocation="NN")
        wo_digest['stat_nox_ops'] = kpi_ops_qs
        wo_digest['stat_nox_ops_TR'] = kpi_ops_qs.filter(trip_code="OPS-TR")
        wo_digest['stat_nox_ops_REP'] = kpi_ops_qs.filter(trip_code="OPS-REP")
        wo_digest['stat_nox_ops_LF'] = kpi_ops_qs.filter(trip_code="OPS-LF")
        wo_digest['stat_nox_ops_STB'] = kpi_ops_qs.filter(trip_code="STB")
        wo_digest['stat_nox_ops_BRKD'] = kpi_ops_qs.filter(trip_code="BRKD")
        wo_digest['stat_nox_ops_OFFHIRE'] = kpi_ops_qs.filter(trip_code="OFFHIRE")
        wo_digest['stat_nox_pob'] = agg_pob.count
        wo_digest['stat_nox_pob_MH'] = agg_pob.count
        wo_digest['stat_nox_pob_SN'] = agg_pob.filter(allocation="SN").count
        wo_digest['stat_nox_pob_NN'] = agg_pob.filter(allocation="NN").count
        wo_digest['stat_nox_pobs_MH'] = agg_pob.count
        wo_digest['stat_nox_pobs_SN'] = agg_pob.filter(allocation="SN").count
        wo_digest['stat_nox_pobs_NN'] = agg_pob.filter(allocation="NN").count
        
        context['wo_digest'] = wo_digest

        work_order_forms = {}
        work_order_forms['frm_document'] = DocumentForm
        context['work_order_forms'] = work_order_forms
        
        return context

    def get_queryset(self):
        return WorkOrderModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_incoice_list(self, cust):
        return InvoiceModel.objects.for_work_order(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
            work_order=cust
        )
        
    def get_total_invoiced(self, invoice_qs):        
        #tot_amt_owed = list ((inv['amount_due'], v) for inv, v in invoice_qs)
        tot_amt_invoiced = 0
        for inv in invoice_qs:
            tot_amt_invoiced += inv.amount_due
        return tot_amt_invoiced

    def get_total_paid(self, invoice_qs):
        tot_amt_paid = 0
        for inv in invoice_qs:
            tot_amt_paid += inv.amount_paid
        return tot_amt_paid

    def get_total_owed(self, amt_invoiced=0, amt_paid=0):
        return amt_invoiced - amt_paid

    def get_total_no_invoices(self, invoice_qs, invoice_state=None):
        tot_number = 0
        for inv in invoice_qs:
            if invoice_state == 'cleared' and (inv.amount_paid >= inv.amount_due):
                tot_number += 1
            if invoice_state == 'pending' and (inv.amount_due >= inv.amount_paid):
                tot_number += 1
        return tot_number


class WorkOrderModelReportView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'work_order_pk'
    slug_field = 'uuid'
    context_object_name = 'work_order'
    #template_name = 'aix/advanced/work_order/work_order_detail.html'
    template_name = 'aix/app/operations/details/wo_details.html'
    extra_context = {
        'hide_menu': True
    }
    dwn_report_file = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        work_order_model: WorkOrderModel = self.object
        customer_model: CustomerModel = work_order_model.customer
        title = f'Customer {customer_model.customer_name}'
        context['page_title'] = title
        context['header_title'] = title

        invoice_qs = InvoiceModel.objects.for_entity_owed(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                customer=customer_model
            ).select_related('ledger__entity')
        
        inv_amt_invoiced = self.get_total_invoiced(invoice_qs)
        inv_amt_paid = self.get_total_paid(invoice_qs)

        context['is_advanced'] = True
        context['invoices'] = self.get_incoice_list(work_order_model.customer)
        context['total_invoiced'] = inv_amt_invoiced
        context['total_paid'] = inv_amt_paid
        context['total_owed'] = self.get_total_owed(inv_amt_invoiced, inv_amt_paid)
        context['total_paid_invoices'] = self.get_total_no_invoices(invoice_qs, 'cleared')
        context['total_owed_invoices'] = self.get_total_no_invoices(invoice_qs, 'pending')
        
        wo_task_qs = WorkOrderTaskModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                work_order=work_order_model
            )
        wo_task_asset_qs = WorkOrderTaskAssetModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                work_order=work_order_model
            )
        wo_task_personnel_qs = WorkOrderTaskPersonnelModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                work_order=work_order_model
            )
        wo_asset_qs = WorkOrderAssetModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                work_order=work_order_model
            )
        wo_personnel_qs = WorkOrderPersonnelModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                work_order=work_order_model
            )
        invoice_qs = InvoiceModel.objects.for_work_order_detail(
                entity_slug=self.kwargs['entity_slug'],
                work_order=work_order_model
            )
        jcd_qs = WorkOrderJobcardModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                work_order=work_order_model
            )
        
        # jcd_items_qs, item_data = work_order_model.get_jcd_item_data(
        #     queryset=work_order_model__jcd_model.itemthroughmodel_set.all().select_related('item_model')
        # )

        wo_qs = jcd_qs.select_related('work_order')
        wo_work_order_qs = WorkOrderModel.objects.for_customer(
                entity_slug=self.kwargs['entity_slug'],
                customer=customer_model
            )
        
        kpi_pob_qs = KpiPobModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        kpi_onoff_qs = KpiOnOffModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        kpi_ops_qs = KpiOpsModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                work_order=work_order_model
            )
        wo_assets = WorkOrderAssetModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        wo_personnel = WorkOrderPersonnelModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                work_order=work_order_model
            )
        # agg_pob = WorkOrderModel.objects.annotate(pobs=Subquery(
        #             KpiPobModel.objects.filter(work_order=work_order_model)
        #         )
        #     )
        
        agg_pob = KpiPobModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                work_order=work_order_model
            )

        ops_qs = kpi_ops_qs.select_related('task__work_order')

        context['incidents'] = 0
        context['inspections'] = 0
        context['onoffs'] = kpi_onoff_qs
        context['pobs'] = kpi_pob_qs
        context['assets'] = wo_assets
        context['personnel'] = wo_personnel

        ops_digest = {}
        ops_digest['hrs_ops'] = ops_qs.filter(trip_code="OPS-TR").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_rep'] = ops_qs.filter(trip_code="OPS-REP").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_lf'] = ops_qs.filter(trip_code="OPS-LF").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_stb'] = ops_qs.filter(trip_code="STB").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_brkd'] = ops_qs.filter(trip_code="BRKD").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_offhire'] = ops_qs.filter(trip_code="OFFHIRE").aggregate(Sum('section2_time_taken'))
        ops_digest['hrs_trips'] = ops_qs.aggregate(Sum('trip_activity'))
        ops_digest['ton_cargo'] = ops_qs.aggregate(Sum('section2_ton_cargo'))
        ops_digest['no_lifts'] = ops_qs.aggregate(Sum('section2_time_taken'))
        ops_digest['ton_lifts'] = ops_qs.aggregate(Sum('section2_time_taken'))
        ops_digest['no_routine'] = ops_qs.aggregate(Sum('no_routine'))
        ops_digest['no_simple'] = ops_qs.aggregate(Sum('no_simple'))
        ops_digest['no_complicated'] = ops_qs.aggregate(Sum('no_complicated'))
        ops_digest['no_complex'] = ops_qs.aggregate(Sum('no_complex'))
        ops_digest['ton_routine'] = ops_qs.aggregate(Sum('ton_routine'))
        ops_digest['ton_simple'] = ops_qs.aggregate(Sum('ton_simple'))
        ops_digest['ton_complicated'] = ops_qs.aggregate(Sum('ton_complicated'))
        ops_digest['ton_complex'] = ops_qs.aggregate(Sum('ton_complex'))

        ops_digest['llt_dsb'] = ops_qs.aggregate(Sum('llt_dsb'))
        ops_digest['llt_tgi'] = ops_qs.aggregate(Sum('llt_tgi'))
        ops_digest['llt_rig1'] = ops_qs.aggregate(Sum('llt_rig1'))
        ops_digest['llt_rig2'] = ops_qs.aggregate(Sum('llt_rig2'))
        ops_digest['llt_rig3'] = ops_qs.aggregate(Sum('llt_rig3'))
        ops_digest['llt_other'] = ops_qs.aggregate(Sum('llt_other'))

        ops_digest['tlt_dsb'] = ops_qs.aggregate(Sum('tlt_dsb'))
        ops_digest['tlt_tgi'] = ops_qs.aggregate(Sum('tlt_tgi'))
        ops_digest['tlt_rig1'] = ops_qs.aggregate(Sum('tlt_rig1'))
        ops_digest['tlt_rig2'] = ops_qs.aggregate(Sum('tlt_rig2'))
        ops_digest['tlt_rig3'] = ops_qs.aggregate(Sum('tlt_rig3'))
        ops_digest['tlt_other'] = ops_qs.aggregate(Sum('tlt_other'))

        ops_digest['dnt_dsb'] = ops_qs.aggregate(Sum('dnt_dsb'))
        ops_digest['dnt_tgi'] = ops_qs.aggregate(Sum('dnt_tgi'))
        ops_digest['dnt_rig1'] = ops_qs.aggregate(Sum('dnt_rig1'))
        ops_digest['dnt_rig2'] = ops_qs.aggregate(Sum('dnt_rig2'))
        ops_digest['dnt_rig3'] = ops_qs.aggregate(Sum('dnt_rig3'))
        ops_digest['dnt_other'] = ops_qs.aggregate(Sum('dnt_other'))
        
        ops_digest['kms_passed'] = ops_qs.aggregate(Sum('kms_passed'))
        ops_digest['consol_fuel'] = ops_qs.aggregate(Sum('consol_fuel'))
            
        wo_digest = {}
        wo_digest['ops_digest'] = ops_digest
        wo_digest['work_order'] = work_order_model
        wo_digest['wo_qs'] = wo_qs
        wo_digest['wo_asset_qs'] = wo_asset_qs
        wo_digest['wo_personnel_qs'] = wo_personnel_qs
        wo_digest['wo_task_qs'] = wo_task_qs
        wo_digest['wo_task_asset_qs'] = wo_task_asset_qs
        wo_digest['wo_task_personnel_qs'] = wo_task_personnel_qs
        wo_digest['wo_work_order_qs'] = wo_work_order_qs
        wo_digest['jcd_qs'] = jcd_qs
        # wo_digest['jcd_items'] = jcd_items_qs
        wo_digest['invoices'] = invoice_qs
        wo_digest['kpi_pob_qs'] = kpi_pob_qs
        wo_digest['kpi_onoff_qs'] = kpi_onoff_qs
        wo_digest['kpi_ops_qs'] = kpi_ops_qs

        # Statistics
        wo_digest['stat_nox_tasks'] = wo_task_qs.count
        wo_digest['stat_nox_assets'] = wo_asset_qs.count
        wo_digest['stat_nox_personnel'] = wo_personnel_qs.count
        wo_digest['stat_nox_task_asset'] = wo_task_asset_qs.count
        wo_digest['stat_nox_task_personnel'] = wo_task_personnel_qs.count
        context['stat_nox_onoff'] = kpi_onoff_qs.count
        wo_digest['stat_nox_onoff_SN'] = kpi_onoff_qs.filter(allocation="SN")
        wo_digest['stat_nox_onoff_NN'] = kpi_onoff_qs.filter(allocation="NN")
        wo_digest['stat_nox_ops'] = kpi_ops_qs
        wo_digest['stat_nox_ops_TR'] = kpi_ops_qs.filter(trip_code="OPS-TR")
        wo_digest['stat_nox_ops_REP'] = kpi_ops_qs.filter(trip_code="OPS-REP")
        wo_digest['stat_nox_ops_LF'] = kpi_ops_qs.filter(trip_code="OPS-LF")
        wo_digest['stat_nox_ops_STB'] = kpi_ops_qs.filter(trip_code="STB")
        wo_digest['stat_nox_ops_BRKD'] = kpi_ops_qs.filter(trip_code="BRKD")
        wo_digest['stat_nox_ops_OFFHIRE'] = kpi_ops_qs.filter(trip_code="OFFHIRE")
        wo_digest['stat_nox_pob'] = agg_pob.count
        wo_digest['stat_nox_pob_MH'] = agg_pob.count
        wo_digest['stat_nox_pob_SN'] = agg_pob.filter(allocation="SN").count
        wo_digest['stat_nox_pob_NN'] = agg_pob.filter(allocation="NN").count
        wo_digest['stat_nox_pobs_MH'] = agg_pob.count
        wo_digest['stat_nox_pobs_SN'] = agg_pob.filter(allocation="SN").count
        wo_digest['stat_nox_pobs_NN'] = agg_pob.filter(allocation="NN").count
        
        context['wo_digest'] = wo_digest

        work_order_forms = {}
        context['work_order_forms'] = work_order_forms
        
        return context

    def get_queryset(self):
        return WorkOrderModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_incoice_list(self, cust):
        return InvoiceModel.objects.for_work_order(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
            work_order=cust
        )
        
    def get_total_invoiced(self, invoice_qs):        
        #tot_amt_owed = list ((inv['amount_due'], v) for inv, v in invoice_qs)
        tot_amt_invoiced = 0
        for inv in invoice_qs:
            tot_amt_invoiced += inv.amount_due
        return tot_amt_invoiced

    def get_total_paid(self, invoice_qs):
        tot_amt_paid = 0
        for inv in invoice_qs:
            tot_amt_paid += inv.amount_paid
        return tot_amt_paid

    def get_total_owed(self, amt_invoiced=0, amt_paid=0):
        return amt_invoiced - amt_paid

    def get_total_no_invoices(self, invoice_qs, invoice_state=None):
        tot_number = 0
        for inv in invoice_qs:
            if invoice_state == 'cleared' and (inv.amount_paid >= inv.amount_due):
                tot_number += 1
            if invoice_state == 'pending' and (inv.amount_due >= inv.amount_paid):
                tot_number += 1
        return tot_number

    def get(self, request, *args, **kwargs):
        response = super(WorkOrderModelReportView, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        if self.dwn_report_file:
            # data = CustomerModel.objects.all().order_by('customer_name')
            open('aix/templates/aix/reports/temp.html', "w").write(render_to_string('aix/reports/result.html', {'data': context}))

            # Converting the HTML template into a PDF file
            #pdf = self.html_to_pdf('aix/templates/aix/reports/temp.html', data)
            
            # customer_qs = data.values('customer_name', 'email')
            # df = pd.DataFrame(customer_qs)
            
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template("aix/templates/aix/reports/wo_rpt.html")
            # template = get_template(template_src)
            # context_dict = {"title" : "Customers Report - List"}
            # context_dict['data'] = data
            # data = context['wo_digest']['jcd_qs'].values('jcd_model__jcd_number', 'invoice_model')
            data = context['wo_digest']['wo_qs']
            df = pd.DataFrame.from_dict(data)
            context['rpt_customer_table'] = df.to_html()
            html  = template.render(context)
            result = BytesIO()
            # pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
            pdf = pisa.pisaDocument(BytesIO(html.encode()), result)
            if not pdf.err:
                return HttpResponse(result.getvalue(), content_type='application/pdf')
            return None
        
         # rendering the template
        # return HttpResponse(pdf, content_type='application/pdf')
        return response


class FetDailyStatusReportView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'work_order_pk'
    slug_field = 'uuid'
    context_object_name = 'cummulative_statistics'
    template_name = 'aix/app/dashboard/work_order.html'
    extra_context = {
        'hide_menu': True
    }
    dwn_report_file = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        work_order_model: WorkOrderModel = self.object
        customer_model: CustomerModel = work_order_model.customer
        title = f'Customer {customer_model.customer_name}'
        context['page_title'] = title
        context['header_title'] = title

        equipment_fet_qs = EquipmentFetModel.objects.filter(work_order=self.kwargs['work_order_pk'])
        context['equipment_fets'] = equipment_fet_qs
        return context

    def get_queryset(self):
        return EquipmentFetModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get(self, request, *args, **kwargs):
        response = super(FetDailyStatusReportView, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        if self.dwn_report_file:
            open('aix/templates/aix/reports/temp.html', "w").write(render_to_string('aix/reports/result.html', {'data': context}))

            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template("aix/templates/aix/reports/fet_daily_status_rpt.html")
            data = context['equipment_fets']
            df = pd.DataFrame.from_dict(data)
            # context['rpt_customer_table'] = df.to_html()
            html  = template.render(context)
            result = BytesIO()
            pdf = pisa.pisaDocument(BytesIO(html.encode()), result)
            if not pdf.err:
                return HttpResponse(result.getvalue(), content_type='application/pdf')
            return None
        return response
    
# ACTION VIEWS...
class BaseWorkOrderActionView(LoginRequiredMixIn, RedirectView, SingleObjectMixin):
    http_method_names = ['get']
    pk_url_kwarg = 'work_order_pk'
    action_name = None
    commit = True

    def get_queryset(self):
        return WorkOrderModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_redirect_url(self, *args, **kwargs):
        return reverse('aix:work-order-details',
                       kwargs={
                           'entity_slug': kwargs['entity_slug'],
                           'work_order_pk': kwargs['work_order_pk']
                       })

    def get(self, request, *args, **kwargs):
        kwargs['user_model'] = self.request.user
        if not self.action_name:
            raise ImproperlyConfigured('View attribute action_name is required.')
        response = super(BaseWorkOrderActionView, self).get(request, *args, **kwargs)
        work_order_model: WorkOrderModel = self.get_object()

        try:
            getattr(work_order_model, self.action_name)(**kwargs)
        except ValidationError as e:
            messages.add_message(request,
                                 message=e.message,
                                 level=messages.ERROR,
                                 extra_tags='is-danger')
        return response


class WorkOrderModelActionMarkAsApprovedView(BaseWorkOrderActionView):
    action_name = 'mark_as_approved'

class WorkOrderModelActionMarkAsUnApprovedView(BaseWorkOrderActionView):
    action_name = 'mark_as_unapproved'
