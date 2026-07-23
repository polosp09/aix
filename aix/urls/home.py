from django.urls import path

from aix import views

urlpatterns = [
    path('aixportal/', views.aixDasboardView.as_view(), name='home'),
    path('staffportal/', views.HRDasboardView.as_view(), name='home-staff'),
    path('dashboard/', views.StaffDasboardView.as_view(), name='dashboard'),
    # path('my-dashboard/', views.DasboardView.as_view(), name='home'),
    # path('dashboard/', views.DasboardView.as_view(), name='dashboard'),
]
