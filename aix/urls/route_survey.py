
from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.RouteSurveyModelListView.as_view(), name='route-survey-list'),
    path('<slug:entity_slug>/create/', views.RouteSurveyModelCreateView.as_view(), name='route-survey-create'),
    path('<slug:entity_slug>/update/<uuid:route_survey_pk>/', views.RouteSurveyModelUpdateView.as_view(), name='route-survey-update'),    
    path('<slug:entity_slug>/detail/<uuid:route_survey_pk>/', views.RouteSurveyModelDetailView.as_view(), name='route-survey-details'),
    # Actions...
#     path('<slug:entity_slug>/actions/<uuid:route_survey_pk>/mark-as-approved-by-hr/',
#          views.RouteSurveyModelActionApprovedByHRView.as_view(),
#          name='route-survey-action-mark-as-approved-by-hr'),
#     path('<slug:entity_slug>/actions/<uuid:route_survey_pk>/mark-as-approved-by-ict/',
#          views.RouteSurveyModelActionApprovedByICTView.as_view(),
#          name='route-survey-action-mark-as-approved-by-ict'),
    
    # reports
    path('<slug:entity_slug>/report/<uuid:route_survey_pk>/',
         views.RouteSurveyReportView.as_view(dwn_report_file=True),
         name='route-survey-rpt'),
]
