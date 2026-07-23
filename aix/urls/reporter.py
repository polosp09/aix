from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.ReportModelListView.as_view(), name='report-list'),
    path('<slug:entity_slug>/create/', views.ReportModelCreateView.as_view(), name='report-create'),
    path('<slug:entity_slug>/update/<uuid:report_pk>/', views.ReportModelUpdateView.as_view(), name='report-update'),
    path('<slug:entity_slug>/preview/', views.ReporterFilterView.as_view(), name='report-filter'),
    path('<slug:entity_slug>/preview/results/', 
            views.ReportResultsView.as_view(search_string=None, report=None, sort_by=None, order_by=None, work_order=None), name='report-filter-results'),
    path('<slug:entity_slug>/export/', views.ReportResultsView.as_view(search_string=None, report=None, sort_by=None, order_by=None, dwn_report_file=True), name='report-export'),
]
