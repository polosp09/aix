from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EmployeeContractTypeModelListView.as_view(), name='employee-contract-type-list'),
    path('<slug:entity_slug>/create/', views.EmployeeContractTypeModelCreateView.as_view(), name='employee-contract-type-create'),
    path('<slug:entity_slug>/update/<uuid:employee_contract_type_pk>/', views.EmployeeContractTypeModelUpdateView.as_view(), name='employee-contract-type-update'),
]
