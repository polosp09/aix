from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.RequisitionActionModelListView.as_view(), name='requisition-action-list'),
    path('<slug:entity_slug>/create/', views.RequisitionActionModelCreateView.as_view(), name='requisition-action-create'),
    path('<slug:entity_slug>/update/<uuid:requisition_action_pk>/', views.RequisitionActionModelUpdateView.as_view(), name='requisition-action-update'),
]
