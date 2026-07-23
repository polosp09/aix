from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.BenefitCalculationModelListView.as_view(), name='benefit-calculation-list'),
    path('<slug:entity_slug>/create/', views.BenefitCalculationModelCreateView.as_view(), name='benefit-calculation-create'),
    path('<slug:entity_slug>/update/<uuid:benefit_calculation_pk>/', views.BenefitCalculationModelUpdateView.as_view(), name='benefit-calculation-update'),
]
