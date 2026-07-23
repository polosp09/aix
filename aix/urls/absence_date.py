from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.AbsenceDateModelListView.as_view(), name='absence-date-list'),
    path('<slug:entity_slug>/create/', views.AbsenceDateModelCreateView.as_view(), name='absence-date-create'),
    path('<slug:entity_slug>/update/<uuid:absence_date_pk>/', views.AbsenceDateModelUpdateView.as_view(), name='absence-date-update'),
]
