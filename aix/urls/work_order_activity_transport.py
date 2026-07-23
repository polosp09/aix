from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WorkOrderActivityTransportModelListView.as_view(), name='work-order-activity-transport-list'),
    path('<slug:entity_slug>/create/', views.WorkOrderActivityTransportModelCreateView.as_view(), name='work-order-activity-transport-create'),
    path('<slug:entity_slug>/update/<uuid:work_order_activity_transport_pk>/', views.WorkOrderActivityTransportModelUpdateView.as_view(), name='work-order-activity-transport-update'),
    path('<slug:entity_slug>/create/<uuid:work_order_activity_pk>/', views.WorkOrderActivityTransportModelAddView.as_view(), name='work-order-activity-transport-create-act'),
    path('<slug:entity_slug>/update/<uuid:work_order_activity_transport_pk>/', views.WorkOrderActivityTransportModelUpdateView.as_view(), name='work-order-activity-transport-update'),
    path('<slug:entity_slug>/update/<uuid:work_order_activity_pk>/<uuid:work_order_activity_transport_pk>/', views.WorkOrderActivityTransportModelUpdateView.as_view(), name='work-order-activity-transport-update-act'),
    path('<slug:entity_slug>/detail/<uuid:work_order_activity_transport_pk>/', views.WorkOrderActivityTransportModelDetailView.as_view(), name='work-order-activity-transport-details'),
    path('<slug:entity_slug>/report/<uuid:work_order_activity_transport_pk>', 
          views.WorkOrderActivityTransportModelDetailView.as_view(dwn_report_file=True), name='work-order-activity-transport-rpt'),
    
]
