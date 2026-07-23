from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.QualificationModelListView.as_view(), name='qualification-list'),
    path('<slug:entity_slug>/create/', views.QualificationModelCreateView.as_view(), name='qualification-create'),
    path('<slug:entity_slug>/update/<uuid:qualification_pk>/', views.QualificationModelUpdateView.as_view(), name='qualification-update'),
]
