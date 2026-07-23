
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EquipmentModelListView.as_view(), name='equipment-list'),
    path('<slug:entity_slug>/create/', views.EquipmentModelCreateView.as_view(), name='equipment-create'),
    path('<slug:entity_slug>/update/<uuid:equipment_pk>/', views.EquipmentModelUpdateView.as_view(), name='equipment-update'),
]
