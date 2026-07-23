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
from aix.forms.employee_faw import (EmployeeFawModelCreateForm, BaseEmployeeFawModelUpdateForm,
                                                DraftEmployeeFawModelUpdateForm, ReviewEmployeeFawModelUpdateForm,
                                                ApprovedEmployeeFawModelUpdateForm, get_faw_item_formset, get_faw_item_formset2, EmployeeFawItemForm,BaseEmployeeFawItemFormset)
from aix.models import WorkOrderModel, WorkOrderPersonnelModel, EmployeeFawModel, ItemFawThroughModel, EstimateModel, EmployeeModel
from aix.views.mixins import LoginRequiredMixIn


class EmployeeFawModelListView(LoginRequiredMixIn, ArchiveIndexView):
    template_name = 'aix/app/operations/intrafield/faw_list.html'
    context_object_name = 'faw_list'
    PAGE_TITLE = _('FAW List')
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

            return EmployeeFawModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                work_order=work_order_model
            ).order_by('-created')

        return EmployeeFawModel.objects.for_entity(
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
        context = super(EmployeeFawModelListView, self).get_context_data(**kwargs)
        
        context['form_action_url'] = reverse('aix:faw-list',
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


class EmployeeFawModelYearListView(YearArchiveView, EmployeeFawModelListView):
    paginate_by = 10
    make_object_list = True


class EmployeeFawModelMonthListView(MonthArchiveView, EmployeeFawModelListView):
    paginate_by = 10
    month_format = '%m'
    date_list_period = 'year'


class EmployeeFawModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/intrafield/faw_create.html'
    PAGE_TITLE = _('Create Jobcard')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'uil:invoice'
    }
    for_work_order = False

    def get(self, request, entity_slug, **kwargs):
        response = super(EmployeeFawModelCreateView, self).get(request, entity_slug, **kwargs)
        if self.for_work_order and 'work_order_pk' in self.kwargs:
            wo_qs = WorkOrderModel.objects.for_entity(
                entity_slug=entity_slug,
                user_model=self.request.user
            )
            work_order_model: WorkOrderModel = get_object_or_404(wo_qs, uuid__exact=self.kwargs['work_order_pk'])
        return response

    def get_context_data(self, **kwargs):
        context = super(EmployeeFawModelCreateView, self).get_context_data(**kwargs)

        if self.for_work_order:
            context['form_action_url'] = reverse('aix:faw-create-work-order',
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
            context['form_action_url'] = reverse('aix:faw-create',
                                                 kwargs={
                                                     'entity_slug': self.kwargs['entity_slug']
                                                 })
        return context

    def get_form(self, form_class=None):
        entity_slug = self.kwargs['entity_slug']
        form = EmployeeFawModelCreateForm(entity_slug=entity_slug,
                                            user_model=self.request.user,
                                            **self.get_form_kwargs())
        return form

    def form_valid(self, form):
        faw_model: EmployeeFawModel = form.save(commit=False)
        faw_model = faw_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user)

        if self.for_work_order:
            work_order_pk = self.kwargs['work_order_pk']
            wo_qs = WorkOrderModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user)
            work_order_model = get_object_or_404(wo_qs, uuid__exact=work_order_pk)
            faw_model.work_order = work_order_model
        faw_model.save()
        employee_qs = WorkOrderPersonnelModel.objects.filter(work_order_id=faw_model.work_order.uuid)  
        personnel_qs = [{'attendance_code': 'A',
                        'employee_model': emp} for emp in EmployeeModel.objects.filter(pk__in=employee_qs.values_list('employee_id', flat=True))]

        persons = []
        for personnel in personnel_qs:
            persons.append(personnel['employee_model'].uuid)

        for emp in persons:
            # print(faw_model.faw_date)
            item_model = ItemFawThroughModel(employee_model_id=emp,
                            attendance_date=faw_model.faw_date, 
                            attendance_code='A',
                            faw_model=faw_model)
            item_model.save()

            # faw, item = ItemFawThroughModel.objects.update_or_create(
            #             defaults={
            #                 'attendance_date': faw_model.faw_date,
            #                 'attendance_code': 'A'
            #             }
            #         )


        return super().form_valid(form=form)

    def get_success_url(self):
        entity_slug = self.kwargs['entity_slug']

        if self.for_work_order:
            work_order_pk = self.kwargs['work_order_pk']
            return reverse('aix:faw-list',
                           kwargs={
                               'entity_slug': self.kwargs['entity_slug'],
                               'work_order_pk': work_order_pk
                           })

        return reverse('aix:faw-list',
                       kwargs={
                           'entity_slug': entity_slug
                       })


