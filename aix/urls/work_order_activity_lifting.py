from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WorkOrderActivityLiftingModelListView.as_view(), name='work-order-activity-lifting-list'),
    path('<slug:entity_slug>/create/', views.WorkOrderActivityLiftingModelCreateView.as_view(), name='work-order-activity-lifting-create'),
    path('<slug:entity_slug>/update/<uuid:work_order_activity_lifting_pk>/', views.WorkOrderActivityLiftingModelUpdateView.as_view(), name='work-order-activity-lifting-update'),
    path('<slug:entity_slug>/create/<uuid:work_order_activity_pk>/', views.WorkOrderActivityLiftingModelAddView.as_view(), name='work-order-activity-lifting-create-act'),
    path('<slug:entity_slug>/update/<uuid:work_order_activity_lifting_pk>/', views.WorkOrderActivityLiftingModelUpdateView.as_view(), name='work-order-activity-lifting-update'),
    path('<slug:entity_slug>/update/<uuid:work_order_activity_pk>/<uuid:work_order_activity_lifting_pk>/', views.WorkOrderActivityLiftingModelUpdateView.as_view(), name='work-order-activity-lifting-update-act'),
    path('<slug:entity_slug>/detail/<uuid:work_order_activity_lifting_pk>/', views.WorkOrderActivityLiftingModelDetailView.as_view(), name='work-order-activity-lifting-details'),
    path('<slug:entity_slug>/report/<uuid:work_order_activity_lifting_pk>', 
          views.WorkOrderActivityLiftingModelDetailView.as_view(dwn_report_file=True), name='work-order-activity-lifting-rpt'),
    
]
