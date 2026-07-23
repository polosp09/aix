from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WorkOrderTaskPersonnelModelListView.as_view(), name='work-order-task-personnel-list'),
    path('<slug:entity_slug>/create/', views.WorkOrderTaskPersonnelModelCreateView.as_view(), name='work-order-task-personnel-create'),
    path('<slug:entity_slug>/update/<uuid:work_order_task_personnel_pk>/', views.WorkOrderTaskPersonnelModelUpdateView.as_view(), name='work-order-task-personnel-update'),
    path('<slug:entity_slug>/create/<uuid:work_order_task_pk>/', views.WorkOrderTaskPersonnelModelAddView.as_view(), name='work-order-task-personnel-create-wo'),
    path('<slug:entity_slug>/update/<uuid:work_order_task_pk>/<uuid:work_order_task_personnel_pk>/', views.WorkOrderTaskPersonnelModelUpdateView.as_view(), name='work-order-task-personnel-update-wo'),
]
