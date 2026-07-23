from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.RequisitionCategoryModelListView.as_view(), name='requisition-category-list'),
    path('<slug:entity_slug>/create/', views.RequisitionCategoryModelCreateView.as_view(), name='requisition-category-create'),
    path('<slug:entity_slug>/update/<uuid:requisition_category_pk>/', views.RequisitionCategoryModelUpdateView.as_view(), name='requisition-category-update'),
]
