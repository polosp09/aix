from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EmployeeLanguageModelListView.as_view(), name='employee-language-list'),
    path('<slug:entity_slug>/create/', views.EmployeeLanguageModelCreateView.as_view(), name='employee-language-create'),
    path('<slug:entity_slug>/update/<uuid:employee_language_pk>/', views.EmployeeLanguageModelUpdateView.as_view(), name='employee-language-update'),
    path('<slug:entity_slug>/create/<uuid:employee_pk>/', views.EmployeeLanguageModelAddView.as_view(), name='employee-language-create-employee'),
    path('<slug:entity_slug>/update/<uuid:employee_language_pk>/<uuid:employee_pk>/', views.EmployeeLanguageModelUpdateView.as_view(), name='employee-language-update-employee'),
]
