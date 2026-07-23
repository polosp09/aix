from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.IncomingDocumentModelListView.as_view(), name='incoming-document-list'),
    path('<slug:entity_slug>/create/', views.IncomingDocumentModelCreateView.as_view(), name='incoming-document-create'),
    path('<slug:entity_slug>/update/<uuid:incoming_document_pk>/', views.IncomingDocumentModelUpdateView.as_view(), name='incoming-document-update'),
]
