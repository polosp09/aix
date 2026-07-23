
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from aix.forms.kpipob import KpiPobForm
from aix.models.entity import EntityModel
from aix.models.kpipob import KpiPobModel
from aix.views.mixins import LoginRequiredMixIn


class KpiPobModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/kpi/pob.html'
    context_object_name = 'pobs'
    PAGE_TITLE = _('List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return KpiPobModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class KpiPobModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/kpi/pob.html'
    PAGE_TITLE = _('Create New Kpi Pob')
    form_class = KpiPobForm
    context_object_name = 'kpipob'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill',
        'hide_menu': True
    }

    def get_queryset(self):
        return KpiPobForm.objects.for_entity(
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
        kpipob_model: KpiPobModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        kpipob_model.entity = entity_model
        # kpipob_model.work_order_id = self.kwargs['work_order_task_pk']
        kpipob_model.task_id = self.kwargs['work_order_task_pk']
        kpipob_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )
        kpipob_model.save()
        return super().form_valid(form)


class KpiPobModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/kpi/pob.html'
    PAGE_TITLE = _('Kpi P.O.B Update')
    context_object_name = 'kpipob'
    form_class = KpiPobForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'kpi_pob_pk'
    slug_field = 'uuid'

    extra_context = {
        'hide_menu': True
    }

    def get_queryset(self):
        return KpiPobModel.objects.for_entity(
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



class KpiPobModelDetailView(LoginRequiredMixIn, DetailView):
    slug_url_kwarg = 'kpi_pob_pk'
    slug_field = 'uuid'
    context_object_name = 'kpipob'
    #template_name = 'aix/advanced/work_order/work_order_detail.html'
    template_name = 'aix/app/operations/kpi/details/pob_details.html'
    extra_context = {
        'hide_menu': True
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        kpi_pob_model: KpiPobModel = self.object
        title = f'Work-Order.# {kpi_pob_model.task.work_order.order_no}'
        context['page_title'] = title
        context['header_title'] = title

        pob_forms = {}
        context['pob_forms'] = pob_forms
        
        return context

    def get_queryset(self):
        return KpiPobModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )