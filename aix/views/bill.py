"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.urls import reverse

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
from xhtml2pdf import pisa 
import pandas as pd
from jinja2 import Environment, FileSystemLoader

from django.utils.html import format_html
from django.utils.timezone import localdate
from django.utils.translation import gettext_lazy as _
from django.views.generic import (UpdateView, CreateView, DeleteView,
                                  ArchiveIndexView, MonthArchiveView, YearArchiveView,
                                  DetailView, RedirectView)
from django.views.generic.detail import SingleObjectMixin

from aix.forms.bill import (BillModelCreateForm, BaseBillModelUpdateForm, DraftBillModelUpdateForm,
                                      BillItemFormset, BillModelConfigureForm, InReviewBillModelUpdateForm,
                                      ApprovedBillModelUpdateForm, AccruedAndApprovedBillModelUpdateForm,
                                      PaidBillModelUpdateForm)
from aix.models import EntityModel, PurchaseOrderModel, LedgerModel, EstimateModel, TransactionModel
from aix.models.bill import BillModel
from aix.views.mixins import LoginRequiredMixIn


class BillModelListView(LoginRequiredMixIn, ArchiveIndexView):
    template_name = 'aix/bills/bill_list.html'
    context_object_name = 'bills'
    PAGE_TITLE = _('Bill List')
    date_field = 'date'
    paginate_by = 20
    paginate_orphans = 2
    allow_empty = True
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'uil:bill'
    }

    def get_queryset(self):
        return BillModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related('vendor', 'ledger', 'ledger__entity').order_by('-updated')

    def get_allow_future(self):
        allow_future = self.request.GET.get('allow_future')
        if allow_future:
            try:
                allow_future = int(allow_future)
                if allow_future in (0, 1):
                    return bool(allow_future)
            except ValueError:
                pass
        return False


class BillModelYearListView(YearArchiveView, BillModelListView):
    paginate_by = 10
    make_object_list = True


class BillModelMonthListView(MonthArchiveView, BillModelListView):
    paginate_by = 10
    month_format = '%m'
    date_list_period = 'year'


class BillModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/bills/bill_create.html'
    PAGE_TITLE = _('Create Bill')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'uil:bill'
    }
    for_purchase_order = False
    for_estimate = False
    po_active_module = ''

    def get(self, request, entity_slug, **kwargs):
        response = super(BillModelCreateView, self).get(request, entity_slug, **kwargs)
        if self.for_estimate and 'ce_pk' in self.kwargs:
            estimate_qs = EstimateModel.objects.for_entity(
                entity_slug=entity_slug,
                user_model=self.request.user
            )
            estimate_model: EstimateModel = get_object_or_404(estimate_qs, uuid__exact=self.kwargs['ce_pk'])
            if not estimate_model.can_bind():
                return HttpResponseNotFound('404 Not Found')
        return response


    def get_context_data(self, **kwargs):
        context = super(BillModelCreateView, self).get_context_data(**kwargs)

        # todo: revisit this in case there's better way...
        if self.for_purchase_order:
            po_pk = self.kwargs['po_pk']
            po_item_uuids_qry_param = self.request.GET.get('item_uuids')
            if po_item_uuids_qry_param:
                try:
                    po_item_uuids = po_item_uuids_qry_param.split(',')
                except:
                    return HttpResponseBadRequest()
            else:
                return HttpResponseBadRequest()

            po_qs = PurchaseOrderModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            ).prefetch_related('itemthroughmodel_set')
            po_model: PurchaseOrderModel = get_object_or_404(po_qs, uuid__exact=po_pk)
            po_items = po_model.itemthroughmodel_set.filter(
                bill_model__isnull=True,
                uuid__in=po_item_uuids
            )
            context['po_model'] = po_model
            context['po_items'] = po_items
            form_action = reverse('aix:bill-create-po',
                                  kwargs={
                                      'entity_slug': self.kwargs['entity_slug'],
                                      'po_pk': po_model.uuid
                                  }) + f'?item_uuids={po_item_uuids_qry_param}'
        elif self.for_estimate:
            estimate_qs = EstimateModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
            estimate_uuid = self.kwargs['ce_pk']
            estimate_model: EstimateModel = get_object_or_404(estimate_qs, uuid__exact=estimate_uuid)
            form_action = reverse('aix:bill-create-estimate',
                                  kwargs={
                                      'entity_slug': self.kwargs['entity_slug'],
                                      'ce_pk': estimate_model.uuid
                                  })
        else:
            form_action = reverse('aix:bill-create',
                                  kwargs={
                                      'entity_slug': self.kwargs['entity_slug'],
                                  })
        context['form_action_url'] = form_action
        return context

    def get_initial(self):
        return {
            'date': localdate()
        }

    def get_form(self, form_class=None):
        entity_slug = self.kwargs['entity_slug']
        return BillModelCreateForm(entity_slug=entity_slug,
                                   user_model=self.request.user,
                                   **self.get_form_kwargs())

    def form_valid(self, form):
        bill_model: BillModel = form.save(commit=False)
        ledger_model, bill_model = bill_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            ledger_posted=False,
            user_model=self.request.user)

        if self.for_estimate:
            ce_pk = self.kwargs['ce_pk']
            estimate_model_qs = EstimateModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user)

            estimate_model = get_object_or_404(estimate_model_qs, uuid__exact=ce_pk)
            bill_model.action_bind_estimate(estimate_model=estimate_model, commit=False)

        elif self.for_purchase_order:
            po_pk = self.kwargs['po_pk']
            item_uuids = self.request.GET.get('item_uuids')
            if not item_uuids:
                return HttpResponseBadRequest()
            item_uuids = item_uuids.split(',')
            po_qs = PurchaseOrderModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
            po_model: PurchaseOrderModel = get_object_or_404(po_qs, uuid__exact=po_pk)
            self.po_active_module = po_model.po_module
            if po_model.po_date > bill_model.date:
                messages.add_message(self.request,
                                     message=f'Bill Date {bill_model.date} cannot be'
                                             f' earlier than PO Date {po_model.po_date}',
                                     level=messages.ERROR,
                                     extra_tags='is-danger')
                return self.render_to_response(self.get_context_data(form=form))

            po_model_items_qs = po_model.itemthroughmodel_set.filter(uuid__in=item_uuids)

            bill_model.update_amount_due(queryset=po_model_items_qs)
            bill_model.new_state(commit=True)
            bill_model.clean()
            bill_model.save()
            po_model_items_qs.update(bill_model=bill_model)
            # check if its initiated from purchase order
            po_force_migrate = False
            if po_model_items_qs:
                po_force_migrate = True
            bill_model.migrate_state(
                user_model=self.request.user,
                entity_slug=self.kwargs['entity_slug'],
                itemthrough_queryset=po_model_items_qs,
                force_migrate=po_force_migrate # force migration for 
            )
            return HttpResponseRedirect(self.get_success_url())
        elif self.for_estimate:
            estimate_qs = EstimateModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
            estimate_model = get_object_or_404(estimate_qs, uuid__exact=self.kwargs['ce_pk'])
            bill_model.ce_model = estimate_model
            bill_model.clean()
            bill_model.save()
            return HttpResponseRedirect(self.get_success_url())
        return super(BillModelCreateView, self).form_valid(form)

    def get_success_url(self):
        entity_slug = self.kwargs['entity_slug']
        if self.for_purchase_order:
            po_pk = self.kwargs['po_pk']
            if self.po_active_module == 'fuel':
                return reverse('aix:po-update-fuel',
                            kwargs={
                                'entity_slug': entity_slug,
                                'po_pk': po_pk
                            })
            return reverse('aix:po-update',
                           kwargs={
                               'entity_slug': entity_slug,
                               'po_pk': po_pk
                           })
        elif self.for_estimate:
            return reverse('aix:customer-estimate-detail',
                           kwargs={
                               'entity_slug': entity_slug,
                               'ce_pk': self.kwargs['ce_pk']
                           })
        bill_model: BillModel = self.object
        return reverse('aix:bill-detail',
                       kwargs={
                           'entity_slug': entity_slug,
                           'bill_pk': bill_model.uuid
                       })


class BillModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'bill_pk'
    slug_field = 'uuid'
    context_object_name = 'bill'
    template_name = 'aix/bills/bill_detail.html'
    extra_context = {
        'header_subtitle_icon': 'uil:bill',
        'hide_menu': True
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        bill_model: BillModel = self.object
        title = f'Bill {bill_model.bill_number}'
        context['page_title'] = title
        context['header_title'] = title

        bill_model: BillModel = self.object
        bill_items_qs, item_data = bill_model.get_itemthrough_data(
            queryset=bill_model.itemthroughmodel_set.all()
        )
        context['bill_items'] = bill_items_qs
        context['total_amount_due'] = item_data['amount_due']

        if not bill_model.is_configured():
            link = format_html(f"""
            <a href="{reverse("aix:bill-update", kwargs={
                'entity_slug': self.kwargs['entity_slug'],
                'bill_pk': bill_model.uuid
            })}">here</a>
            """)
            msg = f'Bill {bill_model.bill_number} has not been fully set up. ' + \
                  f'Please update or assign associated accounts {link}.'
            messages.add_message(self.request,
                                 message=msg,
                                 level=messages.WARNING,
                                 extra_tags='is-danger')
        return context

    def get_queryset(self):
        return BillModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).prefetch_related(
            'itemthroughmodel_set',
            'ledger__journal_entries__entity_unit'
        ).select_related('ledger', 'ledger__entity', 'vendor', 'cash_account', 'prepaid_account', 'unearned_account')


