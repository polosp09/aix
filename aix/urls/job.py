from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.JobModelListView.as_view(), name='job-list'),
    path('<slug:entity_slug>/create/', views.JobModelCreateView.as_view(), name='job-create'),
    path('<slug:entity_slug>/update/<uuid:job_pk>/', views.JobModelUpdateView.as_view(), name='job-update'),
]
