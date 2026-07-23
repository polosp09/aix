
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/<uuid:work_order_task_pk>/', views.KpiOpsModelListView.as_view(), name='kpi-ops-list'),
    path('<slug:entity_slug>/create/', views.KpiOpsModelCreateView.as_view(), name='kpi-ops-create'),
    path('<slug:entity_slug>/update/<uuid:kpi_ops_pk>/', views.KpiOpsModelUpdateView.as_view(), name='kpi-ops-update'),
    path('<slug:entity_slug>/create/<uuid:work_order_task_pk>/', views.KpiOpsModelCreateView.as_view(), name='kpi-ops-create-tsk'),
    path('<slug:entity_slug>/update/<uuid:work_order_task_pk>/<uuid:kpi_ops_pk>/', views.KpiOpsModelUpdateView.as_view(), name='kpi-ops-update-tsk'),
    path('<slug:entity_slug>/detail/<uuid:kpi_ops_pk>/', views.KpiOpsModelDetailView.as_view(), name='kpi-ops-details'),
    path('<slug:entity_slug>/report/<uuid:kpi_ops_pk>', 
          views.KpiOpsModelDetailView.as_view(dwn_report_file=True), name='kpi-ops-rpt'),
]
