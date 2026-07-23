
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/dashboard/', views.WorkOrderModelDashboardView.as_view(), name='work-order-dashboard'),
    path('<slug:entity_slug>/list/', views.WorkOrderModelListView.as_view(), name='work-order-list'),
    path('<slug:entity_slug>/create/', views.WorkOrderModelCreateView.as_view(), name='work-order-create'),
    path('<slug:entity_slug>/update/<uuid:work_order_pk>/', views.WorkOrderModelUpdateView.as_view(), name='work-order-update'),
    path('<slug:entity_slug>/detail/<uuid:work_order_pk>/', views.WorkOrderModelDetailView.as_view(), name='work-order-details'),
    
    path('<slug:entity_slug>/actions/<uuid:work_order_pk>/mark-as-approved/',
         views.WorkOrderModelActionMarkAsApprovedView.as_view(),
         name='work-order-action-mark-as-approved'),

    path('<slug:entity_slug>/actions/<uuid:work_order_pk>/mark-as-unapproved/',
         views.WorkOrderModelActionMarkAsUnApprovedView.as_view(),
         name='work-order-action-mark-as-unapproved'),

    # reports
    path('<slug:entity_slug>/report/<uuid:work_order_pk>/',
         views.WorkOrderModelReportView.as_view(dwn_report_file=True),
         name='wo-rpt'),
    path('<slug:entity_slug>/report/<uuid:work_order_pk>/',
         views.FetDailyStatusReportView.as_view(dwn_report_file=True),
         name='fet-daily-status-rpt'),
]
