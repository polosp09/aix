from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from aix.forms.aix_its_status_report import AixItsStatusReportForm
from aix.models.entity import EntityModel
from aix.models.aix_its_status_report import AixItsStatusReportModel
from aix.views.mixins import LoginRequiredMixIn

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
from xhtml2pdf import pisa 

import pandas as pd
from jinja2 import Environment, FileSystemLoader


class AixItsStatusReportModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/settings/aix_its_status_report.html'
    context_object_name = 'aix_its_status_reports'
    PAGE_TITLE = _('Its Status Report List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return AixItsStatusReportModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class AixItsStatusReportModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/settings/aix_its_status_report.html'
    PAGE_TITLE = _('Create New AixItsStatusReport')
    form_class = AixItsStatusReportForm
    context_object_name = 'aix_its_status_report'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return AixItsStatusReportForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:aix-its-status-report-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        aix_its_status_report_model: AixItsStatusReportModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        aix_its_status_report_model.entity = entity_model
        aix_its_status_report_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
        )
        aix_its_status_report_model.save()
        return super().form_valid(form)


class AixItsStatusReportModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/settings/aix_its_status_report.html'
    PAGE_TITLE = _('AixItsStatusReport Update')
    context_object_name = 'aix_its_status_report'
    form_class = AixItsStatusReportForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'aix_its_status_report_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return AixItsStatusReportModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:aix-its-status-report-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 



# Reports

class AixItsStatusReportReportView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'aix_its_status_report_pk'
    slug_field = 'uuid'
    context_object_name = 'aix_its_status_report_model'
    template_name = 'aix/app/settings/aix_its_status_report.html'
    extra_context = {
        'header_subtitle_icon': 'uil:invoice',
        'hide_menu': True
    }
    dwn_report_file = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        aix_its_status_report_model: AixItsStatusReportModel = self.object
        title = f'Status Report Details'
        context['page_title'] = title
        context['header_title'] = title

        aix_its_status_report_model: AixItsStatusReportModel = self.object
        aix_its_status_report_items_qs = AixItsStatusReportModel.objects.all()
        context['aix_its_status_report_items'] = aix_its_status_report_items_qs
        return context

    def get_queryset(self):
        return AixItsStatusReportModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related('entity')

    def get(self, request, *args, **kwargs):
        response = super(AixItsStatusReportReportView, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        if self.dwn_report_file:
            open('aix/templates/aix/reports/temp.html', "w").write(render_to_string('aix/reports/result.html', {'data': context}))
            
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template("aix/templates/aix/reports/aix_its_status_report_rpt.html")
            data = context['aix_its_status_report_items'].values()
            df = pd.DataFrame(data)
            context['rpt_customer_table'] = df.to_html()
            html  = template.render(context)
            result = BytesIO()
            pdf = pisa.pisaDocument(BytesIO(html.encode()), result)
            if not pdf.err:
                return HttpResponse(result.getvalue(), content_type='application/pdf')
            return None
        
        return response