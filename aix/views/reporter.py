from datetime import timedelta, datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader, RequestContext
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from django.contrib.auth import get_user_model
from django.db.models import Q, Sum, Count, QuerySet

import os.path
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
import numpy as np
from xhtml2pdf import pisa 
import pandas as pd
from jinja2 import Environment, FileSystemLoader

from aix.forms.reporter import ReportForm, ReporterForm
from aix.models.aix_its_status_report import AixItsStatusReportModel
from aix.models.customer import CustomerModel
from aix.models.entity import EntityModel
from aix.models.equipment import EquipmentModel
from aix.models.employee_faw import EmployeeFawModel
from aix.models.employee_faw_items import ItemFawThroughModel
from aix.models.equipment_fet import EquipmentFetModel
from aix.models.equipment_fet_items import ItemFetThroughModel
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
from aix.models.reporter import ReportModel
from aix.views.mixins import LoginRequiredMixIn

UserModel = get_user_model()

class ReportModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/reports/reporter.html'
    context_object_name = 'reports'
    PAGE_TITLE = _('Report List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return ReportModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class ReportModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/reports/report_manager.html'
    PAGE_TITLE = _('Create New Report')
    form_class = ReportForm
    context_object_name = 'report'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return ReportForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:report-list',           kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    # def form_valid(self, form):
    #     report_model: ReportModel = form.save(commit=False)
    #     entity_model = EntityModel.objects.for_user(
    #         user_model=self.request.user
    #     ).get(slug__exact=self.kwargs['entity_slug'])
    #     report_model.entity = entity_model
    #     # report_model.save()
    #     # return super().form_valid(form)
    #     return super()
    
    def post(self, request, entity_slug, *args, **kwargs):
        response = super(ReportModelCreateView, self).post(request, *args, **kwargs)
        return self.render_to_response({ 'entity_slug': entity_slug })
        # return response


class ReportModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/reports/reporter.html'
    PAGE_TITLE = _('Report Update')
    context_object_name = 'report'
    form_class = ReportForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'report_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return ReportModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:report-create',           kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class ReporterFilterView(ListView):
    template_name = 'aix/reports/reporter.html'
    context_object_name = 'reports'
    PAGE_TITLE = _('Report List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill',
        'entity_slug': 'total-uganda-13sjr71j'
    }
    
    search_string = None
    sort_by = None
    order_by = None

    def get_queryset(self):
        return ReportModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        title = f'Repport Manager '
        context['page_title'] = title
        context['header_title'] = title

        context['report_filter'] = ReportForm
        return context

    def get_success_url(self):
        return reverse('aix:report-filter',           kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def get(self, request, entity_slug):
        self.request = request
        return super(ReporterFilterView, self).get(request, self)
 
    # def post(self, request,  *args, **kwargs):
    #     title_contains = request.POST['title_contains']
    #     context = {}
    #     context['entity_slug'] = entity_slug
    #     context['title_contains'] = title_contains
    #     context['entity_slug'] = entity_slug
    #     print(request.POST['title_contains'])
    #     print(request)
    #     form = {}
    #     return render(request, 'aix/reports/reporter.html', {'entity_slug':entity_slug })
    #     # return render_to_response('classroom/classroom_privacy.html', { 'form': form }, context_instance=RequestContext(request))
    #     # return redirect(reverse('aix:report-filter', args = (entity_slug,)))
    #     """
    #     Process comment
    #     """
        # self.form = ReporterForm(request.POST or None)

        # if self.form.is_valid():
            # post = Post.objects.get(pk = id)
            # post.n_comments += 1
            # post.save()

            # comment = Comment()
            # comment.comment = request.POST['comment']
            # comment.created_at = timezone.now()
            # comment.modified_at = timezone.now()
            # comment.post_id = id
            # comment.user_id = 2
            # comment.save()

            # return redirect(reverse('aix:report-filter', args = (id,)))



    def post(self, request, entity_slug,*args, **kwargs):
        # response = super(ReporterFilterView, self).post(request, *args, **kwargs)
        tpl = loader.get_template('aix/reports/reporter.html')
        context_object_name = 'reports'
        
        
        context = {}
        context['entity_slug'] = entity_slug
        title_contains = request.POST['title_contains']
        context['title_contains'] = title_contains
        context['entity_slug'] = entity_slug
        print(request.POST['title_contains'])
        print(request)
        request.context = context
        wo_qs = WorkOrderModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )
        context['wo_qs'] = wo_qs
        # self.object_list = wo_qs
        # context = self.get_context_data(item_formset=item_formset)
        # return self.render_to_response(args=self.kwargs['entity_slug'], context=RequestContext(request))
        # return HttpResponse(tpl.render(context, request), content_type="application/xhtml+xml")
        return render(request, 'aix/reports/reporter.html', { 'entity_slug': entity_slug, 'wo_qs':wo_qs, 'dd':'ddk'})


class ReportResultsView(LoginRequiredMixIn, ListView):
    template_name = 'aix/reports/report_manager.html'
    context_object_name = 'reports'
    PAGE_TITLE = _('Report List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill',
        'hide_menu': False
    }
    report = None
    search_string = None
    sort_by = None
    order_by = None
    dwn_report_file = False
    work_order = None
    start_date = None
    end_date = None

    def get_queryset(self):
        return ReportModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')
    

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        title = f'Repport Manager '
        context['page_title'] = title
        context['header_title'] = title
        context['entity_slug'] = self.kwargs['entity_slug']

        context['report_filter'] = ReportForm
        context['reportname'] = self.search_string
        context['searchstring'] = self.search_string
        context['sortby'] = self.sort_by
        context['orderby'] = self.order_by
        context['start_date'] = self.start_date
        context['end_date'] = self.end_date
        context['workorder'] = self.work_order
        print(self.work_order)
        reportname = self.report
        searchstring = self.search_string
        sortby = self.sort_by
        orderby = self.order_by
        work_order = self.work_order
        start_date = self.start_date
        end_date = self.end_date
        results = ''
        wo_qs = WorkOrderModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )
        if self.request.method == 'POST':
            searchstring = self.request.POST['searchstring']
            sortby = self.request.POST['sortby']
            orderby = self.request.POST['orderby']
            reportname = self.request.POST['report']
            work_order = self.request.POST['workorder']
            start_date = self.request.POST.get('start', None)
            end_date = self.request.POST.get('end', None)
            self.work_order = work_order
            if reportname == 'A':
                status_report_qs = AixItsStatusReportModel.objects.for_entity(
                    entity_slug=self.kwargs['entity_slug'],
                    user_model=self.request.user
                )
                if start_date and end_date:
                    # s_date = datetime.strftime(start_date, "%Y-%m-%d %H:%M:%S.%f")
                    # e_date = datetime.strftime(end_date, "%Y-%m-%d") + timedelta(days=1)
                    status_report_qs = status_report_qs.filter(startdate__gte=start_date, duedate__lte=end_date)
                results = status_report_qs
            if reportname == 'B':
                equipment_qs = EquipmentModel.objects.for_entity(
                    entity_slug=self.kwargs['entity_slug'],
                    user_model=self.request.user
                )

                results = equipment_qs

            if reportname == 'C':
                fet_qs = ItemFetThroughModel.objects.filter(fet_model__work_order=self.work_order)
                data = fet_qs

                # generate table for fet
                days_in_june = [f"{day}" for day in range(1, 31)]  # June has 30 days
                # Create a DataFrame with one row and each day as a column
                df = pd.DataFrame([[''] * len(days_in_june)], columns=days_in_june, index=fet_qs.values_list('equipment_model__reg_no', flat=True)) 
                # Iterate through the queryset and fill the DataFrame
                for row_index, fet_item in enumerate(fet_qs):
                    for col_index, day in enumerate(days_in_june):
                        if fet_item.attendance_date:
                            if fet_item.attendance_date.day == int(day):
                                df.at[fet_item.equipment_model.reg_no, str(day)] = fet_item.attendance_code
                                # print(fet_item.attendance_code, day, fet_item.equipment_model.reg_no)
                df.drop_duplicates(inplace=True)

                df['H'] = (df == 'H').sum(axis=1)
                df['S'] = (df == 'S').sum(axis=1)
                df['OH'] = (df == 'OH').sum(axis=1)
                df['R'] = (df == 'R').sum(axis=1)  
                df['MOB'] = (df == 'MOB').sum(axis=1)
                df['DMB'] = (df == 'DMB').sum(axis=1)
                df['NOS'] = (df == 'NOS').sum(axis=1)
                df['OPS'] = (df == 'OPS').sum(axis=1)
                df['ES'] = (df == 'ES').sum(axis=1)
                total_columns = ['H', 'S', 'OH', 'R', 'MOB', 'DMB', 'NOS', 'OPS', 'ES']
                blank_row = {col: '' for col in df.columns}
                for col in total_columns:
                    blank_row[col] = df[col].sum()
                grand_total_row = pd.DataFrame([blank_row], index=['Grand_Total'])
                df = pd.concat([df, grand_total_row], ignore_index=False)
                # df = pd.concat([df, pd.DataFrame([blank_row])], ignore_index=False)
                df.index = df.index.map(lambda i: 'Grand_Total' if i == len(df) - 1 else str(i))
                df_table = df.to_html(classes='table')
                context['df_table'] = df_table
                context['fet_items_df'] = df_table
                # print(df_table)

            if reportname == 'D':
                # faw_qs = ItemFawThroughModel.objects.filter(faw_model__work_order=work_order)
                faw_qs = ItemFawThroughModel.objects.all()
                data = faw_qs
                print(faw_qs.count())
                # Create a list of days in June
                days_in_june = [f"{day}" for day in range(1, 31)]  # June has 30 days
                # Create a DataFrame with one row and each day as a column
                df = pd.DataFrame([[''] * len(days_in_june)], columns=days_in_june, index=faw_qs.values_list('employee_model__name', flat=True))
                # df = df.set_index('staff')
                for row_index, faw_item in enumerate(faw_qs):
                    for col_index, day in enumerate(days_in_june):
                        # Assuming faw_item.attendance_date is a datetime object
                        if faw_item.attendance_date:
                            if str(faw_item.attendance_date.day) == day:
                                # Set the value for that day
                                df.at[faw_item.employee_model.name, day] = faw_item.attendance_code
                                # print(faw_item.attendance_code, faw_item.attendance_date, day, faw_item.employee_model.name)
                # df = df.drop_duplicates(subset=[''], keep='first')
                # df = df.index.duplicated(keep='first')
                df = df.loc[~df.index.duplicated(keep='first'), :]
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
                df_table = df.to_html(classes='table')
                context['df_table'] = df_table
                context['faw_items_df'] = df_table

        context['results'] = results
        context['reportname'] = reportname
        context['searchstring'] = searchstring
        context['sortby'] = sortby
        context['orderby'] = orderby
        context['workorder'] = work_order
        context['start_date'] = start_date
        context['end_date'] = end_date
        context['work_orders'] = wo_qs
        return context

    def get_success_url(self):
        return reverse('aix:report-filter-results',           kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'search_string': self.search_string,
                           'report': self.report,
                           'sort_by': self.sort_by,
                           'order_by': self.order_by,
                           'work_order': self.work_order
                       })
    
    def get(self, request, entity_slug):
        response = super(ReportResultsView, self).get(request, self)
        # if self.dwn_report_file == True:
        #     self.request = request
        #     print(self.request.method)
        #     if self.request.method == 'GET':
        #         # self.DownLoadData(request)
        #         with BytesIO() as b:
        #             # data = get_analytics_data()
        #             data = []

        #             # searchstring = self.request.POST['searchstring']
        #             # sortby = self.request.POST['sortby']
        #             # orderby = self.request.POST['orderby']
        #             # reportname = self.request.POST['report']
        #             print(self.search_string)
        #             searchstring = ""
        #             sortby = ""
        #             orderby = ""
        #             reportname = "A"
        #             if reportname == 'A':
        #                 wo_qs = WorkOrderModel.objects.for_entity(
        #                     entity_slug=self.kwargs['entity_slug'],
        #                     user_model=self.request.user
        #                 )
        #                 data = wo_qs
        #             if reportname == 'B':
        #                 task_qs = WorkOrderTaskModel.objects.for_entity(
        #                     entity_slug=self.kwargs['entity_slug'],
        #                     user_model=self.request.user
        #                 )
        #                 data = task_qs
        #             if reportname == 'C':
        #                 kpi_ops_qs = KpiOpsModel.objects.for_entity(
        #                     entity_slug=self.kwargs['entity_slug'],
        #                     user_model=self.request.user
        #                 )
        #                 data = kpi_ops_qs

        #             # print(data)
        #             df = pd.DataFrame.from_dict(data)
        #             response = HttpResponse(content_type='application/xlsx')
        #             response['Content-Disposition'] = f'attachment; filename="FILENAME.xlsx"'
        #             with pd.ExcelWriter(response) as writer:
        #                 df.to_excel(writer, sheet_name='SHEET NAME')

        return response

    def post(self, request, entity_slug,*args, **kwargs):
        self.request = request
        response = super(ReportResultsView, self).get(request, self)
        dwn = int(self.request.POST['download'])
        searchstring = self.request.POST['searchstring']
        sortby = self.request.POST['sortby']
        orderby = self.request.POST['orderby']
        reportname = self.request.POST['report']
        work_order = self.request.POST['workorder']
        start_date = self.request.POST.get('start', None)
        end_date = self.request.POST.get('end', None)
        context = self.get_context_data()
        df_table = None

        if dwn < 1:
            self.request = request
            # if self.request.method == 'POST':
            with BytesIO() as b:
                data = []
                dataframe = None
                FILENAME = 'Exported_Data'
                if reportname == 'A':
                    status_report_qs = AixItsStatusReportModel.objects.for_entity(
                        entity_slug=self.kwargs['entity_slug'],
                        user_model=self.request.user
                    )
                    status_report_qs = status_report_qs.all().defer('created','updated')
                    if start_date and end_date:
                        status_report_qs = status_report_qs.filter(startdate__gte=start_date, duedate__lte=end_date)
                    data = status_report_qs.values('activity', 'activity_type', 'startdate', 'duedate', 'description', 'priority', 'status')
                    # print(data, start_date, end_date)
                    FILENAME = 'exported_status_report'
                if reportname == 'A1':
                    wo_qs = WorkOrderModel.objects.for_entity(
                        entity_slug=self.kwargs['entity_slug'],
                        user_model=self.request.user
                    )
                    data = wo_qs.values()
                    # print(data)
                    FILENAME = 'exported_work_order'
                if reportname == 'B':
                    equipment_qs = EquipmentModel.objects.for_entity(
                        entity_slug=self.kwargs['entity_slug'],
                        user_model=self.request.user
                    )
                    data = equipment_qs
                    FILENAME = 'exported_equipment'
                if reportname == 'C':
                    fet_qs = ItemFetThroughModel.objects.filter(fet_model__work_order=self.work_order)
                    data = fet_qs

                    # generate table for fet
                    days_in_june = [f"{day}" for day in range(1, 31)]  # June has 30 days
                    # Create a DataFrame with one row and each day as a column
                    df = pd.DataFrame([[''] * len(days_in_june)], columns=days_in_june, index=fet_qs.values_list('equipment_model__reg_no', flat=True)) 
                    # Iterate through the queryset and fill the DataFrame
                    for row_index, fet_item in enumerate(fet_qs):
                        for col_index, day in enumerate(days_in_june):
                            if fet_item.attendance_date:
                                if fet_item.attendance_date.day == int(day):
                                    df.at[fet_item.equipment_model.reg_no, str(day)] = fet_item.attendance_code
                                    # print(fet_item.attendance_code, day, fet_item.equipment_model.reg_no)
                    df.drop_duplicates(inplace=True)

                    df['H'] = (df == 'H').sum(axis=1)
                    df['S'] = (df == 'S').sum(axis=1)
                    df['OH'] = (df == 'OH').sum(axis=1)
                    df['R'] = (df == 'R').sum(axis=1)  
                    df['MOB'] = (df == 'MOB').sum(axis=1)
                    df['DMB'] = (df == 'DMB').sum(axis=1)
                    df['NOS'] = (df == 'NOS').sum(axis=1)
                    df['OPS'] = (df == 'OPS').sum(axis=1)
                    df['ES'] = (df == 'ES').sum(axis=1)
                    total_columns = ['H', 'S', 'OH', 'R', 'MOB', 'DMB', 'NOS', 'OPS', 'ES']
                    blank_row = {col: '' for col in df.columns}
                    for col in total_columns:
                        blank_row[col] = df[col].sum()
                    grand_total_row = pd.DataFrame([blank_row], index=['Grand_Total'])
                    df = pd.concat([df, grand_total_row], ignore_index=False)
                    # df = pd.concat([df, pd.DataFrame([blank_row])], ignore_index=False)
                    df.index = df.index.map(lambda i: 'Grand_Total' if i == len(df) - 1 else str(i))
                    df_table = df.to_html(classes='table is-bordered')
                    context['df_table'] = df_table
                    context['fet_items_df'] = df_table
                    # print(df_table)

                if reportname == 'D':
                    faw_qs = ItemFawThroughModel.objects.filter(faw_model__work_order=work_order)
                    data = faw_qs
                    # Create a list of days in June
                    days_in_june = [f"{day}" for day in range(1, 31)]  # June has 30 days
                    # Create a DataFrame with one row and each day as a column
                    df = pd.DataFrame([[''] * len(days_in_june)], columns=days_in_june, index=faw_qs.values_list('employee_model__name', flat=True))
                    # df = df.set_index('staff')
                    for row_index, faw_item in enumerate(faw_qs):
                        for col_index, day in enumerate(days_in_june):
                            # Assuming faw_item.attendance_date is a datetime object
                            if faw_item.attendance_date:
                                if str(faw_item.attendance_date.day) == day:
                                    # Set the value for that day
                                    df.at[faw_item.employee_model.name, day] = faw_item.attendance_code
                                    # print(faw_item.attendance_code, faw_item.attendance_date, day, faw_item.employee_model.name)
                    # df = df.drop_duplicates(subset=[''], keep='first')
                    df = df.index.duplicated(keep='first')
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
                    df_table = df.to_html(classes='table is-bordered')
                    context['df_table'] = df_table
                    context['faw_items_df'] = df_table
                
                df_cleaned = pd.DataFrame(data)
                response = HttpResponse(content_type='application/xlsx')
                response['Content-Disposition'] = f'attachment; filename="{FILENAME}.xlsx"'
                with pd.ExcelWriter(response) as writer:
                    df_cleaned.to_excel(writer, sheet_name='SHEET NAME')
                return response
        else:
            # print(searchstring, reportname)
            data = None
            if reportname == 'A':
                status_report_qs = AixItsStatusReportModel.objects.for_entity(
                    entity_slug=self.kwargs['entity_slug'],
                    user_model=self.request.user
                )
                data = status_report_qs
            if reportname == 'B':
                equipment_qs = EquipmentModel.objects.for_entity(
                    entity_slug=self.kwargs['entity_slug'],
                    user_model=self.request.user
                )
                data = equipment_qs
            if reportname == 'C':
                fet_qs = ItemFetThroughModel.objects.filter(fet_model__work_order=self.work_order)
                data = fet_qs

                # generate table for fet
                days_in_june = [f"{day}" for day in range(1, 31)]  # June has 30 days
                # Create a DataFrame with one row and each day as a column
                df = pd.DataFrame([[''] * len(days_in_june)], columns=days_in_june, index=fet_qs.values_list('equipment_model__reg_no', flat=True)) 
                # Iterate through the queryset and fill the DataFrame
                for row_index, fet_item in enumerate(fet_qs):
                    for col_index, day in enumerate(days_in_june):
                        if fet_item.attendance_date:
                            if fet_item.attendance_date.day == int(day):
                                df.at[fet_item.equipment_model.reg_no, str(day)] = fet_item.attendance_code
                                # print(fet_item.attendance_code, day, fet_item.equipment_model.reg_no)
                df.drop_duplicates(inplace=True)

                df['H'] = (df == 'H').sum(axis=1)
                df['S'] = (df == 'S').sum(axis=1)
                df['OH'] = (df == 'OH').sum(axis=1)
                df['R'] = (df == 'R').sum(axis=1)  
                df['MOB'] = (df == 'MOB').sum(axis=1)
                df['DMB'] = (df == 'DMB').sum(axis=1)
                df['NOS'] = (df == 'NOS').sum(axis=1)
                df['OPS'] = (df == 'OPS').sum(axis=1)
                df['ES'] = (df == 'ES').sum(axis=1)
                total_columns = ['H', 'S', 'OH', 'R', 'MOB', 'DMB', 'NOS', 'OPS', 'ES']
                blank_row = {col: '' for col in df.columns}
                for col in total_columns:
                    blank_row[col] = df[col].sum()
                grand_total_row = pd.DataFrame([blank_row], index=['Grand_Total'])
                df = pd.concat([df, grand_total_row], ignore_index=False)
                # df = pd.concat([df, pd.DataFrame([blank_row])], ignore_index=False)
                df.index = df.index.map(lambda i: 'Grand_Total' if i == len(df) - 1 else str(i))
                df_table = df.to_html(classes='table is-bordered')
                context['df_table'] = df_table
                context['fet_items_df'] = df_table
                # print(df_table)

            if reportname == 'D':
                faw_qs = ItemFawThroughModel.objects.filter(faw_model__work_order=work_order)
                data = faw_qs
                # Create a list of days in June
                days_in_june = [f"{day}" for day in range(1, 31)]  # June has 30 days
                # Create a DataFrame with one row and each day as a column
                df = pd.DataFrame([[''] * len(days_in_june)], columns=days_in_june, index=faw_qs.values_list('employee_model__name', flat=True))
                # df = df.set_index('staff')
                for row_index, faw_item in enumerate(faw_qs):
                    for col_index, day in enumerate(days_in_june):
                        # Assuming faw_item.attendance_date is a datetime object
                        if faw_item.attendance_date:
                            if str(faw_item.attendance_date.day) == day:
                                # Set the value for that day
                                df.at[faw_item.employee_model.name, day] = faw_item.attendance_code
                                # print(faw_item.attendance_code, faw_item.attendance_date, day, faw_item.employee_model.name)
                # df = df.drop_duplicates(subset=[''], keep='first')
                df = df.loc[~df.index.duplicated(keep='first'), :]
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
                df_table = df.to_html(classes='table is-bordered')
                context['df_table'] = df_table
                context['faw_items_df'] = df_table

            # if reportname == 'C':
            #     kpi_ops_qs = KpiOpsModel.objects.for_entity(
            #         entity_slug=self.kwargs['entity_slug'],
            #         user_model=self.request.user
            #     )
            #     data = kpi_ops_qs
            
            # if reportname == 'D':
            #     hse_data = self.rpt_hse_records()
            #     df_hse = pd.DataFrame(hse_data)
            #     columns_hse = ['fat','lti','rwdc','mtc','fac','hipo','envdam','nmi','matloss','ptw','tbt','hht','drills','audit','training_subject','reporting_cards','safety_initiative']
            #     df_hse = pd.pivot_table(df_hse, index=['activity_date'],values=columns_hse,aggfunc=np.sum)
            #     df_hse = df_hse.to_html(classes='data', header="true")
            #     response.context_data['df_hse'] = df_hse

            #     ops_data = self.rpt_ops_records()
            #     df_ops = pd.DataFrame(ops_data)
            #     columns_ops = ['etp','atp','activity_time','kms_passed','consol_fuel','operator','banksman','rigger1','rigger2','rigger3','rigger4','section2_time_taken','section2_ton_cargo','section2_number_lifts','section2_ton_lifts','no_routine','no_simple','no_complicated','no_complex','ton_routine','ton_simple','ton_complicated','ton_complex','section3_time_taken','section3_ton_cargo','section3_number_lifts','section3_ton_lifts','llt_dsb','llt_tgi','llt_rig1','llt_rig2','llt_rig3','llt_other','tlt_dsb','tlt_tgi','tlt_rig1','tlt_rig2','tlt_rig3','tlt_other','dnt_dsb','dnt_tgi','dnt_rig1','dnt_rig2','dnt_rig3','dnt_other']
            #     df_ops = pd.pivot_table(df_ops, index=['activity_date', 'equipment__vehicle_type_name'],values=columns_ops,aggfunc=np.sum)
            #     df_ops = df_ops.to_html(classes='data', header="true")
            #     response.context_data['df_ops'] = df_ops
                
            #     ops_data = self.rpt_ops_records()
            #     df_ops_dpf = pd.DataFrame(ops_data)
            #     # print(df_ops_dpf)
            #     df_ops_dpf = self.column_calculations(df_ops_dpf)
            #     # print(df_ops_dpf)
            #     # columns_ops = ['etp','atp','activity_time','kms_passed','consol_fuel','operator','banksman','rigger1','rigger2','rigger3','rigger4','section2_time_taken','section2_ton_cargo','section2_number_lifts','section2_ton_lifts','no_routine','no_simple','no_complicated','no_complex','ton_routine','ton_simple','ton_complicated','ton_complex','section3_time_taken','section3_ton_cargo','section3_number_lifts','section3_ton_lifts','llt_dsb','llt_tgi','llt_rig1','llt_rig2','llt_rig3','llt_other','tlt_dsb','tlt_tgi','tlt_rig1','tlt_rig2','tlt_rig3','tlt_other','dnt_dsb','dnt_tgi','dnt_rig1','dnt_rig2','dnt_rig3','dnt_other']
            #     # df_ops_dpf = pd.pivot_table(df_ops_dpf, index=['trip_code'],values=columns_ops,aggfunc=np.sum)
            #     df_ops_dpf = df_ops_dpf.to_html(classes='data', header="true")
            #     response.context_data['df_ops_dpf'] = df_ops_dpf

            #     # df_ops_month = pd.DataFrame(ops_data)
            #     # df_ops_month.groupby(df_ops_month['activity_date'].dt.month).sum()
            #     # columns_ops_month = ['etp','atp','activity_time','kms_passed','consol_fuel']
            #     # df_ops_month = pd.pivot_table(df_ops_month,index=['activity_date', 'equipment__vehicle_type_name'],values=columns_ops,aggfunc=np.sum)
            #     # df_ops_month = df_ops_month.to_html(classes='data', header="true")
                
            #     df_ops_month = pd.DataFrame(ops_data)
            #     df_ops_month.index = pd.to_datetime(df_ops_month['activity_date'],format='%m/%d/%y %I:%M%p')
            #     # df_ops_month.groupby(by=[df_ops_month.index.month, df_ops_month.index.year])
            #     columns_ops_month = ['etp','atp','activity_time','kms_passed','consol_fuel']
            #     df_ops_month = pd.pivot_table(df_ops_month,index=df_ops_month.index.month,values=columns_ops,aggfunc=np.sum)
            #     df_ops_month = df_ops_month.to_html(classes='data', header="true")
            #     response.context_data['sug_ops_transport'] = df_ops_month
            #     df_ops_month = pd.DataFrame(ops_data)
            #     df_ops_month.index = pd.to_datetime(df_ops_month['activity_date'],format='%m/%d/%y %I:%M%p')
            #     columns_ops_month = ['kms_passed','consol_fuel','no_routine','no_simple','no_complicated','no_complex','ton_routine','section2_number_lifts']
            #     df_ops_month = pd.pivot_table(df_ops_month,index=df_ops_month.index.month,values=columns_ops_month,aggfunc=np.sum)
            #     df_ops_month = df_ops_month.to_html(classes='data', header="true")
            #     response.context_data['sug_ops_lifting'] = df_ops_month
            #     df_ops_month = pd.DataFrame(ops_data)
            #     df_ops_month['dsb'] = df_ops_month['llt_dsb'] + df_ops_month['tlt_dsb']
            #     df_ops_month['tgi'] = df_ops_month['llt_tgi'] + df_ops_month['tlt_tgi']
            #     df_ops_month['rig1'] = df_ops_month['llt_rig1'] + df_ops_month['tlt_rig1']
            #     df_ops_month['rig2'] = df_ops_month['llt_rig2'] + df_ops_month['tlt_rig2']
            #     df_ops_month['rig3'] = df_ops_month['llt_rig3'] + df_ops_month['tlt_rig3']
            #     df_ops_month['other'] = df_ops_month['llt_other'] + df_ops_month['tlt_other']
            #     df_ops_month.index = pd.to_datetime(df_ops_month['activity_date'],format='%m/%d/%y %I:%M%p')
            #     # df_ops_month.loc['dsb'] = df_ops_month[['llt_dsb', 'tlt_dsb']].sum(axis = 1, skipna = True)
            #     columns_ops_month = ['dsb','tgi','rig1','rig2','rig3','other','rigger1','rigger2','rigger3','llt_dsb','llt_tgi','llt_rig1','llt_rig2','llt_rig3','llt_other','tlt_dsb','tlt_tgi','tlt_rig1','tlt_rig2','tlt_rig3','tlt_other','dnt_dsb','dnt_tgi','dnt_rig1','dnt_rig2','dnt_rig3','dnt_other']
            #     df_ops_month = pd.pivot_table(df_ops_month,index=df_ops_month.index.month,values=columns_ops_month,aggfunc=np.sum)
            #     df_ops_month = df_ops_month.rename({'rig1': 'RIG#1','rig2': 'RIG#2','rig3': 'RIG#3'}, axis='columns')
            #     df_ops_month = df_ops_month.to_html(classes='data', header="true")
            #     response.context_data['sug_ops_location'] = df_ops_month
                
            # if reportname == 'G':
            #     data = self.rpt_ops_records()
            
        
            results = data
            if data and dwn == 1:
                results = data
            else:
                results = []
                # results = [val for val in data]
            
            context['rpt_data'] = results
            context['rpt_table'] = df_table
            # context['dataframe'] = dataframe
            # print(results, 'results', df_table, 'df_table')
            if results:
                # print(results)
                # for res in results:
                #     print(res)
                # response.context_data['rpt_data'] = results
                open('aix/templates/aix/reports/temp.html', "w").write(render_to_string('aix/reports/result.html', {'data': context}))
                
                env = Environment(loader=FileSystemLoader('.'))
                if reportname == 'A':
                    template = env.get_template("aix/templates/aix/reports/aix_its_status_report.html")
                elif reportname == 'B':
                    template = env.get_template("aix/templates/aix/reports/equipment_report.html")
                elif reportname == 'C':
                    template = env.get_template("aix/templates/aix/reports/fet_daily_status_rpt.html")
                elif reportname == 'D':
                    template = env.get_template("aix/templates/aix/reports/faw_daily_status_rpt.html")

                print(context['fet_items_df'], 'xm')
                # print(template, 'bnm')
                data = context['results'].values()
                df = pd.DataFrame(data)
                context['rpt_customer_table'] = df.to_html()
                html  = template.render(context)
                result = BytesIO()
                pdf = pisa.pisaDocument(BytesIO(html.encode()), result)
                if not pdf.err:
                    return HttpResponse(result.getvalue(), content_type='application/pdf')
                return None
            # print(df_table, 'xm')
            return response
        return render(request, 'aix/reports/reporter.html',context)

    def rpt_daily_performance(self):
        kpi_hse_qs = KpiHseModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )
        kpi_onoff_qs = KpiOnOffModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )
        kpi_pob_qs = KpiPobModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )

        wo_task_asset_qs = WorkOrderTaskAssetModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        wo_task_personnel_qs = WorkOrderTaskPersonnelModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            )
        activity_qs = KpiOpsModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            )
        ops_qs = activity_qs.select_related('task')

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
        
        task_digest = {}
        task_digest['hse_qs'] = kpi_hse_qs
        task_digest['ops_qs'] = ops_qs
        task_digest['ops_digest'] = ops_digest
        task_digest['kpi_onoff_qs'] = kpi_onoff_qs
        task_digest['kpi_pob_qs'] = kpi_pob_qs
        task_digest['task_asset_qs'] = wo_task_asset_qs
        task_digest['task_personnel_qs'] = wo_task_personnel_qs
        # context['task_digest'] = task_digest
        # context['task_asset_qs'] = wo_task_asset_qs
        # context['task_personnel_qs'] = wo_task_personnel_qs
        # # context['task_personnel'] = wo_task_personnel_qs.values("code").annotate(Count("uuid"))
        # context['task_personnel'] = wo_task_personnel_qs.count()
        # context['task_assets'] = wo_task_asset_qs.count()

        return task_digest

    def rpt_ops_records(self):
        ops_qs = KpiOpsModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            ).select_related()
        # ops_qs = KpiOpsModel.objects.select_related('equipment_id', 'task_id')
        ops_qs = ops_qs.values('activity_date','trip_code','trip_activity','activity_time','etd','atd','eta','ata','etp','atp','kms_passed','consol_fuel','operator','banksman','rigger1','rigger2','rigger3','rigger4','section2_time_taken','section2_ton_cargo','section2_number_lifts','section2_ton_lifts','no_routine','no_simple','no_complicated','no_complex','ton_routine','ton_simple','ton_complicated','ton_complex','section3_time_taken','section3_ton_cargo','section3_number_lifts','section3_ton_lifts','llt_dsb','llt_tgi','llt_rig1','llt_rig2','llt_rig3','llt_other','tlt_dsb','tlt_tgi','tlt_rig1','tlt_rig2','tlt_rig3','tlt_other','dnt_dsb','dnt_tgi','dnt_rig1','dnt_rig2','dnt_rig3','dnt_other','equipment__license_plate', 'equipment__vehicle_type_name')
        # print(ops_qs)
        return ops_qs
    
    def rpt_hse_records(self):
        hse_qs = KpiHseModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
            ).select_related()
        
        hse_qs = hse_qs.values('activity_date','start_time','end_time','fat','lti','rwdc','mtc','fac','hipo','envdam','nmi','matloss','ptw','ptw_description','tbt','tbt_description','hht','hht_description','drills','drills_description','audit','audit_description','training_subject','reporting_cards','rc_description','safety_initiative','si_description','status')
        # print(hse_qs)
        return hse_qs

    def rpt_fet_daily_status(self):
        fet_qs = EquipmentFetModel.objects.filter(work_order=self.kwargs['work_order_pk'])
        return fet_qs 
    
    def DownLoadData(self, request):
        with BytesIO() as b:
            # data = get_analytics_data()
            data = []

            # searchstring = self.request.POST['searchstring']
            # sortby = self.request.POST['sortby']
            # orderby = self.request.POST['orderby']
            # reportname = self.request.POST['report']
            searchstring = ""
            sortby = ""
            orderby = ""
            reportname = "A"
            if reportname == 'A':
                wo_qs = WorkOrderModel.objects.for_entity(
                    entity_slug=self.kwargs['entity_slug'],
                    user_model=self.request.user
                )
                data = wo_qs
            if reportname == 'B':
                equipment_qs = EquipmentModel.objects.for_entity(
                    entity_slug=self.kwargs['entity_slug'],
                    user_model=self.request.user
                )
                data = equipment_qs
            if reportname == 'C':
                kpi_ops_qs = KpiOpsModel.objects.for_entity(
                    entity_slug=self.kwargs['entity_slug'],
                    user_model=self.request.user
                )
                data = kpi_ops_qs
            if reportname == 'D':
                # data = self.rpt_daily_performance().values()
                # data = self.rpt_ops_records().values()
                data = self.rpt_ops_records()
                # print(data)
                df = pd.DataFrame(data)
                # df.groupby(['equipment_id'])
                # df.groupby(['task_id'])['rigger1'].sum()

                # df.groupby(['task_id', 'rigger1']).agg({'rigger1': 'max'})
                # dataframe = df.to_html(classes='data', header="true")

                # sums = df.select_dtypes(pd.np.number).sum().rename('total')
                # df.append(sums)
                # df.loc['Total'] = df[['rigger1', 'rigger2']].sum()

                # df.groupby(['activity_date']).agg(
                #             sum_col3 = ('rigger1','sum'),
                #             sum_col4 = ('rigger2','sum'),
                #             ).reset_index()
                # df.groupby(['rigger1']).agg(['max']).sum()
                columns = ['etp','atp','activity_time','kms_passed','consol_fuel','operator','banksman','rigger1','rigger2','rigger3','rigger4','section2_time_taken','section2_ton_cargo','section2_number_lifts','section2_ton_lifts','no_routine','no_simple','no_complicated','no_complex','ton_routine','ton_simple','ton_complicated','ton_complex','section3_time_taken','section3_ton_cargo','section3_number_lifts','section3_ton_lifts','llt_dsb','llt_tgi','llt_rig1','llt_rig2','llt_rig3','llt_other','tlt_dsb','tlt_tgi','tlt_rig1','tlt_rig2','tlt_rig3','tlt_other','dnt_dsb','dnt_tgi','dnt_rig1','dnt_rig2','dnt_rig3','dnt_other',]
                
                # df['eta'] = pd.to_datetime(df['eta']).dt.date
                # df['eta'] = pd.to_datetime(df['eta'])
                # df['eta'] = df['eta'].apply(df['eta']).dt.second
                # df['eta'] = pd.DatetimeIndex(df['eta']).second
                # df['etp'] = df['eta'] - df['etd']
                print (df)
                df = pd.pivot_table(df, index=['activity_date', 'equipment__vehicle_type_name'],values=columns,aggfunc=np.sum)
                dataframe = df.to_html(classes='data', header="true")

                # df2 = pd.DataFrame({'A': ['18:22:28', '12:15:10']})
                df2 = pd.DataFrame(data)
                # df['eta'] = df['eta'].apply(lambda x: self.converter(x.values()))
                # df2['eta'] = pd.to_datetime(df2['eta']).dt.date
                # df['eta'] = df['eta'].apply(df['eta']).dt.second
                # df2['eta'].astype(str)
                # df2['eta'] = pd.to_timedelta(df2.eta)

                # print (df2)

            # print(data)
            # data = [{"title": "something", "price": 34, "quantity": 23}]
            # df = pd.DataFrame.from_dict(data, columns=['order_no', 'start_date', 'end_date'])
            # df = pd.DataFrame(data, columns=['title', 'price', 'quantity'])
            response = HttpResponse(content_type='application/xlsx')
            response['Content-Disposition'] = f'attachment; filename="FILENAME.xlsx"'
            with pd.ExcelWriter(response) as writer:
                df.to_excel(writer, sheet_name='SHEET NAME')

            return response

            # with pd.ExcelWriter(b) as writer:
            #     df.to_excel(writer, sheet_name="Data", index=False)

            # # PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
            # # filename = PROJECT_ROOT + f"analytics_data.xlsx"
            # filename = f'C:\\Users\\pshopi\Documents\\tech\mk\\analytics_data.xlsx'
            # res = HttpResponse(
            #     b.getvalue(),
            #     content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            # )
            # res['Content-Disposition'] = f'attachment; filename={filename}'
            # return res

    def column_calculations(self, df):
        df = self.configure_times(df)
        print(df)
        df['tot_time'] = (df['ata'] - df['atd'])*24
        df['tot_cargo'] = df['tlt_dsb'] + df['tlt_dsb'] + df['tlt_tgi'] + df['tlt_rig1'] + df['tlt_rig2'] + df['tlt_rig3'] + df['tlt_other']
        df['tot_lift_no'] = df['no_routine'] + df['no_simple'] + df['no_complicated'] + df['no_complex']
        df['tot_lift_ton'] = df['ton_routine'] + df['ton_simple'] + df['ton_complicated'] + df['ton_complex']
        df['delay_time'] = (df['atd'] - df['etd']) + (df['ata'] - df['eta'])
        
        # df['city'] = df['team'].map(lambda x: 'Atlanta' if 'A' in x else 'Boston' if 'B' in x else '')
        # df['tot_dsb'] = df['']
        def final_winner(df):
            if pd.isnull(df['tot_lift_ton']) and not pd.isnull(df['tot_lift_no']):
                return df['tot_dsb']
            elif (df['tot_lift_no']+df['tot_lift_no'])>0:
                df['tot_dsb'] = df['tot_time']*((df['llt_dsb']+df['tlt_dsb'])/(df['tot_cargo']+df['tot_lift_ton']))
                return df['tot_dsb']
            else:
                df['tot_dsb'] = df['tlt_dsb'] + df['tlt_dsb']
                return df['tot_dsb']

        df['tot_dsb'] = df.apply(final_winner, axis=1)
        return df

    
    
    def converter(x):
        hour = x.hour + (x.days * 24)
        hour = hour if hour > 9 else "0"+str(hour)
        minutes = x.minutes if minutes > 9 else "0"+str(minutes)
        seconds = x.seconds if minutes > 9 else "0"+str(seconds)
        return f"{hour}:{minutes}:{seconds}"

    def get_seconds(time_str):
        print('Time in hh:mm:ss:', time_str)
        # split in hh, mm, ss
        hh, mm, ss = time_str.split(':')
        return int(hh) * 3600 + int(mm) * 60 + int(ss)

    def get_time_hh_mm_ss(sec):
        # create timedelta and convert it into string
        td_str = str(timedelta(seconds=sec))
        print('Time in seconds:', sec)

        # split string into individual component
        x = td_str.split(':')
        print('Time in hh:mm:ss:', x[0], 'Hours', x[1], 'Minutes', x[2], 'Seconds')
        
    def configure_times(self, df):
        # df['etat'] = df['eta'].dt.strftime('%S')
        df['etat'] = pd.to_datetime(df['activity_date'].astype('str')+' '+df['eta'].astype('str'))
        df['etdt'] = pd.to_datetime(df['activity_date'].astype('str')+' '+df['etd'].astype('str'))
        df['atat'] = pd.to_datetime(df['activity_date'].astype('str')+' '+df['ata'].astype('str'))
        df['atdt'] = pd.to_datetime(df['activity_date'].astype('str')+' '+df['atd'].astype('str'))
        # print(df['etat'])
        # df['etat'] = pd.DatetimeIndex(df['etat']).second
        # df['etat'] = pd.to_timedelta(df['etat']).dt.to_seconds()
        df['etat'] = (df['etat'].dt.hour*60+df['etat'].dt.minute)*60 + df['etat'].dt.second
        df['etdt'] = (df['etdt'].dt.hour*60+df['etdt'].dt.minute)*60 + df['etdt'].dt.second
        df['atat'] = (df['atat'].dt.hour*60+df['atat'].dt.minute)*60 + df['atat'].dt.second
        df['atdt'] = (df['atdt'].dt.hour*60+df['atdt'].dt.minute)*60 + df['atdt'].dt.second
        print(df['etat'])
        return df