
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/<uuid:work_order_task_pk>/', views.KpiOnOffModelListView.as_view(), name='kpi-onoff-list'),
    path('<slug:entity_slug>/create/', views.KpiOnOffModelCreateView.as_view(), name='kpi-onoff-create'),
    path('<slug:entity_slug>/update/<uuid:kpi_onoff_pk>/', views.KpiOnOffModelUpdateView.as_view(), name='kpi-onoff-update'),
    path('<slug:entity_slug>/create/<uuid:work_order_task_pk>/', views.KpiOnOffModelCreateView.as_view(), name='kpi-onoff-create-wo'),
    path('<slug:entity_slug>/update/<uuid:work_order_task_pk>/<uuid:kpi_onoff_pk>/', views.KpiOnOffModelUpdateView.as_view(), name='kpi-onoff-update-wo'),
    path('<slug:entity_slug>/detail/<uuid:kpi_onoff_pk>/', views.KpiOnOffModelDetailView.as_view(), name='kpi-onoff-details'),
]