class EmployeeFawModelUpdateView(LoginRequiredMixIn, UpdateView):
    slug_url_kwarg = 'faw_pk'
    slug_field = 'uuid'
    context_object_name = 'faw_model'
    template_name = 'aix/app/operations/intrafield/faw_update.html'
    extra_context = {
        'header_subtitle_icon': 'uil:invoice'
    }
    update_items = False
    faw_model = None

    def post(self, request, entity_slug, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        faw_model: EmployeeFawModel = self.object
        if self.update_items:
            EmployeeFawItemFormset = get_faw_item_formset(faw_model)
            faw_item_formset: EmployeeFawItemFormset = EmployeeFawItemFormset(request.POST,
                                                                                 user_model=self.request.user,
                                                                                 faw_model=faw_model,
                                                                                 entity_slug=entity_slug)

            context = self.get_context_data(item_formset=faw_item_formset)

            # todo: revisit this workflow and conform to API
            if faw_item_formset.is_valid():
                if faw_item_formset.has_changed():

                    faw_items = faw_item_formset.save(commit=False)
                    create_invoice_uuids = [
                        str(i['uuid'].uuid) for i in faw_item_formset.cleaned_data if i and i['create_invoice'] is True
                    ]

                    if create_invoice_uuids:
                        item_uuids = ','.join(create_invoice_uuids)
                        redirect_url = reverse(
                            'aix:invoice-create-faw',
                            kwargs={
                                'entity_slug': self.kwargs['entity_slug'],
                                'faw_pk': faw_model.uuid,
                            }
                        )
                        redirect_url += f'?item_uuids={item_uuids}'
                        return HttpResponseRedirect(redirect_url)
                    
                    faw_count = faw_items.count(1)
                    for item in faw_items:
                        if not item.faw_model_id:
                            item.faw_model = faw_model
                        # print(item.faw_unit_cost)
                        # item.faw_item_status = 'not_ordered'
                    faw_item_formset.save()
                    # todo: check that update state methods are accepting queryset from formsets...
                    # faw_model.update_faw_state(item_queryset=faw_item_formset.queryset)
                    faw_model.clean()
                    faw_model.save(update_fields=['faw_date',
                                                 'faw_status',
                                                 'updated'])
            # return self.render_to_response(context)
            return HttpResponseRedirect(self.get_success_url())
        return response

    def get_form(self, form_class=None):
        faw_model: EmployeeFawModel = self.object
        if faw_model.is_draft():
            return DraftEmployeeFawModelUpdateForm(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                **self.get_form_kwargs()
            )
        elif faw_model.is_review():
            return ReviewEmployeeFawModelUpdateForm(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                **self.get_form_kwargs()
            )
        elif faw_model.is_approved():
            return ApprovedEmployeeFawModelUpdateForm(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                **self.get_form_kwargs()
            )
        return BaseEmployeeFawModelUpdateForm(
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
        return super(EmployeeFawModelUpdateView, self).get_form_kwargs()

    def get_context_data(self, *, object_list=None, item_formset=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        faw_model: EmployeeFawModel = self.object
        title = f'Jobcard {faw_model.code}'
        context['page_title'] = title
        context['header_title'] = title
        if not item_formset:
            # faw_item_queryset, item_data = faw_model.get_faw_item_data(
            #     queryset=faw_model.itemfawthroughmodel_set.select_related('faw_model').order_by(
            #         'created'
            #     )
            # )
            # faw_item_queryset, item_data = faw_model.get_faw_staff_data(
            #     queryset=EmployeeModel.objects.all().select_related('entity').order_by(
            #         'created'
            #     )
            # )
            # faw_item_queryset = EmployeeModel.objects.all().select_related('entity').order_by(
            #         'created'
            #     )
            employee_qs = WorkOrderPersonnelModel.objects.filter(work_order_id=faw_model.work_order.uuid)  
            initial_data = [{'attendance_code': 'A',
                            'employee_model': emp} for emp in EmployeeModel.objects.filter(pk__in=employee_qs.values_list('employee_id', flat=True))]
            # initial_data = [{'attendance_code': 'A',
            #                 'employee_model': emp} for emp in EmployeeModel.objects.all()]
            print(employee_qs.count(), len(initial_data))
            EmployeeFawItemFormset = get_faw_item_formset2(faw_model)
            context['item_formset'] = EmployeeFawItemFormset(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                faw_model=faw_model,
                # queryset=faw_item_queryset,
                # initial=initial_data,
                # extra=len(initial_data)
            )
            # print(len(initial_data))
            # context['total_amount_due'] = item_data['amount_due']
            # context['total_paid'] = item_data['total_paid']
        else:
            context['item_formset'] = item_formset
            # context['total_amount_due'] = faw_model.faw_amount
            # faw_item_queryset = EmployeeModel.objects.all().select_related('entity').order_by(
            #         'created'
            #     )
            faw_item_queryset, item_data = faw_model.get_faw_item_data(
                queryset=faw_model.itemfawthroughmodel_set.filter(faw_model_id=faw_model.uuid).select_related('faw_model').order_by(
                    'created'
                )
            )
            # context['total_amount_due'] = item_data['amount_due']
            # context['total_paid'] = item_data['total_paid']
        return context
        
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        qty = self.request.GET.get('qty', None)
        qs = EmployeeModel.objects.all()
        if qty:
            qs = qs.filter(qty=qty)
        # kwargs['extra'] = qty
        return kwargs

    def get_success_url(self):
        entity_slug = self.kwargs['entity_slug']
        faw_pk = self.kwargs['faw_pk']
        return reverse('aix:faw-detail',
                       kwargs={
                           'entity_slug': entity_slug,
                           'faw_pk': faw_pk
                       })

    def get_queryset(self):
        return EmployeeFawModel.objects.filter(
            entity__slug=self.kwargs['entity_slug'],
            # user=self.request.user,
            # work_order=self.work_order.uuid
        ).select_related('entity')
        # return EmployeeFawModel.objects.for_entity(
        #     entity_slug=self.kwargs['entity_slug'],
        #     user_model=self.request.user
        # ).select_related('entity')

    def form_valid(self, form: BaseEmployeeFawModelUpdateForm):
        faw_model: EmployeeFawModel = form.save(commit=False)

        if form.has_changed():
            faw_items_qs = ItemFawThroughModel.objects.for_faw(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                faw_pk=faw_model.uuid,
            ).select_related('faw_model')

            if all(['faw_status' in form.changed_data,
                    faw_model.faw_status == faw_model.FAW_STATUS_FULFILLED]):
                faw_items_qs.update(faw_item_status=ItemFawThroughModel.FAW_STATUS_CANCELED)

        messages.add_message(self.request,
                             messages.SUCCESS,
                             f'{self.object.code} successfully updated.',
                             extra_tags='is-success')

        return super().form_valid(form)
    
    # def get(self, request, *args, **kwargs):
    #     if id in kwargs.keys():
    #         employee = EmployeeModel.objects.get(id=kwargs.get('id'))
    #     else:
    #         employee = None
            
    #     # faw_form = BaseEmployeeFawModelUpdateForm(instance=employee)
    #     # faw_model: EmployeeFawModel = self.object
    #     # EmployeeFawItemFormset = get_faw_item_formset(employee)
    #     ReadOnlyEmployeeFawItemFormset = modelformset_factory(
    #         model=ItemFawThroughModel,
    #         form=EmployeeFawItemForm,
    #         formset=BaseEmployeeFawItemFormset,
    #         queryset=employee
    #     )
    #     context['item_formset'] = EmployeeFawItemFormset(
    #         entity_slug=self.kwargs['entity_slug'],
    #         user_model=self.request.user,
    #         faw_model=self.faw_model,
    #         instance=employee,
    #     )
    #     return (request, self.template_name, context)



class EmployeeFawModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'faw_pk'
    slug_field = 'uuid'
    context_object_name = 'faw_model'
    template_name = 'aix/app/operations/intrafield/faw_detail.html'
    extra_context = {
        'header_subtitle_icon': 'uil:invoice',
        'hide_menu': True
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        faw_model: EmployeeFawModel = self.object
        title = f'Code {faw_model.code}'
        context['page_title'] = title
        context['header_title'] = title

        faw_model: EmployeeFawModel = self.object
        faw_items_qs, item_data = faw_model.get_faw_item_data(
            queryset=faw_model.itemfawthroughmodel_set.filter(faw_model_id=faw_model.uuid).select_related('employee_model')
        )
        context['faw_items'] = faw_items_qs

        # faw_item_queryset, item_data = faw_model.get_faw_item_data(
        #     queryset=faw_model.itemFawthroughmodel_set.select_related('faw_model').order_by(
        #         'created'
        #     )
        # )
        return context

    def get_queryset(self):
        return EmployeeFawModel.objects.filter(
            entity__slug=self.kwargs['entity_slug'],
            # user=self.request.user,
            # work_order=self.work_order.uuid
        ).select_related('entity')
        # return EmployeeFawModel.objects.for_entity(
        #     entity_slug=self.kwargs['entity_slug'],
        #     user_model=self.request.user,
        #     # work_order=self.work_order.uuid
        # ).select_related('entity')


class EmployeeFawModelDeleteView(LoginRequiredMixIn, DeleteView):
    slug_url_kwarg = 'faw_pk'
    slug_field = 'uuid'
    context_object_name = 'faw_model'
    template_name = 'aix/app/operations/intrafield/faw_delete.html'
    extra_context = {
        'hide_menu': True,
        'header_subtitle_icon': 'uil:invoice'
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        faw_model: EmployeeFawModel = self.object
        context['page_title'] = _('Delete Jobcard ') + faw_model.code
        context['header_title'] = context['page_title']
        return context

    def get_queryset(self):
        return EmployeeFawModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:entity-dashboard',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                       })

    def delete(self, request, *args, **kwargs):
        faw_model: EmployeeFawModel = self.get_object()
        self.object = faw_model
        faw_items_qs = faw_model.itemfawthroughmodel_set.filter(invoice_model__isnull=False)
        if faw_items_qs.exists():
            messages.add_message(request,
                                 message=f'Cannot delete {faw_model.code} because it has related invoices.',
                                 level=messages.ERROR,
                                 extra_tags='is-danger')
            url = reverse('aix:faw-update',
                          kwargs={
                              'entity_slug': self.kwargs['entity_slug'],
                              'faw_pk': self.kwargs['faw_pk']
                          })
            return HttpResponseRedirect(url)
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


# ACTIONS...
class BaseEmployeeFawActionActionView(LoginRequiredMixIn, RedirectView, SingleObjectMixin):
    http_method_names = ['get']
    pk_url_kwarg = 'faw_pk'
    action_name = None
    commit = True

    def get_queryset(self):
        return EmployeeFawModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_redirect_url(self, entity_slug, faw_pk, *args, **kwargs):
        return reverse('aix:faw-update',
                       kwargs={
                           'entity_slug': entity_slug,
                           'faw_pk': faw_pk
                       })

    def get(self, request, *args, **kwargs):
        kwargs['user_model'] = self.request.user
        if not self.action_name:
            raise ImproperlyConfigured('View attribute action_name is required.')
        response = super(BaseEmployeeFawActionActionView, self).get(request, *args, **kwargs)
        # faw_model: EmployeeFawModel = self.get_object()
        faw_qs = EmployeeFawModel.objects.all()
        faw_model: EmployeeFawModel = get_object_or_404(faw_qs, uuid=self.kwargs['faw_pk'])

        try:
            getattr(faw_model, self.action_name)(commit=self.commit, **kwargs)
        except ValidationError as e:
            messages.add_message(request,
                                 message=e.message,
                                 level=messages.ERROR,
                                 extra_tags='is-danger')
        return response


class EmployeeFawMarkAsDraftView(BaseEmployeeFawActionActionView):
    action_name = 'mark_as_draft'


class EmployeeFawMarkAsReviewView(BaseEmployeeFawActionActionView):
    action_name = 'mark_as_review'


class EmployeeFawMarkAsApprovedView(BaseEmployeeFawActionActionView):
    action_name = 'mark_as_approved'


class EmployeeFawMarkAsFulfilledView(BaseEmployeeFawActionActionView):
    action_name = 'mark_as_fulfilled'


class EmployeeFawMarkAsCanceledView(BaseEmployeeFawActionActionView):
    action_name = 'mark_as_canceled'


class EmployeeFawMarkAsVoidView(BaseEmployeeFawActionActionView):
    action_name = 'mark_as_void'

# Reports

class EmployeeFawReportView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'faw_pk'
    slug_field = 'uuid'
    context_object_name = 'faw_model'
    template_name = 'aix/app/operations/intrafield/faw_detail.html'
    extra_context = {
        'header_subtitle_icon': 'uil:invoice',
        'hide_menu': True
    }
    dwn_report_file = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        faw_model: EmployeeFawModel = self.object
        title = f'FAW {faw_model.code}'
        context['page_title'] = title
        context['header_title'] = title

        faw_model: EmployeeFawModel = self.object
        faw_items_qs, item_data = faw_model.get_faw_item_data(
            queryset=faw_model.itemfawthroughmodel_set.filter(faw_model_id=faw_model.uuid).select_related('employee_model')
        )
        context['customer'] = faw_model.work_order.customer
        context['faw_items'] = faw_items_qs

        faw_item_queryset, item_data = faw_model.get_faw_item_data(
            queryset=faw_model.itemfawthroughmodel_set.filter(faw_model_id=faw_model.uuid).select_related('faw_model').order_by(
                'created'
            )
        )
        # Create a list of days in June
        days_in_june = [f"{day}" for day in range(1, 31)]  # June has 30 days

        # Create a DataFrame with one row and each day as a column
        df = pd.DataFrame([[''] * len(days_in_june)], columns=days_in_june, index=faw_items_qs.values_list('employee_model__name', flat=True))

        # for index, faw_item in enumerate(faw_items_qs):
        #     # Assuming faw_item.attendance_date is a datetime object
        #     if faw_item.attendance_date:
        #         day = faw_item.attendance_date.day
        #         # Check if the day is in the DataFrame's columns
        #         if str(day) in df.columns:
        #             # Set the value for that day
        #             df.at[index, str(day)] = faw_item.attendance_code
        #             print(faw_item.attendance_code, day, str(index))
        for row_index, faw_item in enumerate(faw_items_qs):
            for col_index, day in enumerate(days_in_june):
                # Assuming faw_item.attendance_date is a datetime object
                if faw_item.attendance_date:
                    if str(faw_item.attendance_date.day) == day:
                        # Set the value for that day
                        df.at[faw_item.employee_model.name, day] = faw_item.attendance_code
                        print(faw_item.attendance_code, faw_item.attendance_date, day, faw_item.employee_model.name)
        
        df['P'] = (df == 'P').sum(axis=1)
        df['L'] = (df == 'L').sum(axis=1)
        df['S'] = (df == 'S').sum(axis=1)
        df['A'] = (df == 'A').sum(axis=1)  
        df['D2'] = (df == 'D2').sum(axis=1)
        df['MOB'] = (df == 'MOB').sum(axis=1)
        df['DMB'] = (df == 'DMB').sum(axis=1)

        total_columns = ['P', 'L', 'S', 'A', 'D2', 'MOB', 'DMB']
        # Add a new column for the total of each row
        blank_row = {col: '' for col in df.columns}
        for col in total_columns:
            blank_row[col] = df[col].sum()
        grand_total_row = pd.DataFrame([blank_row], index=['Grand Total'])
        df = pd.concat([df, grand_total_row], ignore_index=False)
        df.index = df.index.map(lambda i: 'Grand Total' if i == len(df) - 1 else str(i))

        # Display the DataFrame
        context['faw_items_df'] = df.to_html(classes='table')    
        return context

    def get_queryset(self):
        return EmployeeFawModel.objects.filter(
            entity__slug=self.kwargs['entity_slug'],
            # user=self.request.user,
            # work_order=self.work_order.uuid
        ).select_related('entity')
        # return EmployeeFawModel.objects.for_entity(
        #     entity_slug=self.kwargs['entity_slug'],
        #     user_model=self.request.user
        # ).select_related('entity')

    def get(self, request, *args, **kwargs):
        response = super(EmployeeFawReportView, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        if self.dwn_report_file:
            # data = CustomerModel.objects.all().order_by('customer_name')
            open('aix/templates/aix/reports/temp.html', "w").write(render_to_string('aix/reports/result.html', {'data': context}))

            # Converting the HTML template into a PDF file
            #pdf = self.html_to_pdf('aix/templates/aix/reports/temp.html', data)
            
            # customer_qs = data.values('customer_name', 'email')
            # df = pd.DataFrame(customer_qs)
            
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template("aix/templates/aix/reports/faw_rpt.html")
            # template = get_template(template_src)
            # context_dict = {"title" : "Customers Report - List"}
            # context_dict['data'] = data
            data = context['faw_items'].values('faw_model__code')
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