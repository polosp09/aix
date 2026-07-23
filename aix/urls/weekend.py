from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WeekendModelListView.as_view(), name='weekend-list'),
    path('<slug:entity_slug>/create/', views.WeekendModelCreateView.as_view(), name='weekend-create'),
    path('<slug:entity_slug>/update/<uuid:weekend_pk>/', views.WeekendModelUpdateView.as_view(), name='weekend-update'),
]
