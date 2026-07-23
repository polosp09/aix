from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.AttachedEmailModelListView.as_view(), name='attached-email-list'),
    path('<slug:entity_slug>/create/', views.AttachedEmailModelCreateView.as_view(), name='attached-email-create'),
    path('<slug:entity_slug>/update/<uuid:attached_email_pk>/', views.AttachedEmailModelUpdateView.as_view(), name='attached_email-update'),
]
