from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.NotificationTrackerModelListView.as_view(), name='notification-tracker-list'),
    path('<slug:entity_slug>/create/', views.NotificationTrackerModelCreateView.as_view(), name='notification-tracker-create'),
    path('<slug:entity_slug>/update/<uuid:notification_tracker_pk>/', views.NotificationTrackerModelUpdateView.as_view(), name='notification-tracker-update'),
]
