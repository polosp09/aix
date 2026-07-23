from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EngagementNotifyWithModelListView.as_view(), name='engagement-notify-with-list'),
    path('<slug:entity_slug>/create/', views.EngagementNotifyWithModelCreateView.as_view(), name='engagement-notify-with-create'),
    path('<slug:entity_slug>/update/<uuid:engagement_notify_with_pk>/', views.EngagementNotifyWithModelUpdateView.as_view(), name='engagement-notify-with-update'),
]
