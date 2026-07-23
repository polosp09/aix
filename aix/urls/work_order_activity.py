
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/<uuid:work_order_task_pk>/', views.WorkOrderActivityModelListView.as_view(), name='work-order-activity-list'),
    path('<slug:entity_slug>/create/', views.WorkOrderActivityModelCreateView.as_view(), name='work-order-activity-create'),
    path('<slug:entity_slug>/update/<uuid:work_order_activity_pk>/', views.WorkOrderActivityModelUpdateView.as_view(), name='work-order-activity-update'),
    path('<slug:entity_slug>/create/<uuid:work_order_task_pk>/', views.WorkOrderActivityModelCreateView.as_view(), name='work-order-activity-create-tsk'),
    path('<slug:entity_slug>/update/<uuid:work_order_task_pk>/<uuid:work_order_activity_pk>/', views.WorkOrderActivityModelUpdateView.as_view(), name='work-order-activity-update-tsk'),
    path('<slug:entity_slug>/detail/<uuid:work_order_activity_pk>/', views.WorkOrderActivityModelDetailView.as_view(), name='work-order-activity-details'),
    path('<slug:entity_slug>/report/<uuid:work_order_activity_pk>', 
          views.WorkOrderActivityModelDetailView.as_view(dwn_report_file=True), name='work-order-activity-rpt'),
]
