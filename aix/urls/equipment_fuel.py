from django.urls import path

from aix import views

urlpatterns = [
    path('<slug:entity_slug>/latest/',
         views.EquipmentFuelModelListView.as_view(),
         name='equipment-fuel-list'),
    path('<slug:entity_slug>/latest/<uuid:work_order_pk>/',
         views.EquipmentFuelModelListView.as_view(),
         name='equipment-fuel-list'),
    path('<slug:entity_slug>/create/',
         views.EquipmentFuelModelCreateView.as_view(),
         name='equipment-fuel-create'),
    path('<slug:entity_slug>/create/wo/<uuid:work_order_pk>/',
         views.EquipmentFuelModelAddView.as_view(),
         name='equipment-fuel-create-wo'),
    path('<slug:entity_slug>/create/wo/<uuid:work_order_pk>/<uuid:customer_pk>/',
         views.EquipmentFuelModelCreateView.as_view(),
         name='equipment-fuel-create-customer'),
    path('<slug:entity_slug>/detail/<uuid:equipment_fuel_pk>/',
         views.EquipmentFuelModelDetailView.as_view(),
         name='equipment-fuel-details'),
    path('<slug:entity_slug>/update/<uuid:equipment_fuel_pk>/',
         views.EquipmentFuelModelUpdateView.as_view(),
         name='equipment-fuel-update'),
    path('<slug:entity_slug>/update/<uuid:work_order_pk>/<uuid:equipment_fuel_pk>/',
         views.EquipmentFuelModelUpdateView.as_view(),
         name='equipment-fuel-update-wo'),

     # reports
     path('<slug:entity_slug>/report/<uuid:equipment_fuel_pk>', 
          views.EquipmentFuelModelDetailView.as_view(dwn_report_file=True), name='equipment-fuel-rpt'),
     
]