class BillModelUpdateView(LoginRequiredMixIn, UpdateView):
    slug_url_kwarg = 'bill_pk'
    slug_field = 'uuid'
    context_object_name = 'bill_model'
    template_name = 'aix/bills/bill_update.html'
    extra_context = {
        'header_subtitle_icon': 'uil:bill'
    }
    http_method_names = ['get', 'post']
    action_update_items = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.item_through_qs = None

    def get_item_through_queryset(self):
        bill_model: BillModel = self.object
        if not self.item_through_qs:
            self.item_through_qs = bill_model.itemthroughmodel_set.select_related(
                'item_model', 'po_model', 'bill_model').order_by('-total_amount')
        return self.item_through_qs

    def get_form(self, form_class=None):
        form_class = self.get_form_class()
        if self.request.method == 'POST' and self.action_update_items:
            return form_class(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                instance=self.object
            )
        return form_class(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
            **self.get_form_kwargs()
        )

    def get_form_class(self):
        bill_model: BillModel = self.object
        if not bill_model.is_configured():
            return BillModelConfigureForm

        if bill_model.is_draft():
            return DraftBillModelUpdateForm
        elif bill_model.is_review():
            return InReviewBillModelUpdateForm
        elif bill_model.is_approved() and not bill_model.accrue:
            return ApprovedBillModelUpdateForm
        elif bill_model.is_approved() and bill_model.accrue:
            return AccruedAndApprovedBillModelUpdateForm
        elif bill_model.is_paid():
            return PaidBillModelUpdateForm
        return BaseBillModelUpdateForm

    def get_context_data(self, *, object_list=None,
                         item_formset: BillItemFormset = None,
                         **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        bill_model: BillModel = self.object
        ledger_model = bill_model.ledger
        item_through_qs = self.get_item_through_queryset()

        title = f'Bill {bill_model.bill_number}'
        context['page_title'] = title
        context['header_title'] = title
        context['header_subtitle'] = bill_model.get_bill_status_display()

        # todo: this logic is different for bill... revisit...
        if not bill_model.is_configured():
            messages.add_message(
                request=self.request,
                message=f'Bill {bill_model.bill_number} must have all accounts configured.',
                level=messages.ERROR,
                extra_tags='is-danger'
            )

        if not bill_model.is_paid():
            if ledger_model.locked:
                messages.add_message(self.request,
                                     messages.ERROR,
                                     f'Warning! This bill is locked. Must unlock before making any changes.',
                                     extra_tags='is-danger')

        if not ledger_model.posted:
            messages.add_message(self.request,
                                 messages.INFO,
                                 f'This bill has not been posted. Must post to see ledger changes.',
                                 extra_tags='is-info')

        if not item_formset:
            _, aggregate_data = bill_model.get_itemthrough_data(
                queryset=item_through_qs
            )

            item_formset = BillItemFormset(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                bill_model=bill_model,
                queryset=item_through_qs
            )
        else:
            _, aggregate_data = bill_model.get_itemthrough_data(
                queryset=item_formset.queryset
            )

        has_po = any(i.po_model_id for i in item_through_qs)
        if has_po:
            item_formset.can_delete = False
            item_formset.has_po = has_po

        context['item_formset'] = item_formset
        context['total_amount_due'] = aggregate_data['amount_due']
        context['has_po'] = has_po
        return context

    def get_success_url(self):
        entity_slug = self.kwargs['entity_slug']
        bill_pk = self.kwargs['bill_pk']
        return reverse('aix:bill-update',
                       kwargs={
                           'entity_slug': entity_slug,
                           'bill_pk': bill_pk
                       })

    def get_queryset(self):
        return BillModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related(
            'ledger', 'ledger__entity', 'vendor', 'cash_account',
            'prepaid_account', 'unearned_account')

    def form_valid(self, form):
        form.save(commit=False)
        messages.add_message(self.request,
                             messages.SUCCESS,
                             f'Bill {self.object.bill_number} successfully updated.',
                             extra_tags='is-success')
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        response = super(BillModelUpdateView, self).get(request, *args, **kwargs)

        # this action can only be used via POST request...
        if self.action_update_items:
            return HttpResponseBadRequest()

        return response

    def post(self, request, bill_pk, entity_slug, *args, **kwargs):

        response = super(BillModelUpdateView, self).post(request, *args, **kwargs)
        bill_model: BillModel = self.object

        # todo: can this be a separate FormView view???
        if self.action_update_items:
            item_formset: BillItemFormset = BillItemFormset(request.POST,
                                                            user_model=self.request.user,
                                                            bill_model=bill_model,
                                                            entity_slug=entity_slug)

            if item_formset.is_valid():
                if item_formset.has_changed():
                    bill_items = item_formset.save(commit=False)
                    bill_qs = BillModel.objects.for_entity(
                        user_model=self.request.user,
                        entity_slug=entity_slug
                    )
                    bill_model: BillModel = get_object_or_404(bill_qs, uuid__exact=bill_pk)

                    entity_qs = EntityModel.objects.for_user(
                        user_model=self.request.user
                    )
                    entity_model: EntityModel = get_object_or_404(entity_qs, slug__exact=entity_slug)

                    for item in bill_items:
                        item.entity = entity_model
                        item.bill_model = bill_model

                    item_formset.save()
                    bill_model.update_amount_due()
                    bill_model.new_state(commit=True)
                    bill_model.clean()
                    bill_model.save(update_fields=['amount_due',
                                                   'amount_receivable',
                                                   'amount_unearned',
                                                   'amount_earned',
                                                   'markdown_notes',
                                                   'updated'])

                    bill_model.migrate_state(
                        entity_slug=entity_slug,
                        user_model=self.request.user,
                        # itemthrough_models=bill_item_list,
                        force_migrate=True
                    )

                    messages.add_message(request,
                                         message=f'Items for Invoice {bill_model.bill_number} saved.',
                                         level=messages.SUCCESS,
                                         extra_tags='is-success')

                    return HttpResponseRedirect(reverse('aix:bill-update',
                                                        kwargs={
                                                            'entity_slug': entity_slug,
                                                            'bill_pk': bill_pk
                                                        }))

            else:
                context = self.get_context_data(item_formset=item_formset)
                return self.render_to_response(context=context)

        return response


# ACTION VIEWS...
class BaseBillActionView(LoginRequiredMixIn, RedirectView, SingleObjectMixin):
    http_method_names = ['get']
    pk_url_kwarg = 'bill_pk'
    action_name = None
    commit = True

    def get_queryset(self):
        return BillModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_redirect_url(self, *args, **kwargs):
        return reverse('aix:bill-update',
                       kwargs={
                           'entity_slug': kwargs['entity_slug'],
                           'bill_pk': kwargs['bill_pk']
                       })

    def get(self, request, *args, **kwargs):
        kwargs['user_model'] = self.request.user
        if not self.action_name:
            raise ImproperlyConfigured('View attribute action_name is required.')
        response = super(BaseBillActionView, self).get(request, *args, **kwargs)
        ce_model: BillModel = self.get_object()

        try:
            getattr(ce_model, self.action_name)(commit=self.commit, **kwargs)
        except ValidationError as e:
            messages.add_message(request,
                                 message=e.message,
                                 level=messages.ERROR,
                                 extra_tags='is-danger')
        return response


class BillModelActionMarkAsDraftView(BaseBillActionView):
    action_name = 'mark_as_draft'


class BillModelActionMarkAsInReviewView(BaseBillActionView):
    action_name = 'mark_as_review'


class BillModelActionMarkAsApprovedView(BaseBillActionView):
    action_name = 'mark_as_approved'


class BillModelActionMarkAsPaidView(BaseBillActionView):
    action_name = 'mark_as_paid'


class BillModelActionDeleteView(BaseBillActionView):
    action_name = 'mark_as_delete'


class BillModelActionVoidView(BaseBillActionView):
    action_name = 'mark_as_void'


class BillModelActionLockLedgerView(BaseBillActionView):
    action_name = 'lock_ledger'


class BillModelActionUnlockLedgerView(BaseBillActionView):
    action_name = 'unlock_ledger'


class BillModelActionForceMigrateView(BaseBillActionView):
    action_name = 'migrate_state'

    def get_redirect_url(self, entity_slug, bill_pk, *args, **kwargs):
        return reverse('aix:bill-update',
                       kwargs={
                           'entity_slug': entity_slug,
                           'bill_pk': bill_pk
                       })


class BillReportView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'bill_pk'
    slug_field = 'uuid'
    context_object_name = 'bill'
    template_name = 'aix/bills/bill_detail.html'
    extra_context = {
        'header_subtitle_icon': 'uil:bill',
        'hide_menu': True
    }
    for_receipt = False
    dwn_report_file = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        bill_model: BillModel = self.object
        title = f'Bill {bill_model.bill_number}'
        context['page_title'] = title
        context['header_title'] = title

        bill_model: BillModel = self.object
        bill_items_qs, item_data = bill_model.get_itemthrough_data(
            queryset=bill_model.itemthroughmodel_set.all()
        )
        context['bill_items'] = bill_items_qs
        context['total_amount_due'] = item_data['amount_due']
        context['total_items'] = item_data['total_items']
        context['total_paid'] = item_data['total_paid']/item_data['total_items']

        txs_queryset = TransactionModel.objects.for_bill(
            bill_pk=bill_model.uuid,
            user_model=self.request.user,
            entity_slug=self.kwargs['entity_slug']
        ).select_related('journal_entry').order_by('-journal_entry__date')
        txs_queryset = txs_queryset.filter(account__code='1010')
        total_credits = sum(tx.amount for tx in txs_queryset if tx.tx_type == 'credit')
        total_debits = sum(tx.amount for tx in txs_queryset if tx.tx_type == 'debit')
        txs_cash_amount = total_credits - total_debits
        context['txs'] = txs_queryset
        context['total_debits'] = total_debits
        context['total_credits'] = total_credits
        context['txs_cash_amount'] = txs_cash_amount
        
        has_po = any(i.po_model_id for i in bill_items_qs if i.po_model_id)
        for i in bill_items_qs:
            if i.po_model_id:
                po_pk = i.po_model_id
                po_qs = PurchaseOrderModel.objects.for_entity(
                    entity_slug=self.kwargs['entity_slug'],
                    user_model=self.request.user
                )
                po_model: PurchaseOrderModel = get_object_or_404(po_qs, uuid__exact=po_pk)
                po_items_qs, item_data = po_model.get_po_item_data(
                    queryset=po_model.itemthroughmodel_set.all().select_related('item_model')
                )
                context['po_items'] = po_items_qs
                context['po_model'] = po_model
                context['po_total_amount'] = sum(
                    i['po_total_amount'] for i in po_items_qs.values(
                        'po_total_amount', 'po_item_status') if i['po_item_status'] != 'cancelled')

        if has_po:
            context['has_po'] = has_po

        if not bill_model.is_configured():
            link = format_html(f"""
            <a href="{reverse("aix:bill-update", kwargs={
                'entity_slug': self.kwargs['entity_slug'],
                'bill_pk': bill_model.uuid
            })}">here</a>
            """)
            msg = f'Bill {bill_model.bill_number} has not been fully set up. ' + \
                  f'Please update or assign associated accounts {link}.'
            messages.add_message(self.request,
                                 message=msg,
                                 level=messages.WARNING,
                                 extra_tags='is-danger')
        return context

    def get_queryset(self):
        return BillModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).prefetch_related(
            'itemthroughmodel_set',
            'ledger__journal_entries__entity_unit'
        ).select_related('ledger', 'ledger__entity', 'vendor', 'cash_account', 'prepaid_account', 'unearned_account')

    
    def get(self, request, *args, **kwargs):
        response = super(BillReportView, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        if self.dwn_report_file:
            # data = CustomerModel.objects.all().order_by('customer_name')
            open('aix/templates/aix/reports/temp.html', "w").write(render_to_string('aix/reports/result.html', {'data': context}))

            # Converting the HTML template into a PDF file
            #pdf = self.html_to_pdf('aix/templates/aix/reports/temp.html', data)
            
            # customer_qs = data.values('customer_name', 'email')
            # df = pd.DataFrame(customer_qs)
            
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template("aix/templates/aix/reports/bill_rpt.html")
            if self.for_receipt:
                template = env.get_template("aix/templates/aix/reports/vendor_receipt_rpt.html")
            # template = get_template(template_src)
            # context_dict = {"title" : "Customers Report - List"}
            # context_dict['data'] = data
            data = context['bill_items'].values('bill_model__bill_number', 'bill_model')
            df = pd.DataFrame(data)
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