from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WorkflowActionModelListView.as_view(), name='workflow-action-list'),
    path('<slug:entity_slug>/create/', views.WorkflowActionModelCreateView.as_view(), name='workflow-action-create'),
    path('<slug:entity_slug>/update/<uuid:workflow_action_pk>/', views.WorkflowActionModelUpdateView.as_view(), name='workflow-action-update'),
]
