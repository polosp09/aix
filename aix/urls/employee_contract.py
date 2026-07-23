from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EmployeeContractModelListView.as_view(), name='employee-contract-list'),
    path('<slug:entity_slug>/create/', views.EmployeeContractModelCreateView.as_view(), name='employee-contract-create'),
    path('<slug:entity_slug>/update/<uuid:employee_contract_pk>/', views.EmployeeContractModelUpdateView.as_view(), name='employee-contract-update'),
    path('<slug:entity_slug>/create/<uuid:employee_pk>/', views.EmployeeContractModelAddView.as_view(), name='employee-contract-create-employee'),
    path('<slug:entity_slug>/update/<uuid:employee_contract_pk>/<uuid:employee_pk>/', views.EmployeeContractModelUpdateView.as_view(), name='employee-contract-update-employee'),
]
