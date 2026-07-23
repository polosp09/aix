from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from aix.forms.route_survey_info import RouteSurveyInfoForm, RouteSurveyInfoAddForm
from aix.models.entity import EntityModel
from aix.models.route_survey_info import RouteSurveyInfoModel
from aix.views.mixins import LoginRequiredMixIn


class RouteSurveyInfoModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/route-survey-info.html'
    context_object_name = 'route_survey_infos'
    PAGE_TITLE = _('RouteSurveyInfo List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RouteSurveyInfoModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class RouteSurveyInfoModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/route_survey_info.html'
    PAGE_TITLE = _('Create New RouteSurveyInfo')
    form_class = RouteSurveyInfoForm
    context_object_name = 'route_survey_info'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RouteSurveyInfoForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:route-survey-info-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        route_survey_info_model: RouteSurveyInfoModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        route_survey_info_model.entity = entity_model
        route_survey_info_model.save()
        return super().form_valid(form)


class RouteSurveyInfoModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/route_survey_info.html'
    PAGE_TITLE = _('RouteSurveyInfo Update')
    context_object_name = 'route_survey_info'
    form_class = RouteSurveyInfoForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'route_survey_info_pk'
    slug_field = 'uuid'

    def get_form(self, form_class=None):
        if 'route_survey_pk' in self.kwargs:
            return RouteSurveyInfoAddForm(**self.get_form_kwargs())
        return EmployeeAssignmentForm(**self.get_form_kwargs())

    def get_queryset(self):
        return RouteSurveyInfoModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        if 'route_survey_pk' in self.kwargs:
            return reverse('aix:work-order-details',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'route_survey_pk': self.kwargs['route_survey_pk']
                        })
        return reverse('aix:route-survey-info-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class RouteSurveyInfoModelAddView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/route_survey_info.html'
    PAGE_TITLE = _('Create New RouteSurveyInfo')
    form_class = RouteSurveyInfoAddForm
    context_object_name = 'route_survey_info'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return RouteSurveyInfoAddForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:route-survey-details',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'route_survey_pk': self.kwargs['route_survey_pk']
                       })

    def form_valid(self, form):
        route_survey_info_model: RouteSurveyInfoModel = form.save(commit=False)
        entity_model_qs = EntityModel.objects.filter(slug__exact=self.kwargs['entity_slug'])
        entity_model = get_object_or_404(entity_model_qs)
        # route_survey_info_model.entity = entity_model.instance,
        # print(self.kwargs['route_survey_pk'])
        route_survey_info_model.route_survey_id = self.kwargs['route_survey_pk']
        route_survey_info_model.entity_id = entity_model.uuid
        route_survey_info_model.save()
        return super().form_valid(form)



class RouteSurveyInfoModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'route_survey_info_pk'
    slug_field = 'uuid'
    context_object_name = 'route_survey_info'
    #template_name = 'aix/advanced/route_survey/route_survey_detail.html'
    template_name = 'aix/app/operations/details/wo_personnel_detail.html'
    extra_context = {
        'hide_menu': True
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        wo_personnel_model: RouteSurveyInfoModel = self.object
        title = f'Personnel {wo_personnel_model.code}'
        context['page_title'] = title
        context['header_title'] = title

        wo_personnel_forms = {}
        context['wo_personnel_forms'] = wo_personnel_forms
        
        return context

    def get_queryset(self):
        return RouteSurveyInfoModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )