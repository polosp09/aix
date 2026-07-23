from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EngagementDoneByModelListView.as_view(), name='engagement-done-by-list'),
    path('<slug:entity_slug>/create/', views.EngagementDoneByModelCreateView.as_view(), name='engagement-done-by-create'),
    path('<slug:entity_slug>/update/<uuid:engagement_done_by_pk>/', views.EngagementDoneByModelUpdateView.as_view(), name='engagement-done-by-update'),
]
