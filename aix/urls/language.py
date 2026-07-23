from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.LanguageModelListView.as_view(), name='language-list'),
    path('<slug:entity_slug>/create/', views.LanguageModelCreateView.as_view(), name='language-create'),
    path('<slug:entity_slug>/update/<uuid:language_pk>/', views.LanguageModelUpdateView.as_view(), name='language-update'),
]
