from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.LeaveRequestWorkflowModelListView.as_view(), name='leave-request-workflow-list'),
    path('<slug:entity_slug>/create/', views.LeaveRequestWorkflowModelCreateView.as_view(), name='leave-request-workflow-create'),
    path('<slug:entity_slug>/update/<uuid:leave_request_workflow_pk>/', views.LeaveRequestWorkflowModelUpdateView.as_view(), name='leave-request-workflow-update'),
]
