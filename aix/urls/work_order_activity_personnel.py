from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WorkOrderActivityPersonnelModelListView.as_view(), name='work-order-activity-personnel-list'),
    path('<slug:entity_slug>/create/', views.WorkOrderActivityPersonnelModelCreateView.as_view(), name='work-order-activity-personnel-create'),
    path('<slug:entity_slug>/update/<uuid:work_order_activity_personnel_pk>/', views.WorkOrderActivityPersonnelModelUpdateView.as_view(), name='work-order-activity-personnel-update'),
    path('<slug:entity_slug>/create/<uuid:work_order_activity_pk>/', views.WorkOrderActivityPersonnelModelAddView.as_view(), name='work-order-activity-personnel-create-act'),
    path('<slug:entity_slug>/update/<uuid:work_order_activity_pk>/<uuid:work_order_activity_personnel_pk>/', views.WorkOrderActivityPersonnelModelUpdateView.as_view(), name='work-order-activity-personnel-update-act'),
    path('<slug:entity_slug>/detail/<uuid:work_order_activity_personnel_pk>/', views.WorkOrderActivityPersonnelModelDetailView.as_view(), name='work-order-activity-personnel-details'),
    path('<slug:entity_slug>/report/<uuid:work_order_activity_personnel_pk>', 
          views.WorkOrderActivityPersonnelModelDetailView.as_view(dwn_report_file=True), name='work-order-activity-personnel-rpt'), 
]
