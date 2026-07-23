
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EquipmentJoinModelListView.as_view(), name='equipment-join-list'),
    path('<slug:entity_slug>/create/', views.EquipmentJoinModelCreateView.as_view(), name='equipment-join-create'),
    path('<slug:entity_slug>/update/<uuid:equipment_join_pk>/', views.EquipmentJoinModelUpdateView.as_view(), name='equipment-join-update'),
]
