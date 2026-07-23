
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WorkOrderTypeModelListView.as_view(), name='work-order-type-list'),
    path('<slug:entity_slug>/create/', views.WorkOrderTypeModelCreateView.as_view(), name='work-order-type-create'),
    path('<slug:entity_slug>/update/<uuid:work_order_type_pk>/', views.WorkOrderTypeModelUpdateView.as_view(), name='work-order-type-update'),
]
