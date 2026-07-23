
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WorkOrderJobcardStatusModelListView.as_view(), name='work-order-jobcard-status-list'),
    path('<slug:entity_slug>/create/', views.WorkOrderJobcardStatusModelCreateView.as_view(), name='work-order-jobcard-status-create'),
    path('<slug:entity_slug>/update/<uuid:work_order_jobcard_status_pk>/', views.WorkOrderJobcardStatusModelUpdateView.as_view(), name='work-order-jobcard-status-update'),
]
