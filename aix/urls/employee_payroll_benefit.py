from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EmployeePayrollBenefitModelListView.as_view(), name='employee-payroll-benefit-list'),
    path('<slug:entity_slug>/create/', views.EmployeePayrollBenefitModelCreateView.as_view(), name='employee-payroll-benefit-create'),
    path('<slug:entity_slug>/update/<uuid:employee_payroll_benefit_pk>/', views.EmployeePayrollBenefitModelUpdateView.as_view(), name='employee-payroll-benefit-update'),
]
