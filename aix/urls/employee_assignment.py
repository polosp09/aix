from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EmployeeAssignmentModelListView.as_view(), name='employee-assignment-list'),
    path('<slug:entity_slug>/create/', views.EmployeeAssignmentModelCreateView.as_view(), name='employee-assignment-create'),
    path('<slug:entity_slug>/update/<uuid:employee_assignment_pk>/', views.EmployeeAssignmentModelUpdateView.as_view(), name='employee-assignment-update'),
    path('<slug:entity_slug>/create/<uuid:employee_pk>/', views.EmployeeAssignmentModelAddView.as_view(), name='employee-assignment-create-employee'),
    path('<slug:entity_slug>/update/<uuid:employee_assignment_pk>/<uuid:employee_pk>/', views.EmployeeAssignmentModelUpdateView.as_view(), name='employee-assignment-update-employee'),
]
