
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EquipmentManufacturerModelListView.as_view(), name='equipment-manufacturer-list'),
    path('<slug:entity_slug>/create/', views.EquipmentManufacturerModelCreateView.as_view(), name='equipment-manufacturer-create'),
    path('<slug:entity_slug>/update/<uuid:equipment_manufacturer_pk>/', views.EquipmentManufacturerModelUpdateView.as_view(), name='equipment-manufacturer-update'),
]
