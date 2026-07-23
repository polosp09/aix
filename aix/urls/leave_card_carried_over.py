from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.LeaveCardCarriedOverModelListView.as_view(), name='leave-card-carried-over-list'),
    path('<slug:entity_slug>/create/', views.LeaveCardCarriedOverModelCreateView.as_view(), name='leave-card-carried-over-create'),
    path('<slug:entity_slug>/update/<uuid:leave_card_carried_over_pk>/', views.LeaveCardCarriedOverModelUpdateView.as_view(), name='leave-card-carried-over-update'),
]
