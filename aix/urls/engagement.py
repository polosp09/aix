from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EngagementModelListView.as_view(), name='engagement-list'),
    path('<slug:entity_slug>/create/', views.EngagementModelCreateView.as_view(), name='engagement-create'),
    path('<slug:entity_slug>/update/<uuid:engagement_pk>/', views.EngagementModelUpdateView.as_view(), name='engagement-update'),
]
