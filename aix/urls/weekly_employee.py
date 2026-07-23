from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WeeklyEmployeeModelListView.as_view(), name='weekly-employee-list'),
    path('<slug:entity_slug>/create/', views.WeeklyEmployeeModelCreateView.as_view(), name='weekly-employee-create'),
    path('<slug:entity_slug>/update/<uuid:weekly_employee_pk>/', views.WeeklyEmployeeModelUpdateView.as_view(), name='weekly-employee-update'),
]
