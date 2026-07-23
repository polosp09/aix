from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WorkOrderActivityAssetModelListView.as_view(), name='work-order-activity-asset-list'),
    path('<slug:entity_slug>/create/', views.WorkOrderActivityAssetModelCreateView.as_view(), name='work-order-activity-asset-create'),
    path('<slug:entity_slug>/update/<uuid:work_order_activity_asset_pk>/', views.WorkOrderActivityAssetModelUpdateView.as_view(), name='work-order-activity-asset-update'),
    path('<slug:entity_slug>/create/<uuid:work_order_activity_pk>/', views.WorkOrderActivityAssetModelAddView.as_view(), name='work-order-activity-asset-create-act'),
    path('<slug:entity_slug>/update/<uuid:work_order_activity_asset_pk>/', views.WorkOrderActivityAssetModelUpdateView.as_view(), name='work-order-activity-asset-update'),
    path('<slug:entity_slug>/update/<uuid:work_order_activity_pk>/<uuid:work_order_activity_asset_pk>/', views.WorkOrderActivityAssetModelUpdateView.as_view(), name='work-order-activity-asset-update-act'),
    path('<slug:entity_slug>/detail/<uuid:work_order_activity_asset_pk>/', views.WorkOrderActivityAssetModelDetailView.as_view(), name='work-order-activity-asset-details'),
    path('<slug:entity_slug>/report/<uuid:work_order_activity_asset_pk>', 
          views.WorkOrderActivityAssetModelDetailView.as_view(dwn_report_file=True), name='work-order-activity-asset-rpt'),
    
]
