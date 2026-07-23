from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WorkflowStatusModelListView.as_view(), name='workflow-status-list'),
    path('<slug:entity_slug>/create/', views.WorkflowStatusModelCreateView.as_view(), name='workflow-status-create'),
    path('<slug:entity_slug>/update/<uuid:workflow_status_pk>/', views.WorkflowStatusModelUpdateView.as_view(), name='workflow-status-update'),
]
