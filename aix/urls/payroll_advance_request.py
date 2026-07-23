from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.PayrollAdvanceRequestModelListView.as_view(), name='payroll-advance-request-list'),
    path('<slug:entity_slug>/create/', views.PayrollAdvanceRequestModelCreateView.as_view(), name='payroll-advance-request-create'),
    path('<slug:entity_slug>/update/<uuid:payroll_advance_request_pk>/', views.PayrollAdvanceRequestModelUpdateView.as_view(), name='payroll-advance-request-update'),
]
