from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.EducationModelListView.as_view(), name='education-list'),
    path('<slug:entity_slug>/create/', views.EducationModelCreateView.as_view(), name='education-create'),
    path('<slug:entity_slug>/update/<uuid:education_pk>/', views.EducationModelUpdateView.as_view(), name='education-update'),
]
