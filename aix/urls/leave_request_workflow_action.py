from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.LeaveRequestWorkflowActionModelListView.as_view(), name='leave-request-workflow-action-list'),
    path('<slug:entity_slug>/create/', views.LeaveRequestWorkflowActionModelCreateView.as_view(), name='leave-request-workflow-action-create'),
    path('<slug:entity_slug>/update/<uuid:leave_request_workflow_action_pk>/', views.LeaveRequestWorkflowActionModelUpdateView.as_view(), name='leave-request-workflow-action-update'),
]
