from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.CurrencyModelListView.as_view(), name='currency-list'),
    path('<slug:entity_slug>/create/', views.CurrencyModelCreateView.as_view(), name='currency-create'),
    path('<slug:entity_slug>/update/<uuid:currency_pk>/', views.CurrencyModelUpdateView.as_view(), name='currency-update'),
]
