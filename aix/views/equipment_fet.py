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
from django.forms import modelformset_factory
from aix.forms.equipment_fet import (EquipmentFetModelCreateForm, BaseEquipmentFetModelUpdateForm,
                                                DraftEquipmentFetModelUpdateForm, ReviewEquipmentFetModelUpdateForm,
                                                ApprovedEquipmentFetModelUpdateForm, get_fet_item_formset, get_fet_item_formset2, EquipmentFetItemForm,BaseEquipmentFetItemFormset)
from aix.models import WorkOrderModel, EquipmentFetModel, ItemFetThroughModel, EstimateModel, EquipmentModel, WorkOrderAssetModel
from aix.views.mixins import LoginRequiredMixIn


class EquipmentFetModelListView(LoginRequiredMixIn, ArchiveIndexView):
    template_name = 'aix/app/operations/intrafield/fet_list.html'
    context_object_name = 'fet_list'
    PAGE_TITLE = _('FET List')
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

            return EquipmentFetModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                work_order=work_order_model
            ).order_by('-created')

        return EquipmentFetModel.objects.for_entity(
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
        context = super(EquipmentFetModelListView, self).get_context_data(**kwargs)
        
        context['form_action_url'] = reverse('aix:fet-list',
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


class EquipmentFetModelYearListView(YearArchiveView, EquipmentFetModelListView):
    paginate_by = 10
    make_object_list = True


class EquipmentFetModelMonthListView(MonthArchiveView, EquipmentFetModelListView):
    paginate_by = 10
    month_format = '%m'
    date_list_period = 'year'


class EquipmentFetModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/intrafield/fet_create.html'
    PAGE_TITLE = _('Create Jobcard')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'uil:invoice'
    }
    for_work_order = False

    def get(self, request, entity_slug, **kwargs):
        response = super(EquipmentFetModelCreateView, self).get(request, entity_slug, **kwargs)
        if self.for_work_order and 'work_order_pk' in self.kwargs:
            wo_qs = WorkOrderModel.objects.for_entity(
                entity_slug=entity_slug,
                user_model=self.request.user
            )
            work_order_model: WorkOrderModel = get_object_or_404(wo_qs, uuid__exact=self.kwargs['work_order_pk'])
        return response

    def get_context_data(self, **kwargs):
        context = super(EquipmentFetModelCreateView, self).get_context_data(**kwargs)

        if self.for_work_order:
            context['form_action_url'] = reverse('aix:fet-create-work-order',
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
        
        else:
            context['form_action_url'] = reverse('aix:fet-create',
                                                 kwargs={
                                                     'entity_slug': self.kwargs['entity_slug']
                                                 })
        return context

    def get_form(self, form_class=None):
        entity_slug = self.kwargs['entity_slug']
        form = EquipmentFetModelCreateForm(entity_slug=entity_slug,
                                            user_model=self.request.user,
                                            **self.get_form_kwargs())
        # asset_qs = AssetModel.objects.filter()
        return form

    def form_valid(self, form):
        fet_model: EquipmentFetModel = form.save(commit=False)
        fet_model = fet_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user)

        if self.for_work_order:
            work_order_pk = self.kwargs['work_order_pk']
            wo_qs = WorkOrderModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user)
            work_order_model = get_object_or_404(wo_qs, uuid__exact=work_order_pk)
            fet_model.work_order = work_order_model
        fet_model.save()
        # equipment_qs = EquipmentModel.objects.all()
        asset_qs = WorkOrderAssetModel.objects.filter(work_order_id=work_order_pk)
        print(asset_qs.count(), 'N')
        equipment_qs = EquipmentModel.objects.filter(asset__in=asset_qs.values_list('asset_id', flat=True))
        print(equipment_qs.count(), 'D')

        for emp in equipment_qs:
            print(fet_model.fet_date)
            item_model = ItemFetThroughModel(equipment_model=emp,
                            attendance_date=fet_model.fet_date, 
                            attendance_code='OH',
                            fet_model=fet_model)
            item_model.save()

            # fet, item = ItemFetThroughModel.objects.update_or_create(
            #             defaults={
            #                 'attendance_date': fet_model.fet_date,
            #                 'attendance_code': 'A'
            #             }
            #         )


        return super().form_valid(form=form)

    def get_success_url(self):
        entity_slug = self.kwargs['entity_slug']

        if self.for_work_order:
            work_order_pk = self.kwargs['work_order_pk']
            return reverse('aix:fet-list',
                           kwargs={
                               'entity_slug': self.kwargs['entity_slug'],
                               'work_order_pk': work_order_pk
                           })

        return reverse('aix:fet-list',
                       kwargs={
                           'entity_slug': entity_slug
                       })


