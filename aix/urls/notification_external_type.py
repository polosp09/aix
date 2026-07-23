from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.NotificationExternalTypeModelListView.as_view(), name='notification-external-type-list'),
    path('<slug:entity_slug>/create/', views.NotificationExternalTypeModelCreateView.as_view(), name='notification-external-type-create'),
    path('<slug:entity_slug>/update/<uuid:notification_external_type_pk>/', views.NotificationExternalTypeModelUpdateView.as_view(), name='notification-external-type-update'),
]
