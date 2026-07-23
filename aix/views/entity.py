"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from datetime import timedelta
from random import randint

from django.contrib.messages import add_message, ERROR
from django.db.models import Q, Count, Sum
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.timezone import localtime, localdate
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, DetailView, UpdateView, CreateView, RedirectView, DeleteView

from aix.forms.entity import EntityModelUpdateForm, EntityModelCreateForm, EntityManagementForm
from aix.io.data_generator import EntityDataGenerator
from aix.models import (EntityModel, EntityUnitModel, ItemThroughModel, TransactionModel,
                                  JournalEntryModel, PurchaseOrderModel, BillModel, CustomerModel, InvoiceModel, EstimateModel,
                                  ItemModel, VendorModel, WorkOrderJobcardModel, WorkOrderModel)

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
from aix.views.mixins import (
    QuarterlyReportMixIn, YearlyReportMixIn,
    MonthlyReportMixIn, DateReportMixIn, LoginRequiredMixIn, SessionConfigurationMixIn, EntityUnitMixIn,
    EntityDigestMixIn, UnpaidElementsMixIn, BaseDateNavigationUrlMixIn
)


# Entity CRUD Views ----
class EntityModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/entitiy_list.html'
    context_object_name = 'entities'
    PAGE_TITLE = _('My Entities')
    extra_context = {
        'header_title': PAGE_TITLE,
        'page_title': PAGE_TITLE,
        
        'hide_menu': True
    }

    def get_queryset(self):
        return EntityModel.objects.for_user(
            user_model=self.request.user)


class EntityModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/entity_create.html'
    form_class = EntityModelCreateForm
    PAGE_TITLE = _('Create Entity')
    extra_context = {
        'header_title': PAGE_TITLE,
        'page_title': PAGE_TITLE
    }

    def get_success_url(self):
        return reverse('aix:home')

    def form_valid(self, form):
        user = self.request.user
        form.instance.admin = user
        entity_model = form.save()
        default_coa = form.cleaned_data.get('default_coa')
        activate_accounts = form.cleaned_data.get('activate_all_accounts')
        if default_coa:
            entity_model.populate_default_coa(activate_accounts=activate_accounts)

        sample_data = form.cleaned_data.get('generate_sample_data')
        if sample_data:
            entity_generator = EntityDataGenerator(
                entity_model=entity_model,
                user_model=self.request.user,
                start_date=localdate() - timedelta(days=30 * 8),
                capital_contribution=50000,
                days_forward=30 * 7,
                tx_quantity=50
            )
            entity_generator.populate_entity()
        return super().form_valid(form)


class EntityModelUpdateView(LoginRequiredMixIn, UpdateView):
    context_object_name = 'entity'
    template_name = 'aix/entity_update.html'
    form_class = EntityModelUpdateForm
    slug_url_kwarg = 'entity_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.object.name
        context['header_title'] = self.object.name
        return context

    def get_success_url(self):
        return reverse('aix:entity-list')

    def get_queryset(self):
        return EntityModel.objects.for_user(user_model=self.request.user)


