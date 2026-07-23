from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.IncomingDocumentTypeModelListView.as_view(), name='incoming-document-type-list'),
    path('<slug:entity_slug>/create/', views.IncomingDocumentTypeModelCreateView.as_view(), name='incoming-document-type-create'),
    path('<slug:entity_slug>/update/<uuid:incoming_document_type_pk>/', views.IncomingDocumentTypeModelUpdateView.as_view(), name='incoming-document-type-update'),
]
