from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.PayrollAdvanceRequestStatusModelListView.as_view(), name='payroll-advance-request-status-list'),
    path('<slug:entity_slug>/create/', views.PayrollAdvanceRequestStatusModelCreateView.as_view(), name='payroll-advance-request-status-create'),
    path('<slug:entity_slug>/update/<uuid:payroll_advance_request_status_pk>/', views.PayrollAdvanceRequestStatusModelUpdateView.as_view(), name='payroll-advance-request-status-update'),
]
