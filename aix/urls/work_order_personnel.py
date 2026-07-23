from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WorkOrderPersonnelModelListView.as_view(), name='work-order-personnel-list'),
    path('<slug:entity_slug>/create/', views.WorkOrderPersonnelModelCreateView.as_view(), name='work-order-personnel-create'),
    path('<slug:entity_slug>/update/<uuid:work_order_personnel_pk>/', views.WorkOrderPersonnelModelUpdateView.as_view(), name='work-order-personnel-update'),
    path('<slug:entity_slug>/create/<uuid:work_order_pk>/', views.WorkOrderPersonnelModelAddView.as_view(), name='work-order-personnel-create-wo'),
    path('<slug:entity_slug>/update/<uuid:work_order_pk>/<uuid:work_order_personnel_pk>/', views.WorkOrderPersonnelModelUpdateView.as_view(), name='work-order-personnel-update-wo'),
    path('<slug:entity_slug>/update/<uuid:work_order_personnel_pk>/', views.WorkOrderPersonnelModelDetailView.as_view(), name='work-order-personnel-details'),
]
