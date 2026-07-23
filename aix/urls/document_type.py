from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.DocumentTypeModelListView.as_view(), name='document-type-list'),
    path('<slug:entity_slug>/create/', views.DocumentTypeModelCreateView.as_view(), name='document-type-create'),
    path('<slug:entity_slug>/update/<uuid:document_type_pk>/', views.DocumentTypeModelUpdateView.as_view(), name='document-type-update'),
]
