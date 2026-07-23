
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.DepartmentModelListView.as_view(), name='department-list'),
    path('<slug:entity_slug>/create/', views.DepartmentModelCreateView.as_view(), name='department-create'),
    path('<slug:entity_slug>/update/<uuid:department_pk>/', views.DepartmentModelUpdateView.as_view(), name='department-update'),
]
