from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.RequisitionWorkflowModelListView.as_view(), name='requisition-workflow-list'),
    path('<slug:entity_slug>/create/', views.RequisitionWorkflowModelCreateView.as_view(), name='requisition-workflow-create'),
    path('<slug:entity_slug>/update/<uuid:requisition_workflow_pk>/', views.RequisitionWorkflowModelUpdateView.as_view(), name='requisition-workflow-update'),
]
