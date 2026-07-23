from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.MaritalStatusModelListView.as_view(), name='marital-status-list'),
    path('<slug:entity_slug>/create/', views.MaritalStatusModelCreateView.as_view(), name='marital-status-create'),
    path('<slug:entity_slug>/update/<uuid:marital_status_pk>/', views.MaritalStatusModelUpdateView.as_view(), name='marital-status-update'),
]
