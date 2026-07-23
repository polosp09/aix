from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.PaymentModeModelListView.as_view(), name='payment-mode-list'),
    path('<slug:entity_slug>/create/', views.PaymentModeModelCreateView.as_view(), name='payment-mode-create'),
    path('<slug:entity_slug>/update/<uuid:payment_mode_pk>/', views.PaymentModeModelUpdateView.as_view(), name='payment-mode-update'),
]
