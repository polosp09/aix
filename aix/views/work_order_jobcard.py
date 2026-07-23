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

from aix.forms.work_order_jobcard import (WorkOrderJobcardModelCreateForm, BaseWorkOrderJobcardModelUpdateForm,
                                                DraftWorkOrderJobcardModelUpdateForm, ReviewWorkOrderJobcardModelUpdateForm,
                                                ApprovedWorkOrderJobcardModelUpdateForm, get_jcd_item_formset)
from aix.models import WorkOrderModel, WorkOrderJobcardModel, ItemThroughModel, EstimateModel
from aix.views.mixins import LoginRequiredMixIn


class WorkOrderJobcardModelListView(LoginRequiredMixIn, ArchiveIndexView):
    template_name = 'aix/app/operations/jobcard/jcd_list.html'
    context_object_name = 'jcd_list'
    PAGE_TITLE = _('JOBCARD List')
    date_field = 'created'
    paginate_by = 10
    paginate_orphans = 2
    allow_empty = True
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'uil:invoice'
    }

    def get_queryset(self):
        if 'work_order_pk' in self.kwargs:
            work_order_qs = WorkOrderModel.objects.for_entity(
                    entity_slug=self.kwargs['entity_slug'],
                    user_model=self.request.user
                ).select_related('entity')
            work_order_model: WorkOrderModel = get_object_or_404(work_order_qs, uuid__exact=self.kwargs['work_order_pk'])

            return WorkOrderJobcardModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                work_order=work_order_model
            ).order_by('-created')

        return WorkOrderJobcardModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-created')

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
        context = super(WorkOrderJobcardModelListView, self).get_context_data(**kwargs)
        
        context['form_action_url'] = reverse('aix:jcd-list',
                                                kwargs={
                                                    'entity_slug': self.kwargs['entity_slug'],
                                                    'work_order_pk': self.kwargs['work_order_pk']
                                                })
        work_order_qs = WorkOrderModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related('customer')
        work_order_model = get_object_or_404(work_order_qs, uuid__exact=self.kwargs['work_order_pk'])
        context['work_order'] = work_order_model
        return context


class WorkOrderJobcardModelYearListView(YearArchiveView, WorkOrderJobcardModelListView):
    paginate_by = 10
    make_object_list = True


class WorkOrderJobcardModelMonthListView(MonthArchiveView, WorkOrderJobcardModelListView):
    paginate_by = 10
    month_format = '%m'
    date_list_period = 'year'


class WorkOrderJobcardModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/jobcard/jcd_create.html'
    PAGE_TITLE = _('Create Jobcard')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'uil:invoice'
    }
    for_work_order = False
    for_estimate = False

    def get(self, request, entity_slug, **kwargs):
        response = super(WorkOrderJobcardModelCreateView, self).get(request, entity_slug, **kwargs)
        if self.for_work_order and 'work_order_pk' in self.kwargs:
            wo_qs = WorkOrderModel.objects.for_entity(
                entity_slug=entity_slug,
                user_model=self.request.user
            )
            work_order_model: WorkOrderModel = get_object_or_404(wo_qs, uuid__exact=self.kwargs['work_order_pk'])
        return response

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
        context = super(WorkOrderJobcardModelCreateView, self).get_context_data(**kwargs)

        if self.for_work_order:
            context['form_action_url'] = reverse('aix:jcd-create-work-order',
                                                 kwargs={
                                                     'entity_slug': self.kwargs['entity_slug'],
                                                     'work_order_pk': self.kwargs['work_order_pk']
                                                 })
            work_order_qs = WorkOrderModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            ).select_related('customer')
            work_order_model = get_object_or_404(work_order_qs, uuid__exact=self.kwargs['work_order_pk'])
            context['work_order_model'] = work_order_model
        
        elif self.for_estimate:
            context['form_action_url'] = reverse('aix:jcd-create-estimate',
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

        else:
            context['form_action_url'] = reverse('aix:jcd-create',
                                                 kwargs={
                                                     'entity_slug': self.kwargs['entity_slug']
                                                 })
        return context

    def get_form(self, form_class=None):
        entity_slug = self.kwargs['entity_slug']
        form = WorkOrderJobcardModelCreateForm(entity_slug=entity_slug,
                                            user_model=self.request.user,
                                            **self.get_form_kwargs())
        return form

    def form_valid(self, form):
        jcd_model: WorkOrderJobcardModel = form.save(commit=False)
        jcd_model = jcd_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user)

        if self.for_work_order:
            work_order_pk = self.kwargs['work_order_pk']
            wo_qs = WorkOrderModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user)
            work_order_model = get_object_or_404(wo_qs, uuid__exact=work_order_pk)
            jcd_model.work_order = work_order_model

        elif self.for_estimatesx:
            ce_pk = self.kwargs['ce_pk']
            estimate_model_qs = EstimateModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user)

            estimate_model = get_object_or_404(estimate_model_qs, uuid__exact=ce_pk)
            jcd_model.action_bind_estimate(estimate_model=estimate_model, commit=False)
        return super().form_valid(form=form)

    def get_success_url(self):
        entity_slug = self.kwargs['entity_slug']

        if self.for_work_order:
            work_order_pk = self.kwargs['work_order_pk']
            return reverse('aix:jcd-list',
                           kwargs={
                               'entity_slug': self.kwargs['entity_slug'],
                               'work_order_pk': work_order_pk
                           })

        elif self.for_estimate:
            ce_pk = self.kwargs['ce_pk']
            return reverse('aix:customer-estimate-detail',
                           kwargs={
                               'entity_slug': self.kwargs['entity_slug'],
                               'ce_pk': ce_pk
                           })
        return reverse('aix:jcd-list',
                       kwargs={
                           'entity_slug': entity_slug
                       })


