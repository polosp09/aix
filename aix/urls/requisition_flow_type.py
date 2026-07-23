from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.RequisitionFlowTypeModelListView.as_view(), name='requisition-flow-type-list'),
    path('<slug:entity_slug>/create/', views.RequisitionFlowTypeModelCreateView.as_view(), name='requisition-flow-type-create'),
    path('<slug:entity_slug>/update/<uuid:requisition_flow_type_pk>/', views.RequisitionFlowTypeModelUpdateView.as_view(), name='requisition-flow-type-update'),
]
