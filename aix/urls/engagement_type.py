from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EngagementTypeModelListView.as_view(), name='engagement-type-list'),
    path('<slug:entity_slug>/create/', views.EngagementTypeModelCreateView.as_view(), name='engagement-type-create'),
    path('<slug:entity_slug>/update/<uuid:engagement_type_pk>/', views.EngagementTypeModelUpdateView.as_view(), name='engagement-type-update'),
]
