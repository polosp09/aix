from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EmployeeOfTheWeekModelListView.as_view(), name='employee-of-the-week-list'),
    path('<slug:entity_slug>/create/', views.EmployeeOfTheWeekModelCreateView.as_view(), name='employee-of-the-week-create'),
    path('<slug:entity_slug>/update/<uuid:employee_of_the_week_pk>/', views.EmployeeOfTheWeekModelUpdateView.as_view(), name='employee-of-the-week-update'),
]
