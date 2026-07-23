from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.CurrencyRateModelListView.as_view(), name='currency-rate-list'),
    path('<slug:entity_slug>/create/', views.CurrencyRateModelCreateView.as_view(), name='currency-rate-create'),
    path('<slug:entity_slug>/update/<uuid:currency_rate_pk>/', views.CurrencyRateModelUpdateView.as_view(), name='currency-rate-update'),
]
