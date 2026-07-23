from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WorkflowModelListView.as_view(), name='workflow-list'),
    path('<slug:entity_slug>/create/', views.WorkflowModelCreateView.as_view(), name='workflow-create'),
    path('<slug:entity_slug>/update/<uuid:workflow_pk>/', views.WorkflowModelUpdateView.as_view(), name='workflow-update'),
]
