from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.AnnouncementModelListView.as_view(), name='announcement-list'),
    path('<slug:entity_slug>/create/', views.AnnouncementModelCreateView.as_view(), name='announcement-create'),
    path('<slug:entity_slug>/update/<uuid:announcement_pk>/', views.AnnouncementModelUpdateView.as_view(), name='announcement-update'),
]
