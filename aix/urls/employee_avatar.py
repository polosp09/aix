from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EmployeeAvatarModelListView.as_view(), name='employee-avatar-list'),
    path('<slug:entity_slug>/create/', views.EmployeeAvatarModelCreateView.as_view(), name='employee-avatar-create'),
    path('<slug:entity_slug>/update/<uuid:employee_avatar_pk>/', views.EmployeeAvatarModelUpdateView.as_view(), name='employee-avatar-update'),
]
