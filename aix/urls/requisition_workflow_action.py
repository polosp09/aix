from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.RequisitionWorkflowActionModelListView.as_view(), name='requisition-workflow-action-list'),
    path('<slug:entity_slug>/create/', views.RequisitionWorkflowActionModelCreateView.as_view(), name='requisition-workflow-action-create'),
    path('<slug:entity_slug>/update/<uuid:requisition_workflow_action_pk>/', views.RequisitionWorkflowActionModelUpdateView.as_view(), name='requisition-workflow-action-update'),
]
