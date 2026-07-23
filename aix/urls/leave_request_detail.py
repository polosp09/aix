from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.LeaveRequestDetailModelListView.as_view(), name='leave-request-detail-list'),
    path('<slug:entity_slug>/create/', views.LeaveRequestDetailModelCreateView.as_view(), name='leave-request-detail-create'),
    path('<slug:entity_slug>/update/<uuid:leave_request_detail_pk>/', views.LeaveRequestDetailModelUpdateView.as_view(), name='leave-request-detail-update'),
]
