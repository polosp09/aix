
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/<uuid:work_order_task_pk>/', views.KpiPobModelListView.as_view(), name='kpi-pob-list'),
    path('<slug:entity_slug>/create/', views.KpiPobModelCreateView.as_view(), name='kpi-pob-create'),
    path('<slug:entity_slug>/update/<uuid:kpi_pob_pk>/', views.KpiPobModelUpdateView.as_view(), name='kpi-pob-update'),
    path('<slug:entity_slug>/create/<uuid:work_order_task_pk>/', views.KpiPobModelCreateView.as_view(), name='kpi-pob-create-wo'),
    path('<slug:entity_slug>/update/<uuid:work_order_task_pk>/<uuid:kpi_pob_pk>/', views.KpiPobModelUpdateView.as_view(), name='kpi-pob-update-wo'),
    path('<slug:entity_slug>/detail/<uuid:kpi_pob_pk>/', views.KpiPobModelDetailView.as_view(), name='kpi-pob-details'),
]
