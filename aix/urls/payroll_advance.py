from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.PayrollAdvanceModelListView.as_view(), name='payroll-advance-list'),
    path('<slug:entity_slug>/create/', views.PayrollAdvanceModelCreateView.as_view(), name='payroll-advance-create'),
    path('<slug:entity_slug>/update/<uuid:payroll_advance_pk>/', views.PayrollAdvanceModelUpdateView.as_view(), name='payroll-advance-update'),
]
