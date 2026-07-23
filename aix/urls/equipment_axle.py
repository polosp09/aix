
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EquipmentAxleModelListView.as_view(), name='equipment-axle-list'),
    path('<slug:entity_slug>/create/', views.EquipmentAxleModelCreateView.as_view(), name='equipment-axle-create'),
    path('<slug:entity_slug>/update/<uuid:equipment_axle_pk>/', views.EquipmentAxleModelUpdateView.as_view(), name='equipment-axle-update'),
]
