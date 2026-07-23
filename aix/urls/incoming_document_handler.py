from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.IncomingDocumentHandlerModelListView.as_view(), name='incoming-document-handler-list'),
    path('<slug:entity_slug>/create/', views.IncomingDocumentHandlerModelCreateView.as_view(), name='incoming-document-handler-create'),
    path('<slug:entity_slug>/update/<uuid:incoming_document_handler_pk>/', views.IncomingDocumentHandlerModelUpdateView.as_view(), name='incoming-document-handler-update'),
]
