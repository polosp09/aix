from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.AbsenceTypeModelListView.as_view(), name='absence-type-list'),
    path('<slug:entity_slug>/create/', views.AbsenceTypeModelCreateView.as_view(), name='absence-type-create'),
    path('<slug:entity_slug>/update/<uuid:absence_type_pk>/', views.AbsenceTypeModelUpdateView.as_view(), name='absence-type-update'),
]
