from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.ImmigrationDetailModelListView.as_view(), name='immigration-detail-list'),
    path('<slug:entity_slug>/create/', views.ImmigrationDetailModelCreateView.as_view(), name='immigration-detail-create'),
    path('<slug:entity_slug>/update/<uuid:immigration_detail_pk>/', views.ImmigrationDetailModelUpdateView.as_view(), name='immigration-detail-update'),
]
