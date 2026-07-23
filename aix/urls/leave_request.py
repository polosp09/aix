from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.LeaveRequestModelListView.as_view(), name='leave-request-list'),
    path('<slug:entity_slug>/create/', views.LeaveRequestModelCreateView.as_view(), name='leave-request-create'),
    path('<slug:entity_slug>/update/<uuid:leave_request_pk>/', views.LeaveRequestModelUpdateView.as_view(), name='leave-request-update'),
]
