from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WorkflowActionTypeModelListView.as_view(), name='workflow-action-type-list'),
    path('<slug:entity_slug>/create/', views.WorkflowActionTypeModelCreateView.as_view(), name='workflow-action-type-create'),
    path('<slug:entity_slug>/update/<uuid:workflow_action_type_pk>/', views.WorkflowActionTypeModelUpdateView.as_view(), name='workflow-action-type-update'),
]
