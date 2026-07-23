from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.VisaModelListView.as_view(), name='visa-list'),
    path('<slug:entity_slug>/create/', views.VisaModelCreateView.as_view(), name='visa-create'),
    path('<slug:entity_slug>/update/<uuid:visa_pk>/', views.VisaModelUpdateView.as_view(), name='visa-update'),
]
