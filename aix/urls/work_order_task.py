from django.urls import path

from aix import views

urlpatterns = [
    path('<slug:entity_slug>/latest/',
         views.WorkOrderTaskModelListView.as_view(),
         name='work-order-task-list'),
    path('<slug:entity_slug>/latest/<uuid:work_order_pk>/',
         views.WorkOrderTaskModelListView.as_view(),
         name='work-order-task-list'),
    path('<slug:entity_slug>/create/',
         views.WorkOrderTaskModelCreateView.as_view(),
         name='work-order-task-create'),
    path('<slug:entity_slug>/create/wo/<uuid:work_order_pk>/',
         views.WorkOrderTaskModelAddView.as_view(),
         name='work-order-task-create-wo'),
    path('<slug:entity_slug>/create/wo/<uuid:work_order_pk>/<uuid:customer_pk>/',
         views.WorkOrderTaskModelCreateView.as_view(),
         name='work-order-task-create-customer'),
    path('<slug:entity_slug>/detail/<uuid:work_order_task_pk>/',
         views.WorkOrderTaskModelDetailView.as_view(),
         name='work-order-task-details'),
    path('<slug:entity_slug>/update/<uuid:work_order_task_pk>/',
         views.WorkOrderTaskModelUpdateView.as_view(),
         name='work-order-task-update'),
    path('<slug:entity_slug>/update/<uuid:work_order_pk>/<uuid:work_order_task_pk>/',
         views.WorkOrderTaskModelUpdateView.as_view(),
         name='work-order-task-update-wo'),
     path('<slug:entity_slug>/report/<uuid:work_order_task_pk>', 
          views.WorkOrderTaskModelDetailView.as_view(dwn_report_file=True), name='task-rpt'),

#     # Actions....
#     path('<slug:entity_slug>/action/<uuid:task_pk>/mark-as-draft/',
#          views.WorkOrderTaskMarkAsDraftView.as_view(),
#          name='task-action-mark-as-draft'),
#     path('<slug:entity_slug>/action/<uuid:task_pk>/mark-as-review/',
#          views.WorkOrderTaskMarkAsReviewView.as_view(),
#          name='task-action-mark-as-review'),
#     path('<slug:entity_slug>/action/<uuid:task_pk>/mark-as-approved/',
#          views.WorkOrderTaskMarkAsApprovedView.as_view(),
#          name='task-action-mark-as-approved'),
#     path('<slug:entity_slug>/action/<uuid:task_pk>/mark-as-fulfilled/',
#          views.WorkOrderTaskMarkAsFulfilledView.as_view(),
#          name='task-action-mark-as-fulfilled'),
#     path('<slug:entity_slug>/action/<uuid:task_pk>/mark-as-canceled/',
#          views.WorkOrderTaskMarkAsCanceledView.as_view(),
#          name='task-action-mark-as-canceled'),
#     path('<slug:entity_slug>/action/<uuid:task_pk>/mark-as-void/',
#          views.WorkOrderTaskMarkAsVoidView.as_view(),
#          name='task-action-mark-as-void'),
     
     # reports
     
#     path('<slug:entity_slug>/report/<uuid:task_pk>/',
#          views.WorkOrderTaskReportView.as_view(dwn_report_file=True),
#          name='task-rpt'),
]
