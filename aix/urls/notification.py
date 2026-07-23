
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.NotificationModelListView.as_view(), name='notification-list'),
    path('<slug:entity_slug>/create/', views.NotificationModelCreateView.as_view(), name='notification-create'),
    path('<slug:entity_slug>/update/<uuid:notification_pk>/', views.NotificationModelUpdateView.as_view(), name='notification-update'),
]
