from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.BusinessIndustryModelListView.as_view(), name='business-industry-list'),
    path('<slug:entity_slug>/create/', views.BusinessIndustryModelCreateView.as_view(), name='business-industry-create'),
    path('<slug:entity_slug>/update/<uuid:business_industry_pk>/', views.BusinessIndustryModelUpdateView.as_view(), name='business-industry-update'),
]