class WorkOrderJobcardModelUpdateView(LoginRequiredMixIn, UpdateView):
    slug_url_kwarg = 'jcd_pk'
    slug_field = 'uuid'
    context_object_name = 'jcd_model'
    template_name = 'aix/app/operations/jobcard/jcd_update.html'
    extra_context = {
        'header_subtitle_icon': 'uil:invoice'
    }
    update_items = False

    def post(self, request, entity_slug, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        jcd_model: WorkOrderJobcardModel = self.object
        if self.update_items:
            WorkOrderJobcardItemFormset = get_jcd_item_formset(jcd_model)
            jcd_item_formset: WorkOrderJobcardItemFormset = WorkOrderJobcardItemFormset(request.POST,
                                                                                 user_model=self.request.user,
                                                                                 jcd_model=jcd_model,
                                                                                 entity_slug=entity_slug)

            context = self.get_context_data(item_formset=jcd_item_formset)

            # todo: revisit this workflow and conform to API
            if jcd_item_formset.is_valid():
                if jcd_item_formset.has_changed():

                    jcd_items = jcd_item_formset.save(commit=False)
                    create_invoice_uuids = [
                        str(i['uuid'].uuid) for i in jcd_item_formset.cleaned_data if i and i['create_invoice'] is True
                    ]

                    if create_invoice_uuids:
                        item_uuids = ','.join(create_invoice_uuids)
                        redirect_url = reverse(
                            'aix:invoice-create-jcd',
                            kwargs={
                                'entity_slug': self.kwargs['entity_slug'],
                                'jcd_pk': jcd_model.uuid,
                            }
                        )
                        redirect_url += f'?item_uuids={item_uuids}'
                        return HttpResponseRedirect(redirect_url)
                    
                    jcd_count = jcd_items.count(1)
                    for item in jcd_items:
                        if not item.jcd_model_id:
                            item.jcd_model = jcd_model
                        print(item.jcd_unit_cost)
                        # item.jcd_item_status = 'not_ordered'
                    jcd_item_formset.save()
                    # todo: check that update state methods are accepting queryset from formsets...
                    jcd_model.update_jcd_state(item_queryset=jcd_item_formset.queryset)
                    jcd_model.clean()
                    jcd_model.save(update_fields=['jcd_amount',
                                                 'jcd_amount_received',
                                                 'jcd_status',
                                                 'jcd_date',
                                                 'updated'])
            return self.render_to_response(context)
        return response

    def get_form(self, form_class=None):
        jcd_model: WorkOrderJobcardModel = self.object
        if jcd_model.is_draft():
            return DraftWorkOrderJobcardModelUpdateForm(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                **self.get_form_kwargs()
            )
        elif jcd_model.is_review():
            return ReviewWorkOrderJobcardModelUpdateForm(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                **self.get_form_kwargs()
            )
        elif jcd_model.is_approved():
            return ApprovedWorkOrderJobcardModelUpdateForm(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                **self.get_form_kwargs()
            )
        return BaseWorkOrderJobcardModelUpdateForm(
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
        return super(WorkOrderJobcardModelUpdateView, self).get_form_kwargs()

    def get_context_data(self, *, object_list=None, item_formset=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        jcd_model: WorkOrderJobcardModel = self.object
        title = f'Jobcard {jcd_model.jcd_number}'
        context['page_title'] = title
        context['header_title'] = title
        if not item_formset:
            jcd_item_queryset, item_data = jcd_model.get_jcd_item_data(
                queryset=jcd_model.itemthroughmodel_set.select_related('invoice_model', 'jcd_model').order_by(
                    'created'
                )
            )
            WorkOrderJobcardItemFormset = get_jcd_item_formset(jcd_model)
            context['item_formset'] = WorkOrderJobcardItemFormset(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                jcd_model=jcd_model,
                queryset=jcd_item_queryset,
            )
            context['total_amount_due'] = item_data['amount_due']
            context['total_paid'] = item_data['total_paid']
        else:
            context['item_formset'] = item_formset
            context['total_amount_due'] = jcd_model.jcd_amount
            jcd_item_queryset, item_data = jcd_model.get_jcd_item_data(
                queryset=jcd_model.itemthroughmodel_set.select_related('invoice_model', 'jcd_model').order_by(
                    'created'
                )
            )
            context['total_amount_due'] = item_data['amount_due']
            context['total_paid'] = item_data['total_paid']
        return context

    def get_success_url(self):
        entity_slug = self.kwargs['entity_slug']
        jcd_pk = self.kwargs['jcd_pk']
        return reverse('aix:jcd-detail',
                       kwargs={
                           'entity_slug': entity_slug,
                           'jcd_pk': jcd_pk
                       })

    def get_queryset(self):
        return WorkOrderJobcardModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related('entity')

    def form_valid(self, form: BaseWorkOrderJobcardModelUpdateForm):
        jcd_model: WorkOrderJobcardModel = form.save(commit=False)

        if form.has_changed():
            jcd_items_qs = ItemThroughModel.objects.for_jcd(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                jcd_pk=jcd_model.uuid,
            ).select_related('invoice_model')

            if all(['jcd_status' in form.changed_data,
                    jcd_model.jcd_status == jcd_model.JCD_STATUS_APPROVED]):
                jcd_items_qs.update(jcd_item_status=ItemThroughModel.STATUS_ORDERED)

            if 'fulfilled' in form.changed_data:

                if not all([i.invoice_model for i in jcd_items_qs]):
                    messages.add_message(self.request,
                                         messages.ERROR,
                                         f'All JOBCARD items must be invoiced before x marking'
                                         f' PO: {jcd_model.jcd_number} as fulfilled.',
                                         extra_tags='is-danger')
                    return self.get(self.request)

                else:
                    if not all([i.invoice_model.is_paid() for i in jcd_items_qs]):
                        messages.add_message(self.request,
                                             messages.SUCCESS,
                                             f'All invoices must be paid before marking'
                                             f' PO: {jcd_model.jcd_number} as fulfilled.',
                                             extra_tags='is-success')
                        return self.get(self.request)

                jcd_items_qs.update(jcd_item_status=ItemThroughModel.STATUS_RECEIVED)

        messages.add_message(self.request,
                             messages.SUCCESS,
                             f'{self.object.jcd_number} successfully updated.',
                             extra_tags='is-success')

        return super().form_valid(form)


class WorkOrderJobcardModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'jcd_pk'
    slug_field = 'uuid'
    context_object_name = 'jcd_model'
    template_name = 'aix/app/operations/jobcard/jcd_detail.html'
    extra_context = {
        'header_subtitle_icon': 'uil:invoice',
        'hide_menu': True
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        jcd_model: WorkOrderJobcardModel = self.object
        title = f'Jobcard {jcd_model.jcd_number}'
        context['page_title'] = title
        context['header_title'] = title

        jcd_model: WorkOrderJobcardModel = self.object
        jcd_items_qs, item_data = jcd_model.get_jcd_item_data(
            queryset=jcd_model.itemthroughmodel_set.all().select_related('item_model')
        )
        context['jcd_items'] = jcd_items_qs
        context['jcd_total_amount'] = sum(
            i['jcd_total_amount'] for i in jcd_items_qs.values(
                'jcd_total_amount', 'jcd_item_status') if i['jcd_item_status'] != 'cancelled')

        jcd_item_queryset, item_data = jcd_model.get_jcd_item_data(
            queryset=jcd_model.itemthroughmodel_set.select_related('invoice_model', 'jcd_model').order_by(
                'created'
            )
        )
        context['total_amount_due'] = item_data['amount_due']
        if item_data['total_paid'] == None:
            context['total_paid'] = item_data['total_paid']
        elif item_data['total_items'] > 1 and item_data['total_paid'] > 0:
            context['total_paid'] = item_data['total_paid'] / item_data['total_items']
        else:
            context['total_paid'] = item_data['total_paid']
        return context

    def get_queryset(self):
        return WorkOrderJobcardModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related('entity')


class WorkOrderJobcardModelDeleteView(LoginRequiredMixIn, DeleteView):
    slug_url_kwarg = 'jcd_pk'
    slug_field = 'uuid'
    context_object_name = 'jcd_model'
    template_name = 'aix/app/operations/jobcard/jcd_delete.html'
    extra_context = {
        'hide_menu': True,
        'header_subtitle_icon': 'uil:invoice'
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        jcd_model: WorkOrderJobcardModel = self.object
        context['page_title'] = _('Delete Jobcard ') + jcd_model.jcd_number
        context['header_title'] = context['page_title']
        return context

    def get_queryset(self):
        return WorkOrderJobcardModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:entity-dashboard',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                       })

    def delete(self, request, *args, **kwargs):
        jcd_model: WorkOrderJobcardModel = self.get_object()
        self.object = jcd_model
        jcd_items_qs = jcd_model.itemthroughmodel_set.filter(invoice_model__isnull=False)
        if jcd_items_qs.exists():
            messages.add_message(request,
                                 message=f'Cannot delete {jcd_model.jcd_number} because it has related invoices.',
                                 level=messages.ERROR,
                                 extra_tags='is-danger')
            url = reverse('aix:jcd-update',
                          kwargs={
                              'entity_slug': self.kwargs['entity_slug'],
                              'jcd_pk': self.kwargs['jcd_pk']
                          })
            return HttpResponseRedirect(url)
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


# ACTIONS...
class BaseWorkOrderJobcardActionActionView(LoginRequiredMixIn, RedirectView, SingleObjectMixin):
    http_method_names = ['get']
    pk_url_kwarg = 'jcd_pk'
    action_name = None
    commit = True

    def get_queryset(self):
        return WorkOrderJobcardModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_redirect_url(self, entity_slug, jcd_pk, *args, **kwargs):
        return reverse('aix:jcd-update',
                       kwargs={
                           'entity_slug': entity_slug,
                           'jcd_pk': jcd_pk
                       })

    def get(self, request, *args, **kwargs):
        kwargs['user_model'] = self.request.user
        if not self.action_name:
            raise ImproperlyConfigured('View attribute action_name is required.')
        response = super(BaseWorkOrderJobcardActionActionView, self).get(request, *args, **kwargs)
        jcd_model: WorkOrderJobcardModel = self.get_object()

        try:
            getattr(jcd_model, self.action_name)(commit=self.commit, **kwargs)
        except ValidationError as e:
            messages.add_message(request,
                                 message=e.message,
                                 level=messages.ERROR,
                                 extra_tags='is-danger')
        return response


class WorkOrderJobcardMarkAsDraftView(BaseWorkOrderJobcardActionActionView):
    action_name = 'mark_as_draft'


class WorkOrderJobcardMarkAsReviewView(BaseWorkOrderJobcardActionActionView):
    action_name = 'mark_as_review'


class WorkOrderJobcardMarkAsApprovedView(BaseWorkOrderJobcardActionActionView):
    action_name = 'mark_as_approved'


class WorkOrderJobcardMarkAsFulfilledView(BaseWorkOrderJobcardActionActionView):
    action_name = 'mark_as_fulfilled'


class WorkOrderJobcardMarkAsCanceledView(BaseWorkOrderJobcardActionActionView):
    action_name = 'mark_as_canceled'


class WorkOrderJobcardMarkAsVoidView(BaseWorkOrderJobcardActionActionView):
    action_name = 'mark_as_void'

# Reports

class WorkOrderJobcardReportView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'jcd_pk'
    slug_field = 'uuid'
    context_object_name = 'jcd_model'
    template_name = 'aix/app/operations/jobcard/jcd_detail.html'
    extra_context = {
        'header_subtitle_icon': 'uil:invoice',
        'hide_menu': True
    }
    dwn_report_file = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        jcd_model: WorkOrderJobcardModel = self.object
        title = f'Jobcard {jcd_model.jcd_number}'
        context['page_title'] = title
        context['header_title'] = title

        jcd_model: WorkOrderJobcardModel = self.object
        jcd_items_qs, item_data = jcd_model.get_jcd_item_data(
            queryset=jcd_model.itemthroughmodel_set.all().select_related('item_model')
        )
        context['customer'] = jcd_model.work_order.customer
        context['jcd_items'] = jcd_items_qs
        context['jcd_total_amount'] = sum(
            i['jcd_total_amount'] for i in jcd_items_qs.values(
                'jcd_total_amount', 'jcd_item_status') if i['jcd_item_status'] != 'cancelled')

        jcd_item_queryset, item_data = jcd_model.get_jcd_item_data(
            queryset=jcd_model.itemthroughmodel_set.select_related('invoice_model', 'jcd_model').order_by(
                'created'
            )
        )
        context['total_amount_due'] = item_data['amount_due']
        if item_data['total_paid'] == None:
            context['total_paid'] = item_data['total_paid']
        elif item_data['total_items'] > 1 and item_data['total_paid'] > 0:
            context['total_paid'] = item_data['total_paid'] / item_data['total_items']
        else:
            context['total_paid'] = item_data['total_paid']
        return context

    def get_queryset(self):
        return WorkOrderJobcardModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related('entity')

    def get(self, request, *args, **kwargs):
        response = super(WorkOrderJobcardReportView, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        if self.dwn_report_file:
            # data = CustomerModel.objects.all().order_by('customer_name')
            open('aix/templates/aix/reports/temp.html', "w").write(render_to_string('aix/reports/result.html', {'data': context}))

            # Converting the HTML template into a PDF file
            #pdf = self.html_to_pdf('aix/templates/aix/reports/temp.html', data)
            
            # customer_qs = data.values('customer_name', 'email')
            # df = pd.DataFrame(customer_qs)
            
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template("aix/templates/aix/reports/jcd_rpt.html")
            # template = get_template(template_src)
            # context_dict = {"title" : "Customers Report - List"}
            # context_dict['data'] = data
            data = context['jcd_items'].values('jcd_model__jcd_number', 'invoice_model')
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