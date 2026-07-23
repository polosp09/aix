"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""
from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.urls import reverse

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
from xhtml2pdf import pisa 
import pandas as pd
from jinja2 import Environment, FileSystemLoader

from django.utils.translation import gettext_lazy as _
from django.views.generic import (CreateView, ArchiveIndexView, YearArchiveView, MonthArchiveView, DetailView,
                                  UpdateView, DeleteView, RedirectView)
from django.views.generic.detail import SingleObjectMixin

from aix.forms.purchase_order import (PurchaseOrderModelCreateForm, BasePurchaseOrderModelUpdateForm,
                                                DraftPurchaseOrderModelUpdateForm, ReviewPurchaseOrderModelUpdateForm,
                                                ApprovedPurchaseOrderModelUpdateForm, get_po_item_formset, get_po_fuel_item_formset)
from aix.models import PurchaseOrderModel, ItemThroughModel, EstimateModel
from aix.views.mixins import LoginRequiredMixIn


class PurchaseOrderModelListView(LoginRequiredMixIn, ArchiveIndexView):
    template_name = 'aix/purchase_order/po_list.html'
    context_object_name = 'po_list'
    PAGE_TITLE = _('PO List')
    date_field = 'created'
    paginate_by = 10
    paginate_orphans = 2
    allow_empty = True
    po_active_module = ''
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'uil:bill'
    }

    def get_queryset(self):
        qs = PurchaseOrderModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-created')
        if self.po_active_module == 'fuel':
            qs = qs.filter(po_module=self.po_active_module)
        return qs

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

    def get_context_data(self, **kwargs):
        context = super(PurchaseOrderModelListView, self).get_context_data(**kwargs)
        if self.po_active_module == 'fuel':
            context['po_active_module'] = self.po_active_module
        return context


class PurchaseOrderModelYearListView(YearArchiveView, PurchaseOrderModelListView):
    paginate_by = 10
    make_object_list = True


class PurchaseOrderModelMonthListView(MonthArchiveView, PurchaseOrderModelListView):
    paginate_by = 10
    month_format = '%m'
    date_list_period = 'year'


class PurchaseOrderModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/purchase_order/po_create.html'
    PAGE_TITLE = _('Create Purchase Order')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'uil:bill'
    }
    for_estimate = False
    po_active_module = ''

    def get(self, request, entity_slug, **kwargs):
        response = super(PurchaseOrderModelCreateView, self).get(request, entity_slug, **kwargs)
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
        context = super(PurchaseOrderModelCreateView, self).get_context_data(**kwargs)

        if self.for_estimate:
            context['form_action_url'] = reverse('aix:po-create-estimate',
                                                 kwargs={
                                                     'entity_slug': self.kwargs['entity_slug'],
                                                     'ce_pk': self.kwargs['ce_pk']
                                                 })
            estimate_qs = EstimateModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            ).select_related('customer')
            estimate_model = get_object_or_404(estimate_qs, uuid__exact=self.kwargs['ce_pk'])
            context['estimate_model'] = estimate_model

        elif self.po_active_module == 'fuel':
            context['po_active_module'] = self.po_active_module
            context['header_title'] = 'Create Fuel Order'
            context['form_action_url'] = reverse('aix:po-create-fuel',
                                                 kwargs={
                                                     'entity_slug': self.kwargs['entity_slug']
                                                 })
        else:
            context['form_action_url'] = reverse('aix:po-create',
                                                 kwargs={
                                                     'entity_slug': self.kwargs['entity_slug']
                                                 })
        return context

    def get_form(self, form_class=None):
        entity_slug = self.kwargs['entity_slug']
        form = PurchaseOrderModelCreateForm(entity_slug=entity_slug,
                                            user_model=self.request.user,
                                            **self.get_form_kwargs())
        return form

    def form_valid(self, form):
        po_model: PurchaseOrderModel = form.save(commit=False)
        po_model = po_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user)

        if self.po_active_module == 'fuel':
            po_model.po_module = self.po_active_module
        if self.for_estimate:
            ce_pk = self.kwargs['ce_pk']
            estimate_model_qs = EstimateModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user)

            estimate_model = get_object_or_404(estimate_model_qs, uuid__exact=ce_pk)
            po_model.action_bind_estimate(estimate_model=estimate_model, commit=False)
        return super().form_valid(form=form)

    def get_success_url(self):
        entity_slug = self.kwargs['entity_slug']

        if self.for_estimate:
            ce_pk = self.kwargs['ce_pk']
            return reverse('aix:customer-estimate-detail',
                           kwargs={
                               'entity_slug': self.kwargs['entity_slug'],
                               'ce_pk': ce_pk
                           })
        if self.po_active_module == 'fuel':
            return reverse('aix:po-list-fuel',
                           kwargs={
                               'entity_slug': entity_slug
                           })
        return reverse('aix:po-list',
                       kwargs={
                           'entity_slug': entity_slug
                       })


