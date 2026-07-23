from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.SkillModelListView.as_view(), name='skill-list'),
    path('<slug:entity_slug>/create/', views.SkillModelCreateView.as_view(), name='skill-create'),
    path('<slug:entity_slug>/update/<uuid:skill_pk>/', views.SkillModelUpdateView.as_view(), name='skill-update'),
]
