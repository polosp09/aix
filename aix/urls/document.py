from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.DocumentModelListView.as_view(), name='document-list'),
    path('<slug:entity_slug>/create/', views.DocumentModelCreateView.as_view(), name='document-create'),
    path('<slug:entity_slug>/update/<uuid:document_pk>/', views.DocumentModelUpdateView.as_view(), name='document-update'),
    path('<slug:entity_slug>/wo-upload/<uuid:work_order_pk>/', views.DocumentModelCreateView.as_view(upload_file='wo'), name='document-upload-wo'),
    path('<slug:entity_slug>/task-upload/<uuid:work_order_task_pk>/', views.DocumentModelCreateView.as_view(upload_file='task'), name='document-upload-wo-task'),
    path('<slug:entity_slug>/activity-upload/<uuid:work_order_activity_pk>/', views.DocumentModelCreateView.as_view(upload_file='activity'), name='document-upload-wo-activity'),
]
