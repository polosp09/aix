from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.PayrollAdvanceRequestDetailModelListView.as_view(), name='payroll-advance-request-detail-list'),
    path('<slug:entity_slug>/create/', views.PayrollAdvanceRequestDetailModelCreateView.as_view(), name='payroll-advance-request-detail-create'),
    path('<slug:entity_slug>/update/<uuid:payroll_advance_request_detail_pk>/', views.PayrollAdvanceRequestDetailModelUpdateView.as_view(), name='payroll-advance-request-detail-update'),
]
