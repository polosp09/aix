from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.NationModelListView.as_view(), name='nation-list'),
    path('<slug:entity_slug>/create/', views.NationModelCreateView.as_view(), name='nation-create'),
    path('<slug:entity_slug>/update/<uuid:nation_pk>/', views.NationModelUpdateView.as_view(), name='nation-update'),
]
