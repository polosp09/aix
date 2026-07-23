from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView, RedirectView
from django.views.generic.detail import SingleObjectMixin

from aix.forms.route_survey import RouteSurveyForm
from aix.models.entity import EntityModel
from aix.models.route_survey import RouteSurveyModel
from aix.models.route_survey_info import RouteSurveyInfoModel
from aix.views.mixins import LoginRequiredMixIn

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string
from xhtml2pdf import pisa 

import pandas as pd
from jinja2 import Environment, FileSystemLoader

class RouteSurveyModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/route_survey.html'
    context_object_name = 'route_surveys'
    PAGE_TITLE = _('RouteSurvey List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RouteSurveyModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class RouteSurveyModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/route_survey.html'
    PAGE_TITLE = _('Create New RouteSurvey')
    form_class = RouteSurveyForm
    context_object_name = 'route_survey'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RouteSurveyForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:route-survey-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        route_survey_model: RouteSurveyModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        route_survey_model.entity = entity_model
        route_survey_model.start_place = route_survey_model.start_gps
        route_survey_model.via_place = route_survey_model.via_gps
        route_survey_model.end_place = route_survey_model.end_gps
        route_survey_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
        )
        route_survey_model.save()
        return super().form_valid(form)


class RouteSurveyModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/route_survey.html'
    PAGE_TITLE = _('RouteSurvey Update')
    context_object_name = 'route_survey'
    form_class = RouteSurveyForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'route_survey_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return RouteSurveyModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:route-survey-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        route_survey_model: RouteSurveyModel = form.save(commit=False)
        route_survey_model.start_place = route_survey_model.start_gps
        route_survey_model.via_place = route_survey_model.via_gps
        route_survey_model.end_place = route_survey_model.end_gps
        route_survey_model.save()
        return super().form_valid(form) 


class RouteSurveyModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'route_survey_pk'
    slug_field = 'uuid'
    context_object_name = 'route_survey'
    template_name = 'aix/app/operations/route_survey_detail.html'
    extra_context = {
        'header_subtitle_icon': 'uil:invoice',
        'hide_menu': True
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        route_survey_model: RouteSurveyModel = self.object
        title = f'Code {route_survey_model.code}'
        context['page_title'] = title
        context['header_title'] = title

        route_survey_model: RouteSurveyModel = self.object
        rs_points_qs, item_data = route_survey_model.get_rs_item_data(
            queryset= RouteSurveyInfoModel.objects.filter(route_survey=route_survey_model).select_related('route_survey')
        )
        print(rs_points_qs.count())
        context['rs_points'] = rs_points_qs
        return context

    def get_queryset(self):
        return RouteSurveyModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related('entity')


# Reports

class RouteSurveyReportView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'route_survey_pk'
    slug_field = 'uuid'
    context_object_name = 'route_survey_model'
    template_name = 'aix/app/operations/route_survey.html'
    extra_context = {
        'header_subtitle_icon': 'uil:invoice',
        'hide_menu': True
    }
    dwn_report_file = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        route_survey_model: RouteSurveyModel = self.object
        title = f'Route Survey Report'
        context['page_title'] = title
        context['header_title'] = title

        route_survey_model: RouteSurveyModel = self.object
        context['route_survey'] = route_survey_model
        route_survey_point_qs = RouteSurveyInfoModel.objects.filter(route_survey=route_survey_model)
        context['rs_points'] = route_survey_point_qs
        return context

    def get_queryset(self):
        return RouteSurveyModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related('entity')

    def get(self, request, *args, **kwargs):
        response = super(RouteSurveyReportView, self).get(request, *args, **kwargs)
        context = self.get_context_data()
        if self.dwn_report_file:
            open('aix/templates/aix/reports/temp.html', "w").write(render_to_string('aix/reports/result.html', {'data': context}))
            
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template("aix/templates/aix/reports/route_survey_rpt.html")
            data = context['rs_points'].values()
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
class BaseRouteSurveyActionView(LoginRequiredMixIn, RedirectView, SingleObjectMixin):
    http_method_names = ['get']
    pk_url_kwarg = 'route_survey_pk'
    action_name = None
    commit = True

    def get_queryset(self):
        return RouteSurveyModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_redirect_url(self, *args, **kwargs):
        return reverse('aix:route-survey-list',
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
        response = super(BaseRouteSurveyActionView, self).get(request, *args, **kwargs)
        ce_model: RouteSurveyModel = self.get_object()

        try:
            getattr(ce_model, self.action_name)(commit=self.commit, **kwargs)
        except ValidationError as e:
            messages.add_message(request,
                                 message=e.message,
                                 level=messages.ERROR,
                                 extra_tags='is-danger')
        return response


class RouteSurveyModelActionApprovedByHRView(BaseRouteSurveyActionView):
    action_name = 'mark_as_approved_by_hr'

class RouteSurveyModelActionApprovedByICTView(BaseRouteSurveyActionView):
    action_name = 'mark_as_approved_by_ict'