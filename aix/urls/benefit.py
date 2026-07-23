from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.BenefitModelListView.as_view(), name='benefit-list'),
    path('<slug:entity_slug>/create/', views.BenefitModelCreateView.as_view(), name='benefit-create'),
    path('<slug:entity_slug>/update/<uuid:benefit_pk>/', views.BenefitModelUpdateView.as_view(), name='benefit-update'),
]
