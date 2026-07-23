
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WorkOrderStatusModelListView.as_view(), name='work-order-status-list'),
    path('<slug:entity_slug>/create/', views.WorkOrderStatusModelCreateView.as_view(), name='work-order-status-create'),
    path('<slug:entity_slug>/update/<uuid:work_order_status_pk>/', views.WorkOrderStatusModelUpdateView.as_view(), name='work-order-status-update'),
]
