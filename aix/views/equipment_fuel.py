from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.db.models import Q, Count, Sum

from aix.forms.equipment_fuel import EquipmentFuelForm, EquipmentFuelAddForm
from aix.models.entity import EntityModel
from aix.models.work_order import WorkOrderModel
from aix.models.equipment_fuel import EquipmentFuelModel
from aix.views.mixins import LoginRequiredMixIn

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
from xhtml2pdf import pisa 

import pandas as pd
from jinja2 import Environment, FileSystemLoader


class EquipmentFuelModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/fuel/fuel.html'
    context_object_name = 'equipment_fuels'
    PAGE_TITLE = _('EquipmentFuel List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EquipmentFuelModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EquipmentFuelModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/fuel/fuel.html'
    PAGE_TITLE = _('Create New EquipmentFuel')
    form_class = EquipmentFuelForm
    context_object_name = 'equipment_fuel'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EquipmentFuelForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:equipment-fuel-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        equipment_fuel_model: EquipmentFuelModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        equipment_fuel_model.entity = entity_model
        equipment_fuel_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
        )
        equipment_fuel_model.save()
        form.send(email=self.request.user.email, equipment_fuel=equipment_fuel_model)
        return super().form_valid(form)


class EquipmentFuelModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/fuel/fuel.html'
    PAGE_TITLE = _('Customer Location Update')
    context_object_name = 'equipment_fuel'
    form_class = EquipmentFuelForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'equipment_fuel_pk'
    slug_field = 'uuid'

    def get_form(self, form_class=None):
        wo_uuid = self.kwargs['work_order_pk']
        wo_qs = WorkOrderModel.objects.filter(uuid__exact=wo_uuid)
        work_order_model: WorkOrderModel = get_object_or_404(wo_qs)
        if 'equipment_fuel_pk' in self.kwargs:
            return EquipmentFuelAddForm(work_order_model, **self.get_form_kwargs())
        return EquipmentFuelForm(work_order_model, **self.get_form_kwargs())

    def get_queryset(self):
        return EquipmentFuelModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        if 'equipment_fuel_pk' in self.kwargs:
            return reverse('aix:equipment-fuel-details',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'equipment_fuel_pk': self.kwargs['equipment_fuel_pk']
                        })
        return reverse('aix:equipment-fuel-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class EquipmentFuelModelAddView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/fuel/fuel.html'
    PAGE_TITLE = _('Create New EquipmentFuel')
    form_class = EquipmentFuelAddForm
    context_object_name = 'equipment_fuel'

    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EquipmentFuelAddForm.objects.for_entity(
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
        # print(work_order_model.start_date)
        form = EquipmentFuelAddForm(work_order_model,
                                    **self.get_form_kwargs())
        return form

    def form_valid(self, form):
        equipment_fuel_model: EquipmentFuelModel = form.save(commit=False)
        entity_model_qs = EntityModel.objects.filter(slug__exact=self.kwargs['entity_slug'])
        entity_model = get_object_or_404(entity_model_qs)
        # equipment_fuel_model.entity = entity_model.instance,
        equipment_fuel_model.work_order_id = self.kwargs['work_order_pk']
        equipment_fuel_model.entity_id = entity_model.uuid
        equipment_fuel_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
        )
        equipment_fuel_model.save()
        # form.send(email=self.request.user.email, equipment_fuel=equipment_fuel_model)
        return super().form_valid(form)


class EquipmentFuelModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'equipment_fuel_pk'
    slug_field = 'uuid'
    context_object_name = 'equipment_fuel'
    #template_name = 'aix/advanced/work_order/equipment_fuel_detail.html'
    template_name = 'aix/app/operations/fuel/details/fuel_details.html'
    extra_context = {
        'hide_menu': True
    }
    dwn_report_file = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        equipment_fuel_model: EquipmentFuelModel = self.object
        customer_model: CustomerModel = equipment_fuel_model.work_order.customer
        title = f'Customer {customer_model.customer_name}'
        context['page_title'] = title
        context['header_title'] = title
        context['work_order'] = equipment_fuel_model.work_order

        ef_qs = EquipmentFuelModel.objects.for_wo(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user,
                work_order=equipment_fuel_model.work_order
            )
        context['equipment_fuel_items'] = ef_qs

        wo_qs = ef_qs.select_related('work_order')
        
        equipment_fuel_digest = {}
        context['equipment_fuel_digest'] = equipment_fuel_digest
                
        equipment_fuel_forms = {}
        context['equipment_fuel_forms'] = equipment_fuel_forms
        context['fuel_cost'] = equipment_fuel_model.fuel_qty*equipment_fuel_model.fuel_price
        
        return context

    def get_queryset(self):
        return EquipmentFuelModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get(self, request, *args, **kwargs):
        response = super(EquipmentFuelModelDetailView, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        # print('data', self.dwn_report_file)
        if self.dwn_report_file:
            # data = CustomerModel.objects.all().order_by('customer_name')
            open('aix/templates/aix/reports/temp.html', "w").write(render_to_string('aix/reports/result.html', {'data': context}))
            
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template("aix/templates/aix/reports/fuel_rpt.html")
            
            data = context['equipment_fuel_items']
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