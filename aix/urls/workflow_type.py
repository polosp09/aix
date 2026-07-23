from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WorkflowTypeModelListView.as_view(), name='workflow-type-list'),
    path('<slug:entity_slug>/create/', views.WorkflowTypeModelCreateView.as_view(), name='workflow-type-create'),
    path('<slug:entity_slug>/update/<uuid:workflow_type_pk>/', views.WorkflowTypeModelUpdateView.as_view(), name='workflow-type-update'),
]
