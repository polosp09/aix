from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.AixItsStatusReportModelListView.as_view(), name='aix-its-status-report-list'),
    path('<slug:entity_slug>/create/', views.AixItsStatusReportModelCreateView.as_view(), name='aix-its-status-report-create'),
    path('<slug:entity_slug>/update/<uuid:aix_its_status_report_pk>/', views.AixItsStatusReportModelUpdateView.as_view(), name='aix-its-status-report-update'),
    
    # reports
    path('<slug:entity_slug>/report/<uuid:aix_its_status_report_pk>/',
         views.AixItsStatusReportReportView.as_view(dwn_report_file=True),
         name='aix-its-status-report-rpt'),
]
