from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.WeeklyEmployeeProcessedModelListView.as_view(), name='weekly-employee-processed-list'),
    path('<slug:entity_slug>/create/', views.WeeklyEmployeeProcessedModelCreateView.as_view(), name='weekly-employee-processed-create'),
    path('<slug:entity_slug>/update/<uuid:weekly_employee_processed_pk>/', views.WeeklyEmployeeProcessedModelUpdateView.as_view(), name='weekly-employee-processed-update'),
]
