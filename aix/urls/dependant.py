from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.DependantModelListView.as_view(), name='dependant-list'),
    path('<slug:entity_slug>/create/', views.DependantModelCreateView.as_view(), name='dependant-create'),
    path('<slug:entity_slug>/update/<uuid:dependant_pk>/', views.DependantModelUpdateView.as_view(), name='dependant-update'),
]
