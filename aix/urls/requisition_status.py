from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.RequisitionStatusModelListView.as_view(), name='requisition-status-list'),
    path('<slug:entity_slug>/create/', views.RequisitionStatusModelCreateView.as_view(), name='requisition-status-create'),
    path('<slug:entity_slug>/update/<uuid:requisition_status_pk>/', views.RequisitionStatusModelUpdateView.as_view(), name='requisition-status-update'),
]
