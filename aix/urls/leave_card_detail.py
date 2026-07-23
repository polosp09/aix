from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.LeaveCardDetailModelListView.as_view(), name='leave-card-detail-list'),
    path('<slug:entity_slug>/create/', views.LeaveCardDetailModelCreateView.as_view(), name='leave-card-detail-create'),
    path('<slug:entity_slug>/update/<uuid:leave_card_detail_pk>/', views.LeaveCardDetailModelUpdateView.as_view(), name='leave-card-detail-update'),
]
