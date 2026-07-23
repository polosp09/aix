
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from aix.forms.kpionoff import KpiOnOffForm
from aix.models.entity import EntityModel
from aix.models.kpionoff import KpiOnOffModel
from aix.views.mixins import LoginRequiredMixIn


class KpiOnOffModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/kpi/onoff.html'
    context_object_name = 'onoffs'
    PAGE_TITLE = _('List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return KpiOnOffModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class KpiOnOffModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/kpi/onoff.html'
    PAGE_TITLE = _('Create New Kpi OnOff')
    form_class = KpiOnOffForm
    context_object_name = 'kpionoff'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    extra_context = {
        'hide_menu': True
    }

    def get_queryset(self):
        return KpiOnOffForm.objects.for_entity(
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
        kpionoff_model: KpiOnOffModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        kpionoff_model.entity = entity_model
        # kpionoff_model.work_order_id = self.kwargs['work_order_task_pk']
        kpionoff_model.task_id = self.kwargs['work_order_task_pk']
        kpionoff_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )
        kpionoff_model.save()
        return super().form_valid(form)


class KpiOnOffModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/kpi/onoff.html'
    PAGE_TITLE = _('Kpi OnOff Update')
    context_object_name = 'kpionoff'
    form_class = KpiOnOffForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'kpi_onoff_pk'
    slug_field = 'uuid'
    extra_context = {
        'hide_menu': True
    }

    def get_queryset(self):
        return KpiOnOffModel.objects.for_entity(
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
        form.save()
        return super().form_valid(form) 



class KpiOnOffModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'kpi_onoff_pk'
    slug_field = 'uuid'
    context_object_name = 'kpionoff'
    #template_name = 'aix/advanced/work_order/work_order_detail.html'
    template_name = 'aix/app/operations/kpi/details/onoff_details.html'
    extra_context = {
        'hide_menu': True
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        kpi_onoff_model: KpiOnOffModel = self.object
        title = f'Work-Order.# {kpi_onoff_model.task.work_order.order_no} TASK.#: {kpi_onoff_model.task.tripno}'
        context['page_title'] = title
        context['header_title'] = title

        onoff_forms = {}
        context['onoff_forms'] = onoff_forms
        return context

    def get_queryset(self):
        return KpiOnOffModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )