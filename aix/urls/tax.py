from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.TaxModelListView.as_view(), name='tax-list'),
    path('<slug:entity_slug>/create/', views.TaxModelCreateView.as_view(), name='tax-create'),
    path('<slug:entity_slug>/update/<uuid:tax_pk>/', views.TaxModelUpdateView.as_view(), name='tax-update'),
]