class EquipmentFetModelUpdateView(LoginRequiredMixIn, UpdateView):
    slug_url_kwarg = 'fet_pk'
    slug_field = 'uuid'
    context_object_name = 'fet_model'
    template_name = 'aix/app/operations/intrafield/fet_update.html'
    extra_context = {
        'header_subtitle_icon': 'uil:invoice'
    }
    update_items = False
    fet_model = None

    def post(self, request, entity_slug, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        fet_model: EquipmentFetModel = self.object
        if self.update_items:
            EquipmentFetItemFormset = get_fet_item_formset(fet_model)
            fet_item_formset: EquipmentFetItemFormset = EquipmentFetItemFormset(request.POST,
                                                                                 user_model=self.request.user,
                                                                                 fet_model=fet_model,
                                                                                 entity_slug=entity_slug)

            context = self.get_context_data(item_formset=fet_item_formset)
            # print(fet_model.uuid)

            # todo: revisit this workflow and conform to API
            if fet_item_formset.is_valid():
                if fet_item_formset.has_changed():

                    fet_items = fet_item_formset.save(commit=False)
                    create_invoice_uuids = [
                        str(i['uuid'].uuid) for i in fet_item_formset.cleaned_data if i and i['create_invoice'] is True
                    ]

                    if create_invoice_uuids:
                        item_uuids = ','.join(create_invoice_uuids)
                        redirect_url = reverse(
                            'aix:invoice-create-fet',
                            kwargs={
                                'entity_slug': self.kwargs['entity_slug'],
                                'fet_pk': fet_model.uuid,
                            }
                        )
                        redirect_url += f'?item_uuids={item_uuids}'
                        return HttpResponseRedirect(redirect_url)
                    
                    fet_count = fet_items.count(1)
                    for item in fet_items:
                        if not item.fet_model_id:
                            item.fet_model = fet_model
                        # if item.attendance_date is None:
                        #     item.attendance_date = fet_model.fet_date
                        # print(item.fet_unit_cost)
                        # item.fet_item_status = 'not_ordered'
                        # item.attendance_date = fet_model.fet_date
                    fet_item_formset.save()
                    # todo: check that update state methods are accepting queryset from formsets...
                    # fet_model.update_fet_state(item_queryset=fet_item_formset.queryset)
                    fet_model.clean()
                    fet_model.save(update_fields=['fet_date',
                                                 'fet_status',
                                                 'updated'])
            # return self.render_to_response(context)
            return HttpResponseRedirect(self.get_success_url())
        return response

    def get_form(self, form_class=None):
        fet_model: EquipmentFetModel = self.object
        if fet_model.is_draft():
            return DraftEquipmentFetModelUpdateForm(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                **self.get_form_kwargs()
            )
        elif fet_model.is_review():
            return ReviewEquipmentFetModelUpdateForm(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                **self.get_form_kwargs()
            )
        elif fet_model.is_approved():
            return ApprovedEquipmentFetModelUpdateForm(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                **self.get_form_kwargs()
            )
        return BaseEquipmentFetModelUpdateForm(
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
        return super(EquipmentFetModelUpdateView, self).get_form_kwargs()

    def get_context_data(self, *, object_list=None, item_formset=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        fet_model: EquipmentFetModel = self.object
        title = f'Jobcard {fet_model.code}'
        context['page_title'] = title
        context['header_title'] = title
        if not item_formset:
            # fet_item_queryset, item_data = fet_model.get_fet_item_data(
            #     queryset=fet_model.itemfetthroughmodel_set.select_related('fet_model').order_by(
            #         'created'
            #     )
            # )
            # fet_item_queryset, item_data = fet_model.get_fet_staff_data(
            #     queryset=EquipmentModel.objects.all().select_related('entity').order_by(
            #         'created'
            #     )
            # )
            print(fet_model.uuid)
            # fet_item_queryset = EquipmentModel.objects.all().select_related('entity').order_by(
            #         'created'
            #     )
            # work_order_pk = fet_model.work_order
            # wo_qs = WorkOrderModel.objects.for_entity(
            #     entity_slug=self.kwargs['entity_slug'],
            #     user_model=self.request.user)
            # work_order_model = get_object_or_404(wo_qs, uuid__exact=work_order_pk)
            asset_qs = WorkOrderAssetModel.objects.filter(work_order_id=fet_model.work_order.uuid)  
            print(asset_qs.count(), 'asset')
            for emp in EquipmentModel.objects.filter(asset__in=asset_qs.values_list('asset', flat=True)):
                print(emp.reg_no, emp.asset)
            initial_data = [{'attendance_code': 'OH',
                            'equipment_model': emp} for emp in EquipmentModel.objects.filter(asset__in=asset_qs.values_list('asset_id', flat=True))]
            EquipmentFetItemFormset = get_fet_item_formset2(fet_model)
            context['item_formset'] = EquipmentFetItemFormset(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                fet_model=fet_model,
                # queryset=fet_item_queryset,
                initial=initial_data,
                # extra=len(initial_data)
            )
            # print(len(initial_data), 'met')
            # fet_item_queryset, item_data = fet_model.get_fet_item_data(
            #     queryset=fet_model.itemfetthroughmodel_set.select_related('fet_model').order_by(
            #         'created'
            #     )
            # )
            # context['item_formset']=fet_item_queryset
            # context['total_amount_due'] = item_data['amount_due']
            # context['total_paid'] = item_data['total_paid']
        else:
            context['item_formset'] = item_formset
            # context['total_amount_due'] = fet_model.fet_amount
            # fet_item_queryset = EquipmentModel.objects.all().select_related('entity').order_by(
            #         'created'
            #     )
            fet_item_queryset, item_data = fet_model.get_fet_item_data(
                queryset=fet_model.itemfetthroughmodel_set.filter(fet_model_id=fet_model.uuid).select_related('fet_model').order_by(
                    'created'
                )
            )
            # context['total_amount_due'] = item_data['amount_due']
            # context['total_paid'] = item_data['total_paid']
        return context
        
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        qty = self.request.GET.get('qty', None)
        qs = EquipmentModel.objects.all()
        if qty:
            qs = qs.filter(qty=qty)
        # kwargs['extra'] = qty
        return kwargs

    def get_success_url(self):
        entity_slug = self.kwargs['entity_slug']
        fet_pk = self.kwargs['fet_pk']
        return reverse('aix:fet-detail',
                       kwargs={
                           'entity_slug': entity_slug,
                           'fet_pk': fet_pk
                       })

    def get_queryset(self):
        return EquipmentFetModel.objects.filter(
            entity__slug=self.kwargs['entity_slug'],
            # user=self.request.user,
            # work_order=self.work_order.uuid
        ).select_related('entity')
        # return EquipmentFetModel.objects.for_entity(
        #     entity_slug=self.kwargs['entity_slug'],
        #     user_model=self.request.user
        # ).select_related('entity')

    def form_valid(self, form: BaseEquipmentFetModelUpdateForm):
        fet_model: EquipmentFetModel = form.save(commit=False)

        if form.has_changed():
            fet_items_qs = ItemFetThroughModel.objects.for_fet(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                fet_pk=fet_model.uuid,
            ).select_related('fet_model')

            if all(['fet_status' in form.changed_data,
                    fet_model.fet_status == fet_model.FET_STATUS_FULFILLED]):
                fet_items_qs.update(fet_item_status=ItemFetThroughModel.FET_STATUS_CANCELED)
            fet_items_qs.update(attendance_date=fet_model.fet_date)
        # print('mex')

        messages.add_message(self.request,
                             messages.SUCCESS,
                             f'{self.object.code} successfully updated.',
                             extra_tags='is-success')

        return super().form_valid(form)
    
    # def get(self, request, *args, **kwargs):
    #     if id in kwargs.keys():
    #         equipment = EquipmentModel.objects.get(id=kwargs.get('id'))
    #     else:
    #         equipment = None
            
    #     # fet_form = BaseEquipmentFetModelUpdateForm(instance=equipment)
    #     # fet_model: EquipmentFetModel = self.object
    #     # EquipmentFetItemFormset = get_fet_item_formset(equipment)
    #     ReadOnlyEquipmentFetItemFormset = modelformset_factory(
    #         model=ItemFetThroughModel,
    #         form=EquipmentFetItemForm,
    #         formset=BaseEquipmentFetItemFormset,
    #         queryset=equipment
    #     )
    #     context['item_formset'] = EquipmentFetItemFormset(
    #         entity_slug=self.kwargs['entity_slug'],
    #         user_model=self.request.user,
    #         fet_model=self.fet_model,
    #         instance=equipment,
    #     )
    #     return (request, self.template_name, context)



class EquipmentFetModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'fet_pk'
    slug_field = 'uuid'
    context_object_name = 'fet_model'
    template_name = 'aix/app/operations/intrafield/fet_detail.html'
    extra_context = {
        'header_subtitle_icon': 'uil:invoice',
        'hide_menu': True
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        fet_model: EquipmentFetModel = self.object
        title = f'Code {fet_model.code}'
        context['page_title'] = title
        context['header_title'] = title

        fet_model: EquipmentFetModel = self.object
        fet_items_qs, item_data = fet_model.get_fet_item_data(
            queryset=fet_model.itemfetthroughmodel_set.filter(fet_model_id=fet_model.uuid).select_related('equipment_model')
        )
        context['fet_items'] = fet_items_qs

        # fet_item_queryset, item_data = fet_model.get_fet_item_data(
        #     queryset=fet_model.itemFetthroughmodel_set.select_related('fet_model').order_by(
        #         'created'
        #     )
        # )
        return context

    def get_queryset(self):
        return EquipmentFetModel.objects.filter(
            entity__slug=self.kwargs['entity_slug'],
            # user=self.request.user,
            # work_order=self.work_order.uuid
        ).select_related('entity')
        # return EquipmentFetModel.objects.for_entity(
        #     entity_slug=self.kwargs['entity_slug'],
        #     user_model=self.request.user,
        #     # work_order=self.work_order.uuid
        # ).select_related('entity')


class EquipmentFetModelDeleteView(LoginRequiredMixIn, DeleteView):
    slug_url_kwarg = 'fet_pk'
    slug_field = 'uuid'
    context_object_name = 'fet_model'
    template_name = 'aix/app/operations/intrafield/fet_delete.html'
    extra_context = {
        'hide_menu': True,
        'header_subtitle_icon': 'uil:invoice'
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        fet_model: EquipmentFetModel = self.object
        context['page_title'] = _('Delete Jobcard ') + fet_model.code
        context['header_title'] = context['page_title']
        return context

    def get_queryset(self):
        return EquipmentFetModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:entity-dashboard',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                       })

    def delete(self, request, *args, **kwargs):
        fet_model: EquipmentFetModel = self.get_object()
        self.object = fet_model
        fet_items_qs = fet_model.itemfetthroughmodel_set.filter(invoice_model__isnull=False)
        if fet_items_qs.exists():
            messages.add_message(request,
                                 message=f'Cannot delete {fet_model.code} because it has related invoices.',
                                 level=messages.ERROR,
                                 extra_tags='is-danger')
            url = reverse('aix:fet-update',
                          kwargs={
                              'entity_slug': self.kwargs['entity_slug'],
                              'fet_pk': self.kwargs['fet_pk']
                          })
            return HttpResponseRedirect(url)
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


# ACTIONS...
class BaseEquipmentFetActionActionView(LoginRequiredMixIn, RedirectView, SingleObjectMixin):
    http_method_names = ['get']
    pk_url_kwarg = 'fet_pk'
    action_name = None
    commit = True

    def get_queryset(self):
        return EquipmentFetModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_redirect_url(self, entity_slug, fet_pk, *args, **kwargs):
        return reverse('aix:fet-update',
                       kwargs={
                           'entity_slug': entity_slug,
                           'fet_pk': fet_pk
                       })

    def get(self, request, *args, **kwargs):
        kwargs['user_model'] = self.request.user
        if not self.action_name:
            raise ImproperlyConfigured('View attribute action_name is required.')
        response = super(BaseEquipmentFetActionActionView, self).get(request, *args, **kwargs)
        # fet_model: EquipmentFetModel = self.get_object()
        fet_qs = EquipmentFetModel.objects.all()
        fet_model: EquipmentFetModel = get_object_or_404(fet_qs, uuid=self.kwargs['fet_pk'])

        try:
            getattr(fet_model, self.action_name)(commit=self.commit, **kwargs)
        except ValidationError as e:
            messages.add_message(request,
                                 message=e.message,
                                 level=messages.ERROR,
                                 extra_tags='is-danger')
        return response


class EquipmentFetMarkAsDraftView(BaseEquipmentFetActionActionView):
    action_name = 'mark_as_draft'


class EquipmentFetMarkAsReviewView(BaseEquipmentFetActionActionView):
    action_name = 'mark_as_review'


class EquipmentFetMarkAsApprovedView(BaseEquipmentFetActionActionView):
    action_name = 'mark_as_approved'


class EquipmentFetMarkAsFulfilledView(BaseEquipmentFetActionActionView):
    action_name = 'mark_as_fulfilled'


class EquipmentFetMarkAsCanceledView(BaseEquipmentFetActionActionView):
    action_name = 'mark_as_canceled'


class EquipmentFetMarkAsVoidView(BaseEquipmentFetActionActionView):
    action_name = 'mark_as_void'

# Reports

class EquipmentFetReportView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'fet_pk'
    slug_field = 'uuid'
    context_object_name = 'fet_model'
    template_name = 'aix/app/operations/intrafield/fet_detail.html'
    extra_context = {
        'header_subtitle_icon': 'uil:invoice',
        'hide_menu': True
    }
    dwn_report_file = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        fet_model: EquipmentFetModel = self.object
        title = f'FET {fet_model.code}'
        context['page_title'] = title
        context['header_title'] = title

        fet_model: EquipmentFetModel = self.object
        fet_items_qs, item_data = fet_model.get_fet_item_data(
            queryset=fet_model.itemfetthroughmodel_set.all().select_related('equipment_model')
        )
        context['customer'] = fet_model.work_order.customer
        context['fet_items'] = fet_items_qs

        fet_item_queryset, item_data = fet_model.get_fet_item_data(
            queryset=fet_model.itemfetthroughmodel_set.select_related('fet_model').order_by(
                'created'
            )
        )
        days_in_june = [f"{day}" for day in range(1, 31)]  # June has 30 days
        # Create a DataFrame with one row and each day as a column
        df = pd.DataFrame([[''] * len(days_in_june)], columns=days_in_june, index=fet_items_qs.values_list('equipment_model__reg_no', flat=True)) 
        # Iterate through the queryset and fill the DataFrame
        for row_index, fet_item in enumerate(fet_items_qs):
            for col_index, day in enumerate(days_in_june):
                if fet_item.attendance_date:
                    if fet_item.attendance_date.day == int(day):
                        # Check if the day is in the DataFrame's columns
                        # if str(index) in df.columns:
                            # Set the value for that day
                        df.at[fet_item.equipment_model.reg_no, str(day)] = fet_item.attendance_code
                        print(fet_item.attendance_code, day, fet_item.equipment_model.reg_no)

        df['H'] = (df == 'H').sum(axis=1)
        df['S'] = (df == 'S').sum(axis=1)
        df['OH'] = (df == 'OH').sum(axis=1)
        df['R'] = (df == 'R').sum(axis=1)  
        df['MOB'] = (df == 'MOB').sum(axis=1)
        df['DMB'] = (df == 'DMB').sum(axis=1)
        df['NOS'] = (df == 'NOS').sum(axis=1)
        df['OPS'] = (df == 'OPS').sum(axis=1)
        df['ES'] = (df == 'ES').sum(axis=1)
        # subtotal = (df == 'H').sum(axis=1) + (df == 'S').sum(axis=1) + (df == 'OH').sum(axis=1)
        # df.loc['Subtotal'] = subtotal
        # grand_total = (df == 'R').sum().sum()
        # df.loc['Grand_Total'] = [''] * (df.shape[1] - 1) + [grand_total]
        total_columns = ['H', 'S', 'OH', 'R', 'MOB', 'DMB', 'NOS', 'OPS', 'ES']
        blank_row = {col: '' for col in df.columns}
        for col in total_columns:
            blank_row[col] = df[col].sum()
            # df['P_count'] = df[total_columns].sum(axis=1)
        # Create a blank row with grand total only in 'P_count'
        # blank_row['R'] = grand_total
        # for col in df.columns:
        # df = df.append(blank_row, ignore_index=True)
        grand_total_row = pd.DataFrame([blank_row], index=['Grand_Total'])
        df = pd.concat([df, grand_total_row], ignore_index=False)
        # df = pd.concat([df, pd.DataFrame([blank_row])], ignore_index=False)
        df.index = df.index.map(lambda i: 'Grand_Total' if i == len(df) - 1 else str(i))

        context['fet_items_df'] = df.to_html(classes='table')
        return context

    def get_queryset(self):
        return EquipmentFetModel.objects.filter(
            entity__slug=self.kwargs['entity_slug'],
            # user=self.request.user,
            # work_order=self.work_order.uuid
        ).select_related('entity')
        # return EquipmentFetModel.objects.for_entity(
        #     entity_slug=self.kwargs['entity_slug'],
        #     user_model=self.request.user
        # ).select_related('entity')

    def get(self, request, *args, **kwargs):
        response = super(EquipmentFetReportView, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        if self.dwn_report_file:
            # data = CustomerModel.objects.all().order_by('customer_name')
            open('aix/templates/aix/reports/temp.html', "w").write(render_to_string('aix/reports/result.html', {'data': context}))

            # Converting the HTML template into a PDF file
            #pdf = self.html_to_pdf('aix/templates/aix/reports/temp.html', data)
            
            # customer_qs = data.values('customer_name', 'email')
            # df = pd.DataFrame(customer_qs)
            
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template("aix/templates/aix/reports/fet_rpt.html")
            # template = get_template(template_src)
            # context_dict = {"title" : "Customers Report - List"}
            # context_dict['data'] = data
            data = context['fet_items'].values('fet_model__code')
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