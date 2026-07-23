from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.RequisitionModelListView.as_view(), name='requisition-list'),
    path('<slug:entity_slug>/create/', views.RequisitionModelCreateView.as_view(), name='requisition-create'),
    path('<slug:entity_slug>/update/<uuid:requisition_pk>/', views.RequisitionModelUpdateView.as_view(), name='requisition-update'),
]
