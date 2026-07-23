from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.TaskStatusModelListView.as_view(), name='task-status-list'),
    path('<slug:entity_slug>/create/', views.TaskStatusModelCreateView.as_view(), name='task-status-create'),
    path('<slug:entity_slug>/update/<uuid:task_status_pk>/', views.TaskStatusModelUpdateView.as_view(), name='task-status-update'),
]
