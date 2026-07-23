from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from aix.forms.work_order_activity_asset import WorkOrderActivityAssetForm, WorkOrderActivityAssetAddForm
from aix.models import AssetModel
from aix.models.entity import EntityModel
from aix.models.work_order_activity_asset import WorkOrderActivityAssetModel
from aix.models.work_order_task_asset import WorkOrderTaskAssetModel
from aix.models.work_order_asset import WorkOrderAssetModel
from aix.views.mixins import LoginRequiredMixIn


class WorkOrderActivityAssetModelListView(LoginRequiredMixIn, ListView):
    template_name = 'aix/app/operations/activities/details/activity_asset.html'
    context_object_name = 'work_order_activity_assets'
    PAGE_TITLE = _('WorkOrderActivityAsset List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderActivityAssetModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class WorkOrderActivityAssetModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/activities/activity_asset.html'
    PAGE_TITLE = _('Create New WorkOrderActivityAsset')
    form_class = WorkOrderActivityAssetForm
    context_object_name = 'work_order_activity_asset'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderActivityAssetForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('aix:work-order-activity-asset-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        work_order_activity_asset_model: WorkOrderActivityAssetModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        work_order_activity_asset_model.entity = entity_model
        work_order_activity_asset_model.save()
        return super().form_valid(form)


class WorkOrderActivityAssetModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'aix/app/operations/activities/activity_asset.html'
    PAGE_TITLE = _('WorkOrderActivityAsset Update')
    context_object_name = 'work_order_activity_asset'
    form_class = WorkOrderActivityAssetForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'work_order_activity_asset_pk'
    slug_field = 'uuid'

    def get_form(self, form_class=None):
        if 'work_order_activity_pk' in self.kwargs:
            entity_slug = self.kwargs['entity_slug']
            user_model = self.request.user
            asset_qs = WorkOrderActivityAssetModel.objects.for_entity(
                entity_slug=entity_slug,
                user_model=user_model
            )
            wo_asset_qs = WorkOrderAssetModel.objects.for_entity(
                entity_slug=entity_slug,
                user_model=user_model
            )
            # print(asset_qs.count(), self.kwargs['work_order_activity_pk'])
            if asset_qs.count() > 0:
                assets = asset_qs
            elif task_asset_qs.count() > 0:
                assets = task_asset_qs
            elif wo_asset_qs.count() > 0:
                assets = wo_asset_qs
            
            asset_list = AssetModel.objects.filter(uuid__in=assets.values_list('asset_id', flat=True))
            return WorkOrderActivityAssetAddForm(assets=asset_list, **self.get_form_kwargs())
        return EmployeeAssignmentForm(**self.get_form_kwargs())

    def get_queryset(self):
        return WorkOrderActivityAssetModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        if 'work_order_activity_pk' in self.kwargs:
            return reverse('aix:work-order-activity-details',
                        kwargs={
                            'entity_slug': self.kwargs['entity_slug'],
                            'work_order_activity_pk': self.kwargs['work_order_activity_pk']
                        })
        return reverse('aix:work-order-asset-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 


class WorkOrderActivityAssetModelAddView(LoginRequiredMixIn, CreateView):
    template_name = 'aix/app/operations/activities/activity_asset.html'
    PAGE_TITLE = _('Create New WorkOrderActivityAsset')
    form_class = WorkOrderActivityAssetAddForm
    context_object_name = 'work_order_activity_asset'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return WorkOrderActivityAssetAddForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_form(self, form_class=None):
        entity_slug = self.kwargs['entity_slug']
        user_model = self.request.user
        asset_qs = WorkOrderActivityAssetModel.objects.for_entity(
            entity_slug=entity_slug,
            user_model=user_model
        )
        task_asset_qs = WorkOrderTaskAssetModel.objects.for_entity(
            entity_slug=entity_slug,
            user_model=user_model
        )
        wo_asset_qs = WorkOrderAssetModel.objects.for_entity(
            entity_slug=entity_slug,
            user_model=user_model
        )
        # print(asset_qs.count(), self.kwargs['work_order_activity_pk'])
        if asset_qs.count() > 0:
            assets = asset_qs
        elif task_asset_qs.count() > 0:
            assets = task_asset_qs
        elif wo_asset_qs.count() > 0:
            assets = wo_asset_qs
        
        asset_list = AssetModel.objects.filter(uuid__in=assets.values_list('asset_id', flat=True))
        # for asset in assets:
        #     asset_list.append(asset.asset)
        #     print(asset.asset)

        # activity_model = get_object_or_404(WorkOrderActivityAssetModel, uuid=self.kwargs['work_order_activity_pk'])
        return WorkOrderActivityAssetAddForm(assets=asset_list, **self.get_form_kwargs())

    def get_success_url(self):
        return reverse('aix:work-order-activity-details',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                           'work_order_activity_pk': self.kwargs['work_order_activity_pk']
                       })

    def form_valid(self, form):
        work_order_activity_asset_model: WorkOrderActivityAssetModel = form.save(commit=False)
        entity_model_qs = EntityModel.objects.filter(slug__exact=self.kwargs['entity_slug'])
        entity_model = get_object_or_404(entity_model_qs)
        # work_order_activity_asset_model.entity = entity_model.instance,
        work_order_activity_asset_model.configure(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
        )
        work_order_activity_asset_model.activity_id = self.kwargs['work_order_activity_pk']
        work_order_activity_asset_model.entity_id = entity_model.uuid
        # print(form.cleaned_data['asset'].asset.uuid)
        # work_order_activity_asset_model.asset_id = form.cleaned_data['asset'].asset.uuid
        work_order_activity_asset_model.save()
        return super().form_valid(form)

class WorkOrderActivityAssetModelDetailView(LoginRequiredMixIn, DetailView):
    template_name = 'aix/app/operations/activities/details/activity_asset_details.html'
    context_object_name = 'work_order_activity_asset'
    PAGE_TITLE = _('WorkOrderActivityAsset Details')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'work_order_activity_asset_pk'
    slug_field = 'uuid'
    dwn_report_file = False

    def get_queryset(self):
        return WorkOrderActivityAssetModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )
    def get_success_url(self):
        return reverse('aix:work-order-activity-asset-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug'],
                            'work_order_activity_asset_pk': self.kwargs['work_order_activity_asset_pk']
                       })
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['work_order_activity_asset'] = self.get_object()
        context['entity_slug'] = self.kwargs['entity_slug']

        asset_qs = WorkOrderActivityAssetModel.objects.for_activity(
            entity_slug=self.kwargs['entity_slug'],
            work_order_activity=self.get_object().activity
        )
        document_qs = WorkOrderActivityAssetModel.objects.for_activity(
            entity_slug=self.kwargs['entity_slug'],
            work_order_activity=self.get_object().activity
        )
        personnel_qs = WorkOrderActivityAssetModel.objects.for_activity(
            entity_slug=self.kwargs['entity_slug'],
            work_order_activity=self.get_object().activity
        )
        context['assets'] = asset_qs
        context['documents'] = document_qs
        context['personnels'] = personnel_qs
        return context

    def get(self, request, *args, **kwargs):
        if self.dwn_report_file:
            # Logic to handle downloading the report file
            pass
        return super().get(request, *args, **kwargs)