from django.urls import path

from aix import views

urlpatterns = [
    path('<slug:entity_slug>/latest/',
         views.EmployeeFawModelListView.as_view(),
         name='faw-list'),
    path('<slug:entity_slug>/latest/<uuid:work_order_pk>/',
         views.EmployeeFawModelListView.as_view(),
         name='faw-list'),
    path('<slug:entity_slug>/create/',
         views.EmployeeFawModelCreateView.as_view(),
         name='faw-create'),
    path('<slug:entity_slug>/create/faw/<uuid:work_order_pk>/',
         views.EmployeeFawModelCreateView.as_view(for_work_order=True),
         name='faw-create-work-order'),
    path('<slug:entity_slug>/create/faw/<uuid:work_order_pk>/<uuid:customer_pk>/',
         views.EmployeeFawModelCreateView.as_view(for_work_order=True),
         name='faw-create-work-order-customer'),
    path('<slug:entity_slug>/detail/<uuid:faw_pk>/',
         views.EmployeeFawModelDetailView.as_view(),
         name='faw-detail'),
    path('<slug:entity_slug>/update/<uuid:faw_pk>/',
         views.EmployeeFawModelUpdateView.as_view(),
         name='faw-update'),
    path('<slug:entity_slug>/update/<uuid:faw_pk>/update-items/',
         views.EmployeeFawModelUpdateView.as_view(update_items=True),
         name='faw-update-items'),
    path('<slug:entity_slug>/delete/<uuid:faw_pk>/',
         views.EmployeeFawModelDeleteView.as_view(),
         name='faw-delete'),

    # Actions....
    path('<slug:entity_slug>/action/<uuid:faw_pk>/mark-as-draft/',
         views.EmployeeFawMarkAsDraftView.as_view(),
         name='faw-action-mark-as-draft'),
    path('<slug:entity_slug>/action/<uuid:faw_pk>/mark-as-review/',
         views.EmployeeFawMarkAsReviewView.as_view(),
         name='faw-action-mark-as-review'),
    path('<slug:entity_slug>/action/<uuid:faw_pk>/mark-as-approved/',
         views.EmployeeFawMarkAsApprovedView.as_view(),
         name='faw-action-mark-as-approved'),
    path('<slug:entity_slug>/action/<uuid:faw_pk>/mark-as-fulfilled/',
         views.EmployeeFawMarkAsFulfilledView.as_view(),
         name='faw-action-mark-as-fulfilled'),
    path('<slug:entity_slug>/action/<uuid:faw_pk>/mark-as-canceled/',
         views.EmployeeFawMarkAsCanceledView.as_view(),
         name='faw-action-mark-as-canceled'),
    path('<slug:entity_slug>/action/<uuid:faw_pk>/mark-as-void/',
         views.EmployeeFawMarkAsVoidView.as_view(),
         name='faw-action-mark-as-void'),
     
     # reports
     
    path('<slug:entity_slug>/report/<uuid:faw_pk>/',
         views.EmployeeFawReportView.as_view(dwn_report_file=True),
         name='faw-rpt'),
]
