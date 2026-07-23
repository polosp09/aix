
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.KpiHseModelListView.as_view(), name='kpi-hse-list'),
    path('<slug:entity_slug>/create/', views.KpiHseModelCreateView.as_view(), name='kpi-hse-create'),
    path('<slug:entity_slug>/update/<uuid:kpi_hse_pk>/', views.KpiHseModelUpdateView.as_view(), name='kpi-hse-update'),
    path('<slug:entity_slug>/create/<uuid:work_order_pk>/', views.KpiHseModelCreateView.as_view(), name='kpi-hse-create-wo'),
    path('<slug:entity_slug>/update/<uuid:work_order_pk>/<uuid:kpi_hse_pk>/', views.KpiHseModelUpdateView.as_view(), name='kpi-hse-update-wo'),
    path('<slug:entity_slug>/detail/<uuid:kpi_hse_pk>/', views.KpiHseModelDetailView.as_view(), name='kpi-hse-details'),
    path('<slug:entity_slug>/report/<uuid:kpi_hse_pk>', 
          views.KpiHseModelDetailView.as_view(dwn_report_file=True), name='kpi-hse-rpt'),
]
