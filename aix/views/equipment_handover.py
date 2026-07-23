from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView, RedirectView
from django.views.generic.detail import SingleObjectMixin

from aix.forms.equipment_handover import EquipmentHandoverForm
from aix.models.entity import EntityModel
from aix.models.employee import EmployeeModel
from aix.models.equipment_handover import EquipmentHandoverModel
from aix.views.mixins import LoginRequiredMixIn

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
from xhtml2pdf import pisa 

import pandas as pd
from jinja2 import Environment, FileSystemLoader

class EquipmentHandoverModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/equipment/equipment_handover.html'
    context_object_name = 'equipment_handovers'
    PAGE_TITLE = _('EquipmentHandover List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EquipmentHandoverModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class EquipmentHandoverModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/equipment/equipment_handover.html'
    PAGE_TITLE = _('Create New EquipmentHandover')
    form_class = EquipmentHandoverForm
    context_object_name = 'equipment_handover'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return EquipmentHandoverForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:equipment-handover-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        equipment_handover_model: EquipmentHandoverModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        equipment_handover_model.entity = entity_model
        equipment_handover_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
        )
        equipment_handover_model.save()
        return super().form_valid(form)


class EquipmentHandoverModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/equipment/equipment_handover.html'
    PAGE_TITLE = _('EquipmentHandover Update')
    context_object_name = 'equipment_handover'
    form_class = EquipmentHandoverForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'equipment_handover_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return EquipmentHandoverModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:equipment-handover-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


# Reports

class EquipmentHandoverReportView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'equipment_handover_pk'
    slug_field = 'uuid'
    context_object_name = 'equipment_handover_model'
    template_name = 'aix/app/equipment/equipment_handover.html'
    extra_context = {
        'header_subtitle_icon': 'uil:invoice',
        'hide_menu': True
    }
    dwn_report_file = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        equipment_handover_model: EquipmentHandoverModel = self.object
        title = f'Status Report Details'
        context['page_title'] = title
        context['header_title'] = title

        equipment_handover_model: EquipmentHandoverModel = self.object
        equipment_handover_items_qs = EquipmentHandoverModel.objects.all()
        context['equipment_handover_items'] = equipment_handover_items_qs
        return context

    def get_queryset(self):
        return EquipmentHandoverModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related('entity')

    def get(self, request, *args, **kwargs):
        response = super(EquipmentHandoverReportView, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        if self.dwn_report_file:
            open('aix/templates/aix/reports/temp.html', "w").write(render_to_string('aix/reports/result.html', {'data': context}))
            
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template("aix/templates/aix/reports/equipment_handover_rpt.html")
            data = context['equipment_handover_items'].values()
            df = pd.DataFrame(data)
            context['rpt_customer_table'] = df.to_html()
            html  = template.render(context)
            result = BytesIO()
            pdf = pisa.pisaDocument(BytesIO(html.encode()), result)
            if not pdf.err:
                return HttpResponse(result.getvalue(), content_type='application/pdf')
            return None
        
        return response


# ACTION VIEWS...
class BaseEquipmentHandoverActionView(LoginRequiredMixIn, RedirectView, SingleObjectMixin):
    http_method_names = ['get']
    pk_url_kwarg = 'equipment_handover_pk'
    action_name = None
    commit = True

    def get_queryset(self):
        return EquipmentHandoverModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_redirect_url(self, *args, **kwargs):
        return reverse('aix:equipment-handover-list',
                       kwargs={
                           'entity_slug': kwargs['entity_slug']
                       })

    def get(self, request, *args, **kwargs):
        user_id = self.request.user.id
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        kwargs['entity_slug'] = entity_model.slug
        kwargs['user_id'] = user_id
        
        if not self.action_name:
            raise ImproperlyConfigured('View attribute action_name is required.')
        response = super(BaseEquipmentHandoverActionView, self).get(request, *args, **kwargs)
        ce_model: EquipmentHandoverModel = self.get_object()

        try:
            getattr(ce_model, self.action_name)(commit=self.commit, **kwargs)
        except ValidationError as e:
            messages.add_message(request,
                                 message=e.message,
                                 level=messages.ERROR,
                                 extra_tags='is-danger')
        return response


class EquipmentHandoverModelActionApprovedByHRView(BaseEquipmentHandoverActionView):
    action_name = 'mark_as_approved_by_hr'

class EquipmentHandoverModelActionApprovedByICTView(BaseEquipmentHandoverActionView):
    action_name = 'mark_as_approved_by_ict'