class PurchaseOrderModelUpdateView(LoginRequiredMixIn, UpdateView):
    slug_url_kwarg = 'po_pk'
    slug_field = 'uuid'
    context_object_name = 'po_model'
    template_name = 'aix/purchase_order/po_update.html'
    extra_context = {
        'header_subtitle_icon': 'uil:bill'
    }
    update_items = False
    po_active_module = ''

    def post(self, request, entity_slug, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        po_model: PurchaseOrderModel = self.object
        if self.update_items:
            PurchaseOrderItemFormset = get_po_item_formset(po_model)
            # check if fuel module is selected
            if po_model.is_module_fuel():
                PurchaseOrderItemFormset = get_po_fuel_item_formset(po_model)
                po_item_formset: PurchaseOrderItemFormset = PurchaseOrderItemFormset(request.POST,
                                                                                    user_model=self.request.user,
                                                                                    po_model=po_model,
                                                                                    entity_slug=entity_slug)
            else:
                po_item_formset: PurchaseOrderItemFormset = PurchaseOrderItemFormset(request.POST,
                                                                                    user_model=self.request.user,
                                                                                    po_model=po_model,
                                                                                    entity_slug=entity_slug)


            context = self.get_context_data(item_formset=po_item_formset)

            # todo: revisit this workflow and conform to API
            if po_item_formset.is_valid():
                if po_item_formset.has_changed():

                    po_items = po_item_formset.save(commit=False)
                    create_bill_uuids = [
                        str(i['uuid'].uuid) for i in po_item_formset.cleaned_data if i and i['create_bill'] is True
                    ]

                    if create_bill_uuids:
                        item_uuids = ','.join(create_bill_uuids)
                        redirect_url = reverse(
                            'aix:bill-create-po',
                            kwargs={
                                'entity_slug': self.kwargs['entity_slug'],
                                'po_pk': po_model.uuid,
                            }
                        )
                        redirect_url += f'?item_uuids={item_uuids}'
                        return HttpResponseRedirect(redirect_url)

                    for item in po_items:
                        if not item.po_model_id:
                            item.po_model = po_model
                    po_item_formset.save()
                    # todo: check that update state methods are accepting queryset from formsets...
                    po_model.update_po_state(item_queryset=po_item_formset.queryset)
                    po_model.clean()
                    po_model.save(update_fields=['po_amount',
                                                 'po_amount_received',
                                                 'updated'])
                
                if po_model.is_module_fuel():
                    redirect_url = redirect_url = reverse(
                        'aix:po-update-fuel',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'po_pk': po_model.uuid,
                        }
                    )
            return self.render_to_response(context)
        return response

    def get_form(self, form_class=None):
        po_model: PurchaseOrderModel = self.object
        if po_model.is_draft():
            return DraftPurchaseOrderModelUpdateForm(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                **self.get_form_kwargs()
            )
        elif po_model.is_review():
            return ReviewPurchaseOrderModelUpdateForm(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                **self.get_form_kwargs()
            )
        elif po_model.is_approved():
            return ApprovedPurchaseOrderModelUpdateForm(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                **self.get_form_kwargs()
            )
        return BasePurchaseOrderModelUpdateForm(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
            **self.get_form_kwargs()
        )

    def get_form_kwargs(self):
        if self.update_items:
            return {
                'initial': self.get_initial(),
                'prefix': self.get_prefix(),
                'instance': self.object
            }
        return super(PurchaseOrderModelUpdateView, self).get_form_kwargs()

    def get_context_data(self, *, object_list=None, item_formset=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        po_model: PurchaseOrderModel = self.object
        title = f'Purchase Order {po_model.po_number}'
        context['page_title'] = title
        context['header_title'] = title
        context['po_active_module'] = self.po_active_module
        if not item_formset:
            po_item_queryset, item_data = po_model.get_po_item_data(
                queryset=po_model.itemthroughmodel_set.select_related('bill_model', 'po_model').order_by(
                    'created'
                )
            )
            # PurchaseOrderItemFormset = get_po_item_formset(po_model)
            # if po_model.can_fuel(self.po_active_module):
            PurchaseOrderItemFormset = get_po_fuel_item_formset(po_model)

            context['item_formset'] = PurchaseOrderItemFormset(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                po_model=po_model,
                queryset=po_item_queryset,
            )
            context['total_amount_due'] = item_data['amount_due']
            context['total_paid'] = item_data['total_paid']
        else:
            context['item_formset'] = item_formset
            context['total_amount_due'] = po_model.po_amount
        return context

    def get_success_url(self):
        entity_slug = self.kwargs['entity_slug']
        po_pk = self.kwargs['po_pk']
        if self.po_active_module == 'fuel':
            return reverse('aix:po-detail-fuel',
                        kwargs={
                            'entity_slug': entity_slug,
                            'po_pk': po_pk
                        })
        return reverse('aix:po-detail',
                       kwargs={
                           'entity_slug': entity_slug,
                           'po_pk': po_pk
                       })

    def get_queryset(self):
        return PurchaseOrderModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related('entity')

    def form_valid(self, form: BasePurchaseOrderModelUpdateForm):
        po_model: PurchaseOrderModel = form.save(commit=False)

        if form.has_changed():
            po_items_qs = ItemThroughModel.objects.for_po(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                po_pk=po_model.uuid,
            ).select_related('bill_model')

            if all(['po_status' in form.changed_data,
                    po_model.po_status == po_model.PO_STATUS_APPROVED]):
                po_items_qs.update(po_item_status=ItemThroughModel.STATUS_NOT_ORDERED)

            if 'fulfilled' in form.changed_data:

                if not all([i.bill_model for i in po_items_qs]):
                    messages.add_message(self.request,
                                         messages.ERROR,
                                         f'All PO items must be billed before marking'
                                         f' PO: {po_model.po_number} as fulfilled.',
                                         extra_tags='is-danger')
                    return self.get(self.request)

                else:
                    if not all([i.bill_model.is_paid() for i in po_items_qs]):
                        messages.add_message(self.request,
                                             messages.SUCCESS,
                                             f'All bills must be paid before marking'
                                             f' PO: {po_model.po_number} as fulfilled.',
                                             extra_tags='is-success')
                        return self.get(self.request)

                po_items_qs.update(po_item_status=ItemThroughModel.STATUS_RECEIVED)

        messages.add_message(self.request,
                             messages.SUCCESS,
                             f'{self.object.po_number} successfully updated.',
                             extra_tags='is-success')

        return super().form_valid(form)


class PurchaseOrderModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'po_pk'
    slug_field = 'uuid'
    context_object_name = 'po_model'
    template_name = 'aix/purchase_order/po_detail.html'
    extra_context = {
        'header_subtitle_icon': 'uil:bill',
        'hide_menu': True
    }
    po_active_module = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        po_model: PurchaseOrderModel = self.object
        title = f'Purchase Order {po_model.po_number}'
        context['page_title'] = title
        context['header_title'] = title

        po_model: PurchaseOrderModel = self.object
        po_items_qs, item_data = po_model.get_po_item_data(
            queryset=po_model.itemthroughmodel_set.all().select_related('item_model')
        )
        context['po_items'] = po_items_qs
        context['po_total_amount'] = sum(
            i['po_total_amount'] for i in po_items_qs.values(
                'po_total_amount', 'po_item_status') if i['po_item_status'] != 'cancelled')
        
        po_item_queryset, item_data = po_model.get_po_item_data(
            queryset=po_model.itemthroughmodel_set.select_related('bill_model', 'po_model').order_by(
                'created'
            )
        )
        context['total_amount_due'] = item_data['amount_due']
        context['total_paid'] = item_data['total_paid']
        if self.po_active_module == 'fuel':
            context['po_active_module'] = self.po_active_module
        return context

    def get_queryset(self):
        return PurchaseOrderModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related('ce_model', 'entity')


class PurchaseOrderModelDeleteView(LoginRequiredMixIn, DeleteView):
    slug_url_kwarg = 'po_pk'
    slug_field = 'uuid'
    context_object_name = 'po_model'
    template_name = 'aix/purchase_order/po_delete.html'
    extra_context = {
        'hide_menu': True,
        'header_subtitle_icon': 'uil:bill'
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        po_model: PurchaseOrderModel = self.object
        context['page_title'] = _('Delete Purchase Order ') + po_model.po_number
        context['header_title'] = context['page_title']
        return context

    def get_queryset(self):
        return PurchaseOrderModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:entity-dashboard',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                       })

    def delete(self, request, *args, **kwargs):
        po_model: PurchaseOrderModel = self.get_object()
        self.object = po_model
        po_items_qs = po_model.itemthroughmodel_set.filter(bill_model__isnull=False)
        if po_items_qs.exists():
            messages.add_message(request,
                                 message=f'Cannot delete {po_model.po_number} because it has related bills.',
                                 level=messages.ERROR,
                                 extra_tags='is-danger')
            url = reverse('aix:po-update',
                          kwargs={
                              'entity_slug': self.kwargs['entity_slug'],
                              'po_pk': self.kwargs['po_pk']
                          })
            return HttpResponseRedirect(url)
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


# ACTIONS...
class BasePurchaseOrderActionActionView(LoginRequiredMixIn, RedirectView, SingleObjectMixin):
    http_method_names = ['get']
    pk_url_kwarg = 'po_pk'
    action_name = None
    commit = True

    def get_queryset(self):
        return PurchaseOrderModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_redirect_url(self, entity_slug, po_pk, *args, **kwargs):
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

    def get(self, request, *args, **kwargs):
        kwargs['user_model'] = self.request.user
        if not self.action_name:
            raise ImproperlyConfigured('View attribute action_name is required.')
        response = super(BasePurchaseOrderActionActionView, self).get(request, *args, **kwargs)
        po_model: PurchaseOrderModel = self.get_object()

        try:
            getattr(po_model, self.action_name)(commit=self.commit, **kwargs)
        except ValidationError as e:
            messages.add_message(request,
                                 message=e.message,
                                 level=messages.ERROR,
                                 extra_tags='is-danger')
        return response


class PurchaseOrderMarkAsDraftView(BasePurchaseOrderActionActionView):
    action_name = 'mark_as_draft'
    po_active_module = ''


class PurchaseOrderMarkAsReviewView(BasePurchaseOrderActionActionView):
    action_name = 'mark_as_review'
    po_active_module = ''


class PurchaseOrderMarkAsApprovedView(BasePurchaseOrderActionActionView):
    action_name = 'mark_as_approved'
    po_active_module = ''


class PurchaseOrderMarkAsFulfilledView(BasePurchaseOrderActionActionView):
    action_name = 'mark_as_fulfilled'
    po_active_module = ''


class PurchaseOrderMarkAsCanceledView(BasePurchaseOrderActionActionView):
    action_name = 'mark_as_canceled'
    po_active_module = ''


class PurchaseOrderMarkAsVoidView(BasePurchaseOrderActionActionView):
    action_name = 'mark_as_void'
    po_active_module = ''


class PurchaseOrderReportView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'po_pk'
    slug_field = 'uuid'
    context_object_name = 'po_model'
    template_name = 'aix/purchase_order/po_detail.html'
    extra_context = {
        'header_subtitle_icon': 'uil:bill',
        'hide_menu': True
    }
    po_active_module = ''
    dwn_report_file = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        po_model: PurchaseOrderModel = self.object
        title = f'Purchase Order {po_model.po_number}'
        context['page_title'] = title
        context['header_title'] = title

        po_model: PurchaseOrderModel = self.object
        po_items_qs, item_data = po_model.get_po_item_data(
            queryset=po_model.itemthroughmodel_set.all().select_related('item_model')
        )
        context['po_items'] = po_items_qs
        context['po_total_amount'] = sum(
            i['po_total_amount'] for i in po_items_qs.values(
                'po_total_amount', 'po_item_status') if i['po_item_status'] != 'cancelled')
        
        po_item_queryset, item_data = po_model.get_po_item_data(
            queryset=po_model.itemthroughmodel_set.select_related('bill_model', 'po_model').order_by(
                'created'
            )
        )
        context['total_amount_due'] = item_data['amount_due']
        context['total_paid'] = item_data['total_paid']
        if self.po_active_module == 'fuel':
            context['po_active_module'] = self.po_active_module
        return context

    def get_queryset(self):
        return PurchaseOrderModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related('ce_model', 'entity')

    def get(self, request, *args, **kwargs):
        response = super(PurchaseOrderReportView, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        if self.dwn_report_file:
            # data = CustomerModel.objects.all().order_by('customer_name')
            open('aix/templates/aix/reports/temp.html', "w").write(render_to_string('aix/reports/result.html', {'data': context}))

            # Converting the HTML template into a PDF file
            #pdf = self.html_to_pdf('aix/templates/aix/reports/temp.html', data)
            
            # customer_qs = data.values('customer_name', 'email')
            # df = pd.DataFrame(customer_qs)
            
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template("aix/templates/aix/reports/po_rpt.html")
            # template = get_template(template_src)
            # context_dict = {"title" : "Customers Report - List"}
            # context_dict['data'] = data
            data = context['po_items'].values('po_model__po_number', 'invoice_model')
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