from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.LeaveRequestActionModelListView.as_view(), name='leave-request-action-list'),
    path('<slug:entity_slug>/create/', views.LeaveRequestActionModelCreateView.as_view(), name='leave-request-action-create'),
    path('<slug:entity_slug>/update/<uuid:leave_request_action_pk>/', views.LeaveRequestActionModelUpdateView.as_view(), name='leave-request-action-update'),
]
