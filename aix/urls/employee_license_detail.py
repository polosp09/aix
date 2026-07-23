from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EmployeeLicenseDetailModelListView.as_view(), name='employee-license-detail-list'),
    path('<slug:entity_slug>/create/', views.EmployeeLicenseDetailModelCreateView.as_view(), name='employee-license-detail-create'),
    path('<slug:entity_slug>/update/<uuid:employee_license_detail_pk>/', views.EmployeeLicenseDetailModelUpdateView.as_view(), name='employee-license-detail-update'),
    path('<slug:entity_slug>/create/<uuid:employee_pk>/', views.EmployeeLicenseDetailModelAddView.as_view(), name='employee-license-detail-create-employee'),
    path('<slug:entity_slug>/update/<uuid:employee_license_detail_pk>/<uuid:employee_pk>/', views.EmployeeLicenseDetailModelUpdateView.as_view(), name='employee-license-detail-update-employee'),
]
