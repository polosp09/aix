from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.SettingsListView.as_view(), name='settings-list'),
]
