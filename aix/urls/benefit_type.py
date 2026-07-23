from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.BenefitTypeModelListView.as_view(), name='benefit-type-list'),
    path('<slug:entity_slug>/create/', views.BenefitTypeModelCreateView.as_view(), name='benefit-type-create'),
    path('<slug:entity_slug>/update/<uuid:benefit_type_pk>/', views.BenefitTypeModelUpdateView.as_view(), name='benefit-type-update'),
]
