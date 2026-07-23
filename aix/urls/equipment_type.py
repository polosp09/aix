
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EquipmentTypeModelListView.as_view(), name='equipment-type-list'),
    path('<slug:entity_slug>/create/', views.EquipmentTypeModelCreateView.as_view(), name='equipment-type-create'),
    path('<slug:entity_slug>/update/<uuid:equipment_type_pk>/', views.EquipmentTypeModelUpdateView.as_view(), name='equipment-type-update'),
]
