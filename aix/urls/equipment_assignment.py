
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EquipmentAssignmentModelListView.as_view(), name='equipment-assignment-list'),
    path('<slug:entity_slug>/create/', views.EquipmentAssignmentModelCreateView.as_view(), name='equipment-assignment-create'),
    path('<slug:entity_slug>/update/<uuid:equipment_assignment_pk>/', views.EquipmentAssignmentModelUpdateView.as_view(), name='equipment-assignment-update'),
]
