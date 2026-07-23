from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EmployeeLicenseTypeModelListView.as_view(), name='employee-license-type-list'),
    path('<slug:entity_slug>/create/', views.EmployeeLicenseTypeModelCreateView.as_view(), name='employee-license-type-create'),
    path('<slug:entity_slug>/update/<uuid:employee_license_type_pk>/', views.EmployeeLicenseTypeModelUpdateView.as_view(), name='employee-license-type-update'),
]
