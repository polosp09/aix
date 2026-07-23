from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.GeneralNotificationModelListView.as_view(), name='general-notification-list'),
    path('<slug:entity_slug>/create/', views.GeneralNotificationModelCreateView.as_view(), name='general-notification-create'),
    path('<slug:entity_slug>/update/<uuid:general_notification_pk>/', views.GeneralNotificationModelUpdateView.as_view(), name='general-notification-update'),
]
