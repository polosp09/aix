from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.TaskAssigneeModelListView.as_view(), name='task-assignee-list'),
    path('<slug:entity_slug>/create/', views.TaskAssigneeModelCreateView.as_view(), name='task-assignee-create'),
    path('<slug:entity_slug>/update/<uuid:task_assignee_pk>/', views.TaskAssigneeModelUpdateView.as_view(), name='task-assignee-update'),
]
