from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from aix.forms.work_order_activity import WorkOrderActivityForm, WorkOrderActivityAddForm
from aix.forms.document import DocumentForm
from aix.models.document import DocumentModel
from aix.models.entity import EntityModel
from aix.models.work_order_activity import WorkOrderActivityModel
from aix.models.work_order_activity_asset import WorkOrderActivityAssetModel
from aix.models.work_order_activity_lifting import WorkOrderActivityLiftingModel
from aix.models.work_order_activity_document import WorkOrderActivityDocumentModel
from aix.models.work_order_activity_personnel import WorkOrderActivityPersonnelModel
from aix.models.work_order_activity_transport import WorkOrderActivityTransportModel
from aix.models.work_order_task import WorkOrderTaskModel
from aix.views.mixins import LoginRequiredMixIn

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
from xhtml2pdf import pisa 

import pandas as pd
from jinja2 import Environment, FileSystemLoader
from aix.models.work_order_activity_transport import WorkOrderActivityTransportModel

class WorkOrderActivityModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/activities/activity.html'
    context_object_name = 'work_order_activities'
    PAGE_TITLE = _('List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill',
        'hide_menu': True
    }

    def get_queryset(self):
        return WorkOrderActivityModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        task_qs = WorkOrderTaskModel.objects.all()
        work_order_task_model: WorkOrderTaskModel = get_object_or_404(task_qs, uuid__exact=self.kwargs['work_order_task_pk'])
        context['task'] = work_order_task_model
        return context


class WorkOrderActivityModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/activities/activity.html'
    PAGE_TITLE = _('Create New Work Order Activity')
    form_class = WorkOrderActivityForm
    context_object_name = 'work_order_activity'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    extra_context = {
        'hide_menu': True
    }

    def get_queryset(self):
        return WorkOrderActivityForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )
    
    def get_form(self, form_class=None):
        entity_slug = self.kwargs['entity_slug']
        wo_task_uuid = self.kwargs['work_order_task_pk']
        wo_task_qs = WorkOrderTaskModel.objects.filter(uuid__exact=wo_task_uuid)
        work_order_task_model: WorkOrderTaskModel = get_object_or_404(wo_task_qs)
        # print(work_order_task_model.start_date)
        form = WorkOrderActivityForm(work_order_task_model,
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
        work_order_activity_model: WorkOrderActivityModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        work_order_activity_model.entity = entity_model
        work_order_activity_model.task_id = self.kwargs['work_order_task_pk']
        work_order_activity_model.work_code = self.kwargs['work_order_task_pk']
        work_order_activity_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )
        work_order_activity_model.configure_times(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
                )
        work_order_activity_model.save()
        # form.send(email=self.request.user.email, work_order_activity=work_order_activity_model)
        return super().form_valid(form)

class WorkOrderActivityModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/activities/activity.html'
    PAGE_TITLE = _('Work Order Activity Update')
    context_object_name = 'work_order_activity'
    form_class = WorkOrderActivityForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'work_order_activity_pk'
    slug_field = 'uuid'
    extra_context = {
        'hide_menu': True
    }

    def get_queryset(self):
        return WorkOrderActivityModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_form(self, form_class=None):
        entity_slug = self.kwargs['entity_slug']
        wo_task_uuid = self.kwargs['work_order_task_pk']
        wo_task_qs = WorkOrderTaskModel.objects.filter(uuid__exact=wo_task_uuid)
        work_order_task_model: WorkOrderTaskModel = get_object_or_404(wo_task_qs)
        # print(work_order_task_model.start_date)
        form = WorkOrderActivityForm(work_order_task_model,
                                    **self.get_form_kwargs())
        return form

    def get_success_url(self):
        return reverse('aix:work-order-task-details',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'work_order_task_pk': self.kwargs['work_order_task_pk']
                       })

    def form_valid(self, form):
        work_order_activity_model: WorkOrderActivityModel = form.save(commit=False)
        work_order_activity_model.configure_times(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
                )
        work_order_activity_model.save()
        form.save()
        return super().form_valid(form) 

class WorkOrderActivityModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'work_order_activity_pk'
    slug_field = 'uuid'
    context_object_name = 'activity'
    #template_name = 'aix/advanced/work_order/work_order_task_detail.html'
    template_name = 'aix/app/operations/activities/details/activity_detail.html'
    extra_context = {
        'hide_menu': True
    }
    dwn_report_file = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        work_order_activity_model: WorkOrderActivityModel = self.object
        title = f'Activity {work_order_activity_model.task.tripno}'
        context['page_title'] = title
        context['header_title'] = title

        context['qs'] = {'name': ['a', 'b', 'c'],}
        
        wo_activity_asset_qs = WorkOrderActivityAssetModel.objects.for_activity(
                entity_slug=self.kwargs['entity_slug'],
                work_order_activity=work_order_activity_model
            )
        wo_activity_personnel_qs = WorkOrderActivityPersonnelModel.objects.for_activity(
                entity_slug=self.kwargs['entity_slug'],
                work_order_activity=work_order_activity_model
            )
        wo_activity_document_qs = DocumentModel.objects.for_activity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                work_order_activity=work_order_activity_model
            )
        wo_activity_lifting_qs = WorkOrderActivityLiftingModel.objects.for_activity(
                entity_slug=self.kwargs['entity_slug'],
                work_order_activity=work_order_activity_model
            )
        wo_activity_transport_qs = WorkOrderActivityTransportModel.objects.for_activity(
                entity_slug=self.kwargs['entity_slug'],
                work_order_activity=work_order_activity_model
            )
        
        activity_digest = {}
        activity_digest['activity'] = work_order_activity_model
        activity_digest['personnel'] = wo_activity_personnel_qs
        activity_digest['assets'] = wo_activity_asset_qs
        activity_digest['documents'] = wo_activity_document_qs
        activity_digest['liftings'] = wo_activity_lifting_qs
        activity_digest['transports'] = wo_activity_transport_qs
        activity_digest['no_assets'] = wo_activity_asset_qs.count
        activity_digest['operators'] = wo_activity_personnel_qs.filter(employee__designation='Crane Operator').count
        activity_digest['banksmen'] = wo_activity_personnel_qs.filter(employee__designation='Banksman').count
        context['activity_digest'] = activity_digest

        activity_forms = {}
        activity_forms['document_form'] = DocumentForm()
        context['activity_forms'] = activity_forms
        
        return context

    def get_queryset(self):
        return WorkOrderActivityModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )


    def get(self, request, *args, **kwargs):
        response = super(WorkOrderActivityModelDetailView, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        # print('data', self.dwn_report_file)
        if self.dwn_report_file:
            # data = CustomerModel.objects.all().order_by('customer_name')
            open('aix/templates/aix/reports/temp.html', "w").write(render_to_string('aix/reports/result.html', {'data': context}))
            
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template("aix/templates/aix/reports/activity_rpt.html")
            
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