from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.RouteSurveyInfoModelListView.as_view(), name='route-survey-info-list'),
    path('<slug:entity_slug>/list/<uuid:route_survey_pk>/', views.RouteSurveyInfoModelListView.as_view(), name='route-survey-info-list'),
    path('<slug:entity_slug>/create/', views.RouteSurveyInfoModelCreateView.as_view(), name='route-survey-info-create'),
    path('<slug:entity_slug>/update/<uuid:route_survey_info_pk>/', views.RouteSurveyInfoModelUpdateView.as_view(), name='route-survey-info-update'),
    path('<slug:entity_slug>/create/<uuid:route_survey_pk>/', views.RouteSurveyInfoModelAddView.as_view(), name='route-survey-info-create-rs'),
    path('<slug:entity_slug>/update/<uuid:route_survey_pk>/<uuid:route_survey_info_pk>/', views.RouteSurveyInfoModelUpdateView.as_view(), name='route-survey-info-update-rs'),
    path('<slug:entity_slug>/update/<uuid:route_survey_info_pk>/', views.RouteSurveyInfoModelDetailView.as_view(), name='route-survey-info-details'),
]
