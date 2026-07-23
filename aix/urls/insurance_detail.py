from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.InsuranceDetailModelListView.as_view(), name='insurance-detail-list'),
    path('<slug:entity_slug>/create/', views.InsuranceDetailModelCreateView.as_view(), name='insurance-detail-create'),
    path('<slug:entity_slug>/update/<uuid:insurance_detail_pk>/', views.InsuranceDetailModelUpdateView.as_view(), name='insurance-detail-update'),
]
