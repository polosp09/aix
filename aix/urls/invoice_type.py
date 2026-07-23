from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.InvoiceTypeModelListView.as_view(), name='invoice-type-list'),
    path('<slug:entity_slug>/create/', views.InvoiceTypeModelCreateView.as_view(), name='invoice-type-create'),
    path('<slug:entity_slug>/update/<uuid:invoice_type_pk>/', views.InvoiceTypeModelUpdateView.as_view(), name='invoice-type-update'),
]
