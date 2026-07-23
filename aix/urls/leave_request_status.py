from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.LeaveRequestStatusModelListView.as_view(), name='leave-request-status-list'),
    path('<slug:entity_slug>/create/', views.LeaveRequestStatusModelCreateView.as_view(), name='leave-request-status-create'),
    path('<slug:entity_slug>/update/<uuid:leave_request_status_pk>/', views.LeaveRequestStatusModelUpdateView.as_view(), name='leave-request-status-update'),
]
