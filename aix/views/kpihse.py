
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from aix.forms.kpihse import KpiHseForm
from aix.models.entity import EntityModel
from aix.models.kpihse import KpiHseModel
from aix.views.mixins import LoginRequiredMixIn

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
from xhtml2pdf import pisa 

import pandas as pd
from jinja2 import Environment, FileSystemLoader

class KpiHseModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/kpi/hse.html'
    context_object_name = 'kpihses'
    PAGE_TITLE = _('List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return KpiHseModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class KpiHseModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/kpi/hse.html'
    PAGE_TITLE = _('Create New Kpi Hse')
    form_class = KpiHseForm
    context_object_name = 'kpihse'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return KpiHseForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:kpi-hse-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                        #    'work_order_pk': self.kwargs['work_order_pk']
                       }) 

    def form_valid(self, form):
        kpihse_model: KpiHseModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        kpihse_model.entity = entity_model
        # kpihse_model.task_id = self.kwargs['work_order_pk']
        kpihse_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )
        kpihse_model.configure_times(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
                )
        kpihse_model.save()
        return super().form_valid(form)


class KpiHseModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/kpi/hse.html'
    PAGE_TITLE = _('Kpi Hse Update')
    context_object_name = 'kpihse'
    form_class = KpiHseForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'kpi_hse_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return KpiHseModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-details',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'work_order_pk': self.kwargs['work_order_pk']
                       })

    def form_valid(self, form):
        kpi_hse_model: KpiHseModel = form.save(commit=False)
        kpi_hse_model.configure_times(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
                )
        form.save()
        return super().form_valid(form) 



class KpiHseModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'kpi_hse_pk'
    slug_field = 'uuid'
    context_object_name = 'kpihse'
    #template_name = 'aix/advanced/work_order/work_order_detail.html'
    template_name = 'aix/app/operations/details/hse_detail.html'
    extra_context = {
        'hide_menu': True
    }
    dwn_report_file = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        kpi_hse_model: KpiHseModel = self.object
        title = f'Activity {kpi_hse_model.code}'
        context['page_title'] = title
        context['header_title'] = title

        context['qs'] = {'name': ['a', 'b', 'c'],}
        hse_forms = {}
        context['hse_forms'] = hse_forms
        
        return context

    def get_queryset(self):
        return KpiHseModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get(self, request, *args, **kwargs):
        response = super(KpiHseModelDetailView, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        # print('data', self.dwn_report_file)
        if self.dwn_report_file:
            # data = CustomerModel.objects.all().order_by('customer_name')
            open('aix/templates/aix/reports/temp.html', "w").write(render_to_string('aix/reports/result.html', {'data': context}))
            
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template("aix/templates/aix/reports/kpi_hse_rpt.html")
            
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