from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EmployeePayrollModelListView.as_view(), name='employee-payroll-list'),
    path('<slug:entity_slug>/create/', views.EmployeePayrollModelCreateView.as_view(), name='employee-payroll-create'),
    path('<slug:entity_slug>/update/<uuid:employee_payroll_pk>/', views.EmployeePayrollModelUpdateView.as_view(), name='employee-payroll-update'),
    path('<slug:entity_slug>/create/<uuid:employee_pk>/', views.EmployeePayrollModelAddView.as_view(), name='employee-payroll-create-employee'),
    path('<slug:entity_slug>/update/<uuid:employee_payroll_pk>/<uuid:employee_pk>/', views.EmployeePayrollModelUpdateView.as_view(), name='employee-payroll-update-employee'),
]
