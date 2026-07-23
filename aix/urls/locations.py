from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.LocationModelListView.as_view(), name='location-list'),
    path('<slug:entity_slug>/create/', views.LocationModelCreateView.as_view(), name='location-create'),
    path('<slug:entity_slug>/update/<uuid:location_pk>/', views.LocationModelUpdateView.as_view(), name='location-update'),
]
