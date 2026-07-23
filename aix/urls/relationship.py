from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.RelationshipModelListView.as_view(), name='relationship-list'),
    path('<slug:entity_slug>/create/', views.RelationshipModelCreateView.as_view(), name='relationship-create'),
    path('<slug:entity_slug>/update/<uuid:relationship_pk>/', views.RelationshipModelUpdateView.as_view(), name='relationship-update'),
]
