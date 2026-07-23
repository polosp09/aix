from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WorkOrderAssetModelListView.as_view(), name='work-order-asset-list'),
    path('<slug:entity_slug>/create/', views.WorkOrderAssetModelCreateView.as_view(), name='work-order-asset-create'),
    path('<slug:entity_slug>/update/<uuid:work_order_asset_pk>/', views.WorkOrderAssetModelUpdateView.as_view(), name='work-order-asset-update'),
    path('<slug:entity_slug>/create/<uuid:work_order_pk>/', views.WorkOrderAssetModelAddView.as_view(), name='work-order-asset-create-wo'),
    path('<slug:entity_slug>/update/<uuid:work_order_pk>/<uuid:work_order_asset_pk>/', views.WorkOrderAssetModelUpdateView.as_view(), name='work-order-asset-update-wo'),
    path('<slug:entity_slug>/update/<uuid:work_order_asset_pk>/', views.WorkOrderAssetModelDetailView.as_view(), name='work-order-asset-details'),
]
