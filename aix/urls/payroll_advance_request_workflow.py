from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.PayrollAdvanceRequestWorkflowModelListView.as_view(), name='payroll-advance-request-workflow-list'),
    path('<slug:entity_slug>/create/', views.PayrollAdvanceRequestWorkflowModelCreateView.as_view(), name='payroll-advance-request-workflow-create'),
    path('<slug:entity_slug>/update/<uuid:payroll_advance_request_workflow_pk>/', views.PayrollAdvanceRequestWorkflowModelUpdateView.as_view(), name='payroll-advance-request-workflow-update'),
]
