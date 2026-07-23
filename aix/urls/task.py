from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.TaskModelListView.as_view(), name='task-list'),
    path('<slug:entity_slug>/create/', views.TaskModelCreateView.as_view(), name='task-create'),
    path('<slug:entity_slug>/update/<uuid:task_pk>/', views.TaskModelUpdateView.as_view(), name='task-update'),
]
