
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EquipmentHandoverModelListView.as_view(), name='equipment-handover-list'),
    path('<slug:entity_slug>/create/', views.EquipmentHandoverModelCreateView.as_view(), name='equipment-handover-create'),
    path('<slug:entity_slug>/update/<uuid:equipment_handover_pk>/', views.EquipmentHandoverModelUpdateView.as_view(), name='equipment-handover-update'),
    
    # Actions...
    path('<slug:entity_slug>/actions/<uuid:equipment_handover_pk>/mark-as-approved-by-hr/',
         views.EquipmentHandoverModelActionApprovedByHRView.as_view(),
         name='equipment-handover-action-mark-as-approved-by-hr'),
    path('<slug:entity_slug>/actions/<uuid:equipment_handover_pk>/mark-as-approved-by-ict/',
         views.EquipmentHandoverModelActionApprovedByICTView.as_view(),
         name='equipment-handover-action-mark-as-approved-by-ict'),
    
    # reports
    path('<slug:entity_slug>/report/<uuid:equipment_handover_pk>/',
         views.EquipmentHandoverReportView.as_view(dwn_report_file=True),
         name='equipment-handover-rpt'),
]
