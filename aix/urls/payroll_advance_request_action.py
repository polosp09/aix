from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.PayrollAdvanceRequestActionModelListView.as_view(), name='payroll-advance-request-action-list'),
    path('<slug:entity_slug>/create/', views.PayrollAdvanceRequestActionModelCreateView.as_view(), name='payroll-advance-request-action-create'),
    path('<slug:entity_slug>/update/<uuid:payroll_advance_request_action_pk>/', views.PayrollAdvanceRequestActionModelUpdateView.as_view(), name='payroll-advance-request-action-update'),
]
