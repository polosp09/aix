from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.DocumentStatusModelListView.as_view(), name='document-status-list'),
    path('<slug:entity_slug>/create/', views.DocumentStatusModelCreateView.as_view(), name='document-status-create'),
    path('<slug:entity_slug>/update/<uuid:document_status_pk>/', views.DocumentStatusModelUpdateView.as_view(), name='document-status-update'),
]
