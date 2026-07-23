from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.db.models import Q, Count, Sum

from aix.forms.work_order_task import WorkOrderTaskForm, WorkOrderTaskAddForm
from aix.forms.document import DocumentForm
from aix.models.document import DocumentModel
from aix.models.entity import EntityModel
from aix.models.work_order import WorkOrderModel
from aix.models.work_order_activity import WorkOrderActivityModel
from aix.models.work_order_jobcard import WorkOrderJobcardModel
from aix.models.work_order_task import WorkOrderTaskModel
from aix.models.work_order_task_asset import WorkOrderTaskAssetModel
from aix.models.work_order_task_personnel import WorkOrderTaskPersonnelModel
from aix.models.kpiops import KpiOpsModel
from aix.models.kpionoff import KpiOnOffModel
from aix.models.kpipob import KpiPobModel
from aix.views.mixins import LoginRequiredMixIn

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
from xhtml2pdf import pisa 

import pandas as pd
from jinja2 import Environment, FileSystemLoader


class WorkOrderTaskModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/task/task.html'
    context_object_name = 'work_order_tasks'
    PAGE_TITLE = _('WorkOrderTask List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderTaskModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WorkOrderTaskModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/task/task.html'
    PAGE_TITLE = _('Create New WorkOrderTask')
    form_class = WorkOrderTaskForm
    context_object_name = 'work_order_task'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderTaskForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-task-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        work_order_task_model: WorkOrderTaskModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        work_order_task_model.entity = entity_model
        work_order_task_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
        )
        work_order_task_model.save()
        form.send(email=self.request.user.email, work_order_task=work_order_task_model)
        return super().form_valid(form)


class WorkOrderTaskModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/task/task.html'
    PAGE_TITLE = _('WorkOrder Task Update')
    context_object_name = 'work_order_task'
    form_class = WorkOrderTaskForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'work_order_task_pk'
    slug_field = 'uuid'

    def get_form(self, form_class=None):
        if 'work_order_task_pk' in self.kwargs:
            work_order_task_pk = self.kwargs['work_order_task_pk']
            task_model: WorkOrderTaskModel = WorkOrderTaskModel.objects.filter(pk=work_order_task_pk)
            task = get_object_or_404(task_model)
            return WorkOrderTaskAddForm(**self.get_form_kwargs(), work_order=task.work_order)
        return WorkOrderTaskForm(**self.get_form_kwargs())

    def get_queryset(self):
        return WorkOrderTaskModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        if 'work_order_task_pk' in self.kwargs:
            return reverse('aix:work-order-details',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'work_order_pk': self.kwargs['work_order_pk']
                        })
        return reverse('aix:work-order-task-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class WorkOrderTaskModelAddView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/task/task.html'
    PAGE_TITLE = _('Create New WorkOrderTask')
    form_class = WorkOrderTaskAddForm
    context_object_name = 'work_order_task'

    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    # def get(self, entity_slug, **kwargs):
    #     response = super(WorkOrderTaskModelAddView, self).get(request, entity_slug, **kwargs)

    #     wo_qs = WorkOrderModel.objects.for_entity(
    #         entity_slug=self.kwargs['entity_slug'],
    #         user_model=self.request.user
    #     )
    #     work_order_model: WorkOrderModel = get_object_or_404(wo_qs, uuid__exact=self.kwargs['work_order_pk'])

    #     return response

    def get_queryset(self):
        return WorkOrderTaskAddForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-details',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'work_order_pk': self.kwargs['work_order_pk']
                       })

    def get_form(self, form_class=None):
        entity_slug = self.kwargs['entity_slug']
        wo_uuid = self.kwargs['work_order_pk']
        wo_qs = WorkOrderModel.objects.filter(uuid__exact=wo_uuid)
        work_order_model: WorkOrderModel = get_object_or_404(wo_qs)
        print(work_order_model.start_date)
        form = WorkOrderTaskAddForm(work_order_model,
                                    **self.get_form_kwargs())
        return form

    def form_valid(self, form):
        work_order_task_model: WorkOrderTaskModel = form.save(commit=False)
        entity_model_qs = EntityModel.objects.filter(slug__exact=self.kwargs['entity_slug'])
        entity_model = get_object_or_404(entity_model_qs)
        # work_order_task_model.entity = entity_model.instance,
        work_order_task_model.work_order_id = self.kwargs['work_order_pk']
        work_order_task_model.entity_id = entity_model.uuid
        work_order_task_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
        )
        work_order_task_model.save()
        form.send(email=self.request.user.email, work_order_task=work_order_task_model)
        return super().form_valid(form)
        # try:
        #     self.instance = WorkOrderTaskModel.objects.get(entity=entity_model, 
        #                         startdate=work_order_task_model.startdate,
        #                         enddate=work_order_task_model.enddate,
        #                         work_order_id=self.kwargs['work_order_pk'],
        #                         startlocation=work_order_task_model.startlocation,
        #                         endlocation = work_order_task_model.endlocation)
            
        # except WorkOrderTaskModel.DoesNotExist:
        #     work_order_task_model.save()
        #     messages.add_message(self.request,
        #                      messages.ERROR,
        #                      f'Task {work_order_task_model.tripno} Duplicate Entry.',
        #                      extra_tags='is-error')
        #     form.send(email=self.request.user.email, work_order_task=work_order_task_model)
        # return super().form_valid(form)


class WorkOrderTaskModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'work_order_task_pk'
    slug_field = 'uuid'
    context_object_name = 'work_order_task'
    #template_name = 'aix/advanced/work_order/work_order_task_detail.html'
    template_name = 'aix/app/operations/task/details/task_details.html'
    extra_context = {
        'hide_menu': True
    }
    dwn_report_file = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        work_order_task_model: WorkOrderTaskModel = self.object
        customer_model: CustomerModel = work_order_task_model.work_order.customer
        title = f'Customer {customer_model.customer_name}'
        context['page_title'] = title
        context['header_title'] = title

        
        jcd_qs = WorkOrderJobcardModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                # work_order=work_order_model
            )
        context['wo_qs'] = jcd_qs

        wo_qs = jcd_qs.select_related('work_order')

        kpi_onoff_qs = KpiOnOffModel.objects.for_task(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                task=work_order_task_model
            )
        kpi_pob_qs = KpiPobModel.objects.for_task(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                task=work_order_task_model
            )
        ops_qs = KpiOpsModel.objects.for_task(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                task=work_order_task_model
            ).select_related('task')

        wo_task_asset_qs = WorkOrderTaskAssetModel.objects.for_task(
                entity_slug=self.kwargs['entity_slug'],
                work_order_task=work_order_task_model
            )
        wo_task_personnel_qs = WorkOrderTaskPersonnelModel.objects.for_task(
                entity_slug=self.kwargs['entity_slug'],
                work_order_task=work_order_task_model
            )
        document_qs = DocumentModel.objects.for_task(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                task=work_order_task_model
            )
        # wo_equipment_qs = work_order_task_model.work_order.equipment.all()
        activity_qs = WorkOrderActivityModel.objects.for_task(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                task=work_order_task_model
            ).select_related('task')

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
        task_digest['ops_qs'] = ops_qs
        task_digest['ops_digest'] = ops_digest
        task_digest['kpi_onoff_qs'] = kpi_onoff_qs
        task_digest['kpi_pob_qs'] = kpi_pob_qs
        task_digest['task_asset_qs'] = wo_task_asset_qs
        task_digest['task_personnel_qs'] = wo_task_personnel_qs
        task_digest['document_qs'] = document_qs
        task_digest['activity_qs'] = activity_qs
        context['task_digest'] = task_digest
        context['task_asset_qs'] = wo_task_asset_qs
        context['task_personnel_qs'] = wo_task_personnel_qs
        # context['task_personnel'] = wo_task_personnel_qs.values("code").annotate(Count("uuid"))
        context['task_personnel'] = wo_task_personnel_qs.count()
        context['task_assets'] = wo_task_asset_qs.count()
        context['task_activites'] = activity_qs.count()
        
        task_forms = {}
        task_forms['document_form'] = DocumentForm()
        context['task_forms'] = task_forms
        
        return context

    def get_queryset(self):
        return WorkOrderTaskModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get(self, request, *args, **kwargs):
        response = super(WorkOrderTaskModelDetailView, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        # print('data', self.dwn_report_file)
        if self.dwn_report_file:
            # data = CustomerModel.objects.all().order_by('customer_name')
            open('aix/templates/aix/reports/temp.html', "w").write(render_to_string('aix/reports/result.html', {'data': context}))
            
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template("aix/templates/aix/reports/task_rpt.html")
            
            data = context['wo_qs']
            # print(data)
            df = pd.DataFrame.from_dict(data)
            # df = pd.DataFrame.from_dict(data.values('order_no'))
            # df = pd.DataFrame(list(data))
            # context['asset'] = df.to_html()
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