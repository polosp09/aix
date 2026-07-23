from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.InvoiceActionModelListView.as_view(), name='invoice-action-list'),
    path('<slug:entity_slug>/create/', views.InvoiceActionModelCreateView.as_view(), name='invoice-action-create'),
    path('<slug:entity_slug>/update/<uuid:invoice_action_pk>/', views.InvoiceActionModelUpdateView.as_view(), name='invoice-action-update'),
]
