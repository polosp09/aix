from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.PayrollAdvanceRequestWorkflowActionModelListView.as_view(), name='payroll-advance-request-workflow-action-list'),
    path('<slug:entity_slug>/create/', views.PayrollAdvanceRequestWorkflowActionModelCreateView.as_view(), name='payroll-advance-request-workflow-action-create'),
    path('<slug:entity_slug>/update/<uuid:payroll_advance_request_workflow_action_pk>/', views.PayrollAdvanceRequestWorkflowActionModelUpdateView.as_view(), name='payroll-advance-request-workflow-action-update'),
]
