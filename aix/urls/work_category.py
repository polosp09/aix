
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WorkCategoryModelListView.as_view(), name='work-category-list'),
    path('<slug:entity_slug>/create/', views.WorkCategoryModelCreateView.as_view(), name='work-category-create'),
    path('<slug:entity_slug>/update/<uuid:work_category_pk>/', views.WorkCategoryModelUpdateView.as_view(), name='work-category-update'),
]
