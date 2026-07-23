
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.SalaryModelListView.as_view(), name='salary-list'),
    path('<slug:entity_slug>/create/', views.SalaryModelCreateView.as_view(), name='salary-create'),
    path('<slug:entity_slug>/update/<uuid:salary_pk>/', views.SalaryModelUpdateView.as_view(), name='salary-update'),
]
