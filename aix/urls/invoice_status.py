from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.InvoiceStatusModelListView.as_view(), name='invoice-status-list'),
    path('<slug:entity_slug>/create/', views.InvoiceStatusModelCreateView.as_view(), name='invoice-status-create'),
    path('<slug:entity_slug>/update/<uuid:invoice_status_pk>/', views.InvoiceStatusModelUpdateView.as_view(), name='invoice-status-update'),
]
