from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WorkOrderActivityDocumentModelListView.as_view(), name='work-order-activity-document-list'),
    path('<slug:entity_slug>/create/', views.WorkOrderActivityDocumentModelCreateView.as_view(), name='work-order-activity-document-create'),
    path('<slug:entity_slug>/update/<uuid:work_order_activity_document_pk>/', views.WorkOrderActivityDocumentModelUpdateView.as_view(), name='work-order-activity-document-update'),
    path('<slug:entity_slug>/create/<uuid:work_order_activity_pk>/', views.WorkOrderActivityDocumentModelAddView.as_view(), name='work-order-activity-document-create-act'),
    path('<slug:entity_slug>/update/<uuid:work_order_activity_document_pk>/', views.WorkOrderActivityDocumentModelUpdateView.as_view(), name='work-order-activity-document-update'),
    path('<slug:entity_slug>/update/<uuid:work_order_activity_pk>/<uuid:work_order_activity_document_pk>/', views.WorkOrderActivityDocumentModelUpdateView.as_view(), name='work-order-activity-document-update-act'),
    path('<slug:entity_slug>/detail/<uuid:work_order_activity_document_pk>/', views.WorkOrderActivityDocumentModelDetailView.as_view(), name='work-order-activity-document-details'),
    path('<slug:entity_slug>/report/<uuid:work_order_activity_document_pk>', 
          views.WorkOrderActivityDocumentModelDetailView.as_view(dwn_report_file=True), name='work-order-activity-document-rpt'),
    
]
