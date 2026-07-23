"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from aix.forms.customer import CustomerModelForm
from aix.models.customer import CustomerModel
from aix.models.work_order import WorkOrderModel
from aix.models.work_order_jobcard import WorkOrderJobcardModel

from aix.models.entity import EntityModel
from aix.models.invoice import InvoiceModel
from aix.views.mixins import LoginRequiredMixIn


class CustomerModelListADVView(LoginRequiredMixIn,
                            ListView):
    template_name = 'aix/advanced/customer/customer-list.html'
    PAGE_TITLE = _('Customer List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'dashicons:businesswoman',
        'is_advanced': True
    }
    context_object_name = 'customers'

    def get_queryset(self):
        return CustomerModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class CustomerModelListView(LoginRequiredMixIn,
                            ListView):
    template_name = 'aix/customer_list.html'
    PAGE_TITLE = _('Customer List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'dashicons:businesswoman'
    }
    context_object_name = 'customers'

    def get_queryset(self):
        return CustomerModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')

class CustomerModelCreateView(LoginRequiredMixIn,
                              CreateView):
    template_name = 'aix/customer_create.html'
    PAGE_TITLE = _('Create New Customer')
    form_class = CustomerModelForm
    context_object_name = 'customer'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'dashicons:businesswoman'
    }

    def get_queryset(self):
        return CustomerModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:customer-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        customer_model: CustomerModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        customer_model.entity = entity_model
        customer_model.save()
        return super().form_valid(form)


class CustomerModelUpdateView(LoginRequiredMixIn,
                              UpdateView):
    template_name = 'aix/customer_update.html'
    PAGE_TITLE = _('Customer Update')
    form_class = CustomerModelForm
    context_object_name = 'customer'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'dashicons:businesswoman'
    }
    slug_url_kwarg = 'customer_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return CustomerModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:customer-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# todo: add CustomerDeleteView


class CustomerModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'customer_pk'
    slug_field = 'uuid'
    context_object_name = 'customer'
    #template_name = 'aix/advanced/customer/customer_detail.html'
    template_name = 'aix/app/clients/details/client_details.html'
    extra_context = {
        'hide_menu': True
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        customer_model: CustomerModel = self.object
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
        
        invoice_qs = InvoiceModel.objects.for_customer_detail(
                entity_slug=self.kwargs['entity_slug'],
                customer=customer_model
            )
        jcd_qs = WorkOrderJobcardModel.objects.for_customer(
                entity_slug=self.kwargs['entity_slug'],
                customer=customer_model
            )
        wo_qs = jcd_qs.select_related('work_order')
        wo_customer_qs = WorkOrderModel.objects.for_customer(
                entity_slug=self.kwargs['entity_slug'],
                customer=customer_model
            )
            
        wo_digest = {}
        wo_digest['wo_qs'] = wo_qs
        wo_digest['wo_customer_qs'] = wo_customer_qs
        wo_digest['jcd_qs'] = jcd_qs
        wo_digest['invoices'] = invoice_qs
        context['wo_digest'] = wo_digest

        customer_forms = {}
        context['customer_forms'] = customer_forms
        
        return context

    def get_queryset(self):
        return CustomerModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_incoice_list(self, cust):
        return InvoiceModel.objects.for_customer(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
            customer=cust
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

    # def get_invoice_amount_paid(self, invoice_model: InvoiceModel):
    #     amt_paid = 0
    #     amt_paid_values = invoice_model.for_txs(
    #         entity_slug=self.kwargs['entity_slug'],
    #         user_model=self.request.user,
    #         invoice_model=invoice_model
    #         )
        
    #     #if amt_paid_values.length > 0:
    #     amt_paid = sum(amt.amount for amt in amt_paid_values)
    #     return amt_paid