class EntityDeleteView(LoginRequiredMixIn, DeleteView):
    slug_url_kwarg = 'entity_slug'
    context_object_name = 'entity'
    template_name = 'aix/entity_delete.html'
    verify_descendants = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['page_title'] = _('Delete Entity ') + self.object.name
        context['header_title'] = context['page_title']
        return context

    def get_queryset(self):
        return EntityModel.objects.for_user(
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:home')

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        entity_model: EntityModel = self.get_object()

        # todo: this will need to be changed once hierarchical support is enabled.
        if self.verify_descendants:
            c = entity_model.children.count()
            if c != 0:
                add_message(request,
                            level=ERROR,
                            extra_tags='is-danger',
                            message=_('Entity has %s children. Must delete children first.' % c))
                return self.get(request, *args, **kwargs)

        ItemThroughModel.objects.for_entity(
            user_model=self.request.user,
            entity_slug=self.kwargs['entity_slug']
        ).delete()

        TransactionModel.objects.for_entity(
            user_model=self.request.user,
            entity_slug=self.kwargs['entity_slug']
        ).delete()

        return super().delete(request, *args, **kwargs)


# DASHBOARD VIEWS START ----
class EntityModelDetailView(LoginRequiredMixIn,
                            EntityUnitMixIn,
                            RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        loc_date = localdate()
        unit_slug = self.get_unit_slug()
        if unit_slug:
            return reverse('aix:unit-dashboard-month',
                           kwargs={
                               'entity_slug': self.kwargs['entity_slug'],
                               'unit_slug': unit_slug,
                               'year': loc_date.year,
                               'month': loc_date.month,
                           })
        return reverse('aix:entity-dashboard-month',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'year': loc_date.year,
                           'month': loc_date.month,
                       })


class FiscalYearEntityModelDashboardView(LoginRequiredMixIn,
                                         SessionConfigurationMixIn,
                                         BaseDateNavigationUrlMixIn,
                                         UnpaidElementsMixIn,
                                         EntityUnitMixIn,
                                         EntityDigestMixIn,
                                         YearlyReportMixIn,
                                         DetailView):
    context_object_name = 'entity'
    slug_url_kwarg = 'entity_slug'
    template_name = 'aix/entity_dashboard.html'
    DJL_NO_FROM_DATE_RAISE_404 = False
    DJL_NO_TO_DATE_RAISE_404 = False

    FETCH_UNPAID_BILLS = True
    FETCH_UNPAID_INVOICES = True

    def get_context_data(self, **kwargs):
        context = super(FiscalYearEntityModelDashboardView, self).get_context_data(**kwargs)
        entity_model: EntityModel = self.object
        context['page_title'] = entity_model.name
        context['header_title'] = entity_model.name
        context['header_subtitle'] = _('Dashboard')
        context['header_subtitle_icon'] = 'mdi:monitor-dashboard'

        unit_slug = context.get('unit_slug', self.get_unit_slug())
        KWARGS = dict(entity_slug=self.kwargs['entity_slug'])

        if unit_slug:
            KWARGS['unit_slug'] = unit_slug

        url_pointer = 'entity' if not unit_slug else 'unit'
        context['pnl_chart_id'] = f'djl-entity-pnl-chart-{randint(10000, 99999)}'
        context['pnl_chart_endpoint'] = reverse(f'aix:{url_pointer}-json-pnl',
                                                kwargs=KWARGS)
        context['payables_chart_id'] = f'djl-entity-payables-chart-{randint(10000, 99999)}'
        context['payables_chart_endpoint'] = reverse(f'aix:{url_pointer}-json-net-payables',
                                                     kwargs=KWARGS)
        context['receivables_chart_id'] = f'djl-entity-receivables-chart-{randint(10000, 99999)}'
        context['receivables_chart_endpoint'] = reverse(f'aix:{url_pointer}-json-net-receivables',
                                                        kwargs=KWARGS)


        bill_digest = {}
        bill_digest['bill_count_all'] = self.get_bill_count()
        bill_digest['bill_count_cleared'] = self.get_bill_count('cleared')
        bill_digest['bill_count_pending'] = self.get_bill_count('pending')

        bill_digest['bill_total_all'] = self.get_bill_total()
        bill_digest['bill_total_cleared'] = self.get_bill_total('cleared')
        bill_digest['bill_total_pending'] = self.get_bill_total('pending')
        
        invoice_digest = {}
        invoice_digest['invoice_count_all'] = self.get_invoice_count()
        invoice_digest['invoice_count_cleared'] = self.get_invoice_count('cleared')
        invoice_digest['invoice_count_pending'] = self.get_invoice_count('pending')

        invoice_digest['invoice_total_all'] = self.get_invoice_total()
        invoice_digest['invoice_total_cleared'] = self.get_invoice_total('cleared')
        invoice_digest['invoice_total_pending'] = self.get_invoice_total('pending')

        po_digest = {}
        po_digest['po_count_all'] = self.get_po_count()
        po_digest['po_count_cleared'] = self.get_po_count('cleared')
        po_digest['po_count_pending'] = self.get_po_count('pending')
        po_digest['po_count_received'] = self.get_po_count('received')

        po_digest['po_total_all'] = self.get_po_total()
        po_digest['po_total_cleared'] = self.get_po_total('cleared')
        po_digest['po_total_pending'] = self.get_po_total('pending')
        po_digest['po_total_received'] = self.get_po_total('received')

        jobcard_digest = {}
        jobcard_digest['jobcard_count_all'] = self.get_jcd_count()
        jobcard_digest['jobcard_count_cleared'] = self.get_jcd_count('cleared')
        jobcard_digest['jobcard_count_pending'] = self.get_jcd_count('pending')
        jobcard_digest['jobcard_count_received'] = self.get_jcd_count('received')

        jobcard_digest['jobcard_total_all'] = self.get_jcd_total()
        jobcard_digest['jobcard_total_cleared'] = self.get_jcd_total('cleared')
        jobcard_digest['jobcard_total_pending'] = self.get_jcd_total('pending')
        jobcard_digest['jobcard_total_received'] = self.get_jcd_total('received')

        fiscal_digest = {}
        fiscal_digest['customer_count_all'] = self.get_customer_count()
        fiscal_digest['vendor_count_all'] = self.get_vendor_count()
        fiscal_digest['wo_count_all'] = self.get_wo_count()
        
        fiscal_digest['bill_digest'] = bill_digest
        fiscal_digest['invoice_digest'] = invoice_digest
        fiscal_digest['po_digest'] = po_digest
        fiscal_digest['jobcard_digest'] = jobcard_digest
        context['fiscal_digest'] = fiscal_digest

        context = self.get_entity_digest(context)

        return context

    def get_fy_start_month(self) -> int:
        entity_model: EntityModel = self.object
        return entity_model.fy_start_month

    def get_queryset(self):
        """
        Returns a queryset of all Entities owned or Managed by the User.
        Queryset is annotated with user_role parameter (owned/managed).
        :return: The View queryset.
        """
        return EntityModel.objects.for_user(
            user_model=self.request.user).select_related('coa')

    def get_bill_count(self, status=None):
        entity_model: EntityModel = self.object
        bill_qs = BillModel.objects.for_entity_bills(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        bill_count = self.get_bill_counts(bill_qs, status)
        return bill_count

    def get_bill_total(self, status=None):
        entity_model: EntityModel = self.object
        bill_qs = BillModel.objects.for_entity_bills(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        bill_count = self.get_bill_totals(bill_qs, status)
        return bill_count

    def get_invoice_count(self, status=None):
        entity_model: EntityModel = self.object
        invoice_qs = InvoiceModel.objects.for_entity_invoices(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        invoice_count = self.get_invoice_counts(invoice_qs, status)
        return invoice_count

    def get_invoice_total(self, status=None):
        entity_model: EntityModel = self.object
        invoice_qs = InvoiceModel.objects.for_entity_invoices(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        invoice_count = self.get_invoice_totals(invoice_qs, status)
        return invoice_count

    def get_customer_count(self, status=None):
        entity_model: EntityModel = self.object
        customer_qs = CustomerModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        customer_count = self.get_customer_counts(customer_qs, status)
        return customer_count

    def get_vendor_count(self, status=None):
        entity_model: EntityModel = self.object
        vendor_qs = VendorModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        vendor_count = self.get_vendor_counts(vendor_qs, status)
        return vendor_count

    def get_wo_count(self, status=None):
        entity_model: EntityModel = self.object
        wo_qs = WorkOrderModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        wo_count = self.get_wo_counts(wo_qs, status)
        return wo_count
    
    def get_po_count(self, status=None):
        entity_model: EntityModel = self.object
        po_qs = PurchaseOrderModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        po_count = self.get_po_counts(po_qs, status)
        return po_count

    def get_po_total(self, status=None):
        entity_model: EntityModel = self.object
        po_qs = PurchaseOrderModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        po_count = self.get_po_totals(po_qs, status)
        return po_count
    
    def get_jcd_count(self, status=None):
        entity_model: EntityModel = self.object
        jcd_qs = WorkOrderJobcardModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        jcd_count = self.get_jcd_counts(jcd_qs, status)
        return jcd_count

    def get_jcd_total(self, status=None):
        entity_model: EntityModel = self.object
        jcd_qs = WorkOrderJobcardModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        jcd_count = self.get_jcd_totals(jcd_qs, status)
        return jcd_count

class QuarterlyEntityDashboardView(FiscalYearEntityModelDashboardView, QuarterlyReportMixIn):
    """
    Entity Quarterly Dashboard View.
    """


class MonthlyEntityDashboardView(FiscalYearEntityModelDashboardView, MonthlyReportMixIn):
    """
    Monthly Entity Dashboard View.
    """


class DateEntityDashboardView(FiscalYearEntityModelDashboardView, DateReportMixIn):
    """
    Date-specific Entity Dashboard View.
    """


# BALANCE SHEET -----------
class EntityModelBalanceSheetView(LoginRequiredMixIn, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        year = localdate().year
        return reverse('aix:entity-bs-year',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'year': year
                       })


class FiscalYearEntityModelBalanceSheetView(LoginRequiredMixIn,
                                            SessionConfigurationMixIn,
                                            BaseDateNavigationUrlMixIn,
                                            EntityUnitMixIn,
                                            YearlyReportMixIn,
                                            DetailView):
    context_object_name = 'entity'
    slug_url_kwarg = 'entity_slug'
    template_name = 'aix/balance_sheet.html'

    def get_context_data(self, **kwargs):
        context = super(FiscalYearEntityModelBalanceSheetView, self).get_context_data(**kwargs)
        context['page_title'] = _('Balance Sheet') + ': ' + self.object.name
        context['header_title'] = context['page_title']
        unit_slug = self.request.GET.get('unit')
        if unit_slug:
            context['unit_model'] = get_object_or_404(EntityUnitModel,
                                                      slug=unit_slug,
                                                      entity__slug__exact=self.kwargs['entity_slug'])
        return context

    def get_queryset(self):
        """
        Returns a queryset of all Entities owned or Managed by the User.
        Queryset is annotated with user_role parameter (owned/managed).
        :return: The View queryset.
        """
        return EntityModel.objects.for_user(user_model=self.request.user)

    def get_fy_start_month(self) -> int:
        entity_model: EntityModel = self.object
        return entity_model.fy_start_month


class QuarterlyEntityModelBalanceSheetView(QuarterlyReportMixIn, FiscalYearEntityModelBalanceSheetView):
    """
    Quarter Balance Sheet View.
    """


class MonthlyEntityModelBalanceSheetView(MonthlyReportMixIn, FiscalYearEntityModelBalanceSheetView):
    """
    Monthly Balance Sheet View.
    """


class DateEntityModelBalanceSheetView(DateReportMixIn, FiscalYearEntityModelBalanceSheetView):
    """
    Date Balance Sheet View.
    """


# INCOME STATEMENT ------------
class EntityModelIncomeStatementView(LoginRequiredMixIn, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        year = localdate().year
        return reverse('aix:entity-ic-year',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'year': year
                       })


class FiscalYearEntityModelIncomeStatementView(LoginRequiredMixIn,
                                               SessionConfigurationMixIn,
                                               BaseDateNavigationUrlMixIn,
                                               EntityUnitMixIn,
                                               YearlyReportMixIn,
                                               DetailView):
    context_object_name = 'entity'
    slug_url_kwarg = 'entity_slug'
    template_name = 'aix/income_statement.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = _('Income Statement: ') + self.object.name
        context['header_title'] = _('Income Statement: ') + self.object.name
        unit_slug = self.kwargs.get('unit_slug')
        if unit_slug:
            context['unit_model'] = get_object_or_404(EntityUnitModel,
                                                      slug__exact=unit_slug,
                                                      entity__slug__exact=self.kwargs['entity_slug'])
        return context

    def get_queryset(self):
        return EntityModel.objects.for_user(user_model=self.request.user)

    def get_fy_start_month(self) -> int:
        entity_model: EntityModel = self.object
        return entity_model.fy_start_month


class QuarterlyEntityModelIncomeStatementView(QuarterlyReportMixIn, FiscalYearEntityModelIncomeStatementView):
    """
    Quarter Income Statement View.
    """


class MonthlyEntityModelIncomeStatementView(MonthlyReportMixIn, FiscalYearEntityModelIncomeStatementView):
    """
    Monthly Income Statement View.
    """


class DateModelIncomeStatementView(DateReportMixIn, FiscalYearEntityModelIncomeStatementView):
    """
    Date Income Statement View.
    """


# ENTITY MISC VIEWS ---
# class SetDefaultEntityView(LoginRequiredMixIn, RedirectView):
#     http_method_names = ['post']
#
#     def post(self, request, *args, **kwargs):
#         form = EntityFilterForm(request.POST, user_model=request.user)
#         session_key = get_default_entity_session_key()
#         if form.is_valid():
#             entity_model = form.cleaned_data['entity_model']
#             self.url = reverse('aix:entity-dashboard',
#                                kwargs={
#                                    'entity_slug': entity_model.slug
#                                })
#             set_default_entity(request, entity_model)
#         else:
#             try:
#                 del self.request.session[session_key]
#             finally:
#                 self.url = reverse('aix:entity-list')
#         return super().post(request, *args, **kwargs)


# class SetSessionDate(LoginRequiredMixIn, RedirectView):
#     """
#     Sets the date filter on the session for a given entity.
#     """
#     http_method_names = ['post']
#
#     def post(self, request, *args, **kwargs):
#         entity_slug = kwargs['entity_slug']
#         as_of_form = AsOfDateFilterForm(data=request.POST, form_id=None)
#         # next_url = request.GET['next']
#
#         if as_of_form.is_valid():
#             as_of_form.clean()
#             end_date = as_of_form.cleaned_data['date']
#             set_session_date_filter(request, entity_slug, end_date)
#             self.url = reverse('aix:entity-dashboard-date',
#                                kwargs={
#                                    'entity_slug': self.kwargs['entity_slug'],
#                                    'year': end_date.year,
#                                    'month': end_date.month,
#                                    'day': end_date.day,
#                                })
#         return super().post(request, *args, **kwargs)



class EntityManagementModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/entity_management.html'
    context_object_name = 'entity_managements'
    PAGE_TITLE = _('EntityManagement List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EntityManagementModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EntityManagementModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/entity_management.html'
    PAGE_TITLE = _('Create New EntityManagement')
    form_class = EntityManagementForm
    context_object_name = 'entity_management'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EntityManagementForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:entity-management-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        entity_management_model: EntityManagementModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        entity_management_model.entity = entity_model
        entity_management_model.save()
        return super().form_valid(form)


class EntityManagementModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/entity_management.html'
    PAGE_TITLE = _('EntityManagement Update')
    context_object_name = 'entity_management'
    form_class = EntityManagementForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'entity_management_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return EntityManagementModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:entity-management-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class EntityManagementDeleteView(LoginRequiredMixIn, DeleteView):
    slug_url_kwarg = 'entity_slug'
    context_object_name = 'entity_management'
    template_name = 'aix/entity_management_delete.html'
    verify_descendants = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['page_title'] = _('Delete Entity MGT ') + self.object.name
        context['header_title'] = context['page_title']
        return context

    def get_queryset(self):
        return EntityManagementModel.objects.for_user(
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:home')

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        entity_management_model: EntityManagementModel = self.get_object()

        return super().delete(request, *args, **kwargs)

# ### aix ### #


class aixEntityModelDashboardView(LoginRequiredMixIn, ListView):
    template_name = 'aix/entity_dashboard_aix.html'
    context_object_name = 'entity_dashboard_aixs'
    PAGE_TITLE = _('aix List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        customer_qs = CustomerModel.objects.all()
        customer_model: CustomerModel = get_object_or_404(customer_qs, uuid__exact="f9246d4b44c440169ea3ac8e979129e0")
        
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
        return EntityModel.objects.for_user(
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
