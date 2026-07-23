from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.HolidayModelListView.as_view(), name='holiday-list'),
    path('<slug:entity_slug>/create/', views.HolidayModelCreateView.as_view(), name='holiday-create'),
    path('<slug:entity_slug>/update/<uuid:holiday_pk>/', views.HolidayModelUpdateView.as_view(), name='holiday-update'),
]
