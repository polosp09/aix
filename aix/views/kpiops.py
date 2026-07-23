from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from aix.forms.kpiops import KpiOpsForm
from aix.models.entity import EntityModel
from aix.models.kpiops import KpiOpsModel
from aix.models.work_order_task import WorkOrderTaskModel
from aix.views.mixins import LoginRequiredMixIn

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
from xhtml2pdf import pisa 

import pandas as pd
from jinja2 import Environment, FileSystemLoader

class KpiOpsModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/kpi/ops.html'
    context_object_name = 'activities'
    PAGE_TITLE = _('List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill',
        'hide_menu': True
    }

    def get_queryset(self):
        return KpiOpsModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        task_qs = WorkOrderTaskModel.objects.all()
        work_order_task_model: WorkOrderTaskModel = get_object_or_404(task_qs, uuid__exact=self.kwargs['work_order_task_pk'])
        context['task'] = work_order_task_model
        return context


class KpiOpsModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/kpi/ops.html'
    PAGE_TITLE = _('Create New Kpi Ops')
    form_class = KpiOpsForm
    context_object_name = 'kpiops'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    extra_context = {
        'hide_menu': True
    }

    def get_queryset(self):
        return KpiOpsForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )
    
    def get_form(self, form_class=None):
        entity_slug = self.kwargs['entity_slug']
        wo_task_uuid = self.kwargs['work_order_task_pk']
        wo_task_qs = WorkOrderTaskModel.objects.filter(uuid__exact=wo_task_uuid)
        work_order_task_model: WorkOrderTaskModel = get_object_or_404(wo_task_qs)
        # print(work_order_task_model.start_date)
        form = KpiOpsForm(work_order_task_model,
                                    **self.get_form_kwargs())
        return form

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        task_qs = WorkOrderTaskModel.objects.all()
        work_order_task_model: WorkOrderTaskModel = get_object_or_404(task_qs, uuid__exact=self.kwargs['work_order_task_pk'])
        context['task'] = work_order_task_model
        return context

    def get_success_url(self):
        return reverse('aix:work-order-task-details',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'work_order_task_pk': self.kwargs['work_order_task_pk']
                       }) 

    def form_valid(self, form):
        kpiops_model: KpiOpsModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        kpiops_model.entity = entity_model
        kpiops_model.task_id = self.kwargs['work_order_task_pk']
        kpiops_model.trip_code = self.kwargs['work_order_task_pk']
        kpiops_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )
        kpiops_model.configure_times(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
                )
        kpiops_model.save()
        form.send(email=self.request.user.email, kpiops=kpiops_model)
        return super().form_valid(form)

class KpiOpsModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/kpi/ops.html'
    PAGE_TITLE = _('Kpi Ops Update')
    context_object_name = 'kpiops'
    form_class = KpiOpsForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'kpi_ops_pk'
    slug_field = 'uuid'
    extra_context = {
        'hide_menu': True
    }

    def get_queryset(self):
        return KpiOpsModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-task-details',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'work_order_task_pk': self.kwargs['work_order_task_pk']
                       })

    def form_valid(self, form):
        kpi_ops_model: KpiOpsModel = form.save(commit=False)
        kpi_ops_model.configure_times(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
                )
        kpi_ops_model.save()
        form.save()
        return super().form_valid(form) 

class KpiOpsModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'kpi_ops_pk'
    slug_field = 'uuid'
    context_object_name = 'kpiops'
    #template_name = 'aix/advanced/work_order/work_order_task_detail.html'
    template_name = 'aix/app/operations/task/details/activity_detail.html'
    extra_context = {
        'hide_menu': True
    }
    dwn_report_file = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        kpi_ops_model: KpiOpsModel = self.object
        title = f'Activity {kpi_ops_model.task.tripno}'
        context['page_title'] = title
        context['header_title'] = title

        context['qs'] = {'name': ['a', 'b', 'c'],}
        ops_digest = {}
        ops_digest['personnel'] = 0
        ops_digest['assets'] = 0
        ops_digest['inspections'] = 0
        ops_digest['incidents'] = 0
        context['ops_digest'] = ops_digest

        activity_forms = {}
        context['activity_forms'] = activity_forms
        
        return context

    def get_queryset(self):
        return KpiOpsModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )


    def get(self, request, *args, **kwargs):
        response = super(KpiOpsModelDetailView, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        # print('data', self.dwn_report_file)
        if self.dwn_report_file:
            # data = CustomerModel.objects.all().order_by('customer_name')
            open('aix/templates/aix/reports/temp.html', "w").write(render_to_string('aix/reports/result.html', {'data': context}))
            
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template("aix/templates/aix/reports/kpi_ops_rpt.html")
            
            data = context['qs']
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