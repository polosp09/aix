from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WorkOrderTaskAssetModelListView.as_view(), name='work-order-task-asset-list'),
    path('<slug:entity_slug>/create/', views.WorkOrderTaskAssetModelCreateView.as_view(), name='work-order-task-asset-create'),
    path('<slug:entity_slug>/update/<uuid:work_order_task_asset_pk>/', views.WorkOrderTaskAssetModelUpdateView.as_view(), name='work-order-task-asset-update'),
    path('<slug:entity_slug>/create/<uuid:work_order_task_pk>/', views.WorkOrderTaskAssetModelAddView.as_view(), name='work-order-task-asset-create-wo'),
    path('<slug:entity_slug>/update/<uuid:work_order_task_pk>/<uuid:work_order_task_asset_pk>/', views.WorkOrderTaskAssetModelUpdateView.as_view(), name='work-order-task-asset-update-wo'),
]
