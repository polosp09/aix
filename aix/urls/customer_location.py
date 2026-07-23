
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.CustomerLocationModelListView.as_view(), name='customer-location-list'),
    path('<slug:entity_slug>/create/', views.CustomerLocationModelCreateView.as_view(), name='customer-location-create'),
    path('<slug:entity_slug>/update/<uuid:customer_location_pk>/', views.CustomerLocationModelUpdateView.as_view(), name='customer-location-update'),
]
