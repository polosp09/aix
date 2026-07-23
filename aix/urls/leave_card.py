from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.LeaveCardModelListView.as_view(), name='leave-card-list'),
    path('<slug:entity_slug>/create/', views.LeaveCardModelCreateView.as_view(), name='leave-card-create'),
    path('<slug:entity_slug>/update/<uuid:leave_card_pk>/', views.LeaveCardModelUpdateView.as_view(), name='leave-card-update'),
    path('<slug:entity_slug>/create/<uuid:employee_pk>/', views.LeaveCardModelAddView.as_view(), name='leave-card-create-employee'),
    path('<slug:entity_slug>/update/<uuid:leave_card_pk>/<uuid:employee_pk>/', views.LeaveCardModelUpdateView.as_view(), name='leave-card-update-employee'),
]
