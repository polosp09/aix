
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EmployeeModelListView.as_view(), name='employee-list'),
    path('<slug:entity_slug>/create/', views.EmployeeModelCreateView.as_view(), name='employee-create'),
    path('<slug:entity_slug>/update/<uuid:employee_pk>/', views.EmployeeModelUpdateView.as_view(), name='employee-update'),
    path('<slug:entity_slug>/detail/<uuid:employee_pk>/', views.EmployeeModelDetailView.as_view(), name='employee-details'),
    path('<slug:entity_slug>/pull/', views.EmployeeModelPullView.as_view(), name='employee-pull'),
]
