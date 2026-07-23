from django.urls import path

from aix import views

urlpatterns = [
    path('<slug:entity_slug>/latest/',
         views.EquipmentFetModelListView.as_view(),
         name='fet-list'),
    path('<slug:entity_slug>/latest/<uuid:work_order_pk>/',
         views.EquipmentFetModelListView.as_view(),
         name='fet-list'),
    path('<slug:entity_slug>/create/',
         views.EquipmentFetModelCreateView.as_view(),
         name='fet-create'),
    path('<slug:entity_slug>/create/fet/<uuid:work_order_pk>/',
         views.EquipmentFetModelCreateView.as_view(for_work_order=True),
         name='fet-create-work-order'),
    path('<slug:entity_slug>/create/fet/<uuid:work_order_pk>/<uuid:customer_pk>/',
         views.EquipmentFetModelCreateView.as_view(for_work_order=True),
         name='fet-create-work-order-customer'),
    path('<slug:entity_slug>/detail/<uuid:fet_pk>/',
         views.EquipmentFetModelDetailView.as_view(),
         name='fet-detail'),
    path('<slug:entity_slug>/update/<uuid:fet_pk>/',
         views.EquipmentFetModelUpdateView.as_view(),
         name='fet-update'),
    path('<slug:entity_slug>/update/<uuid:fet_pk>/update-items/',
         views.EquipmentFetModelUpdateView.as_view(update_items=True),
         name='fet-update-items'),
    path('<slug:entity_slug>/delete/<uuid:fet_pk>/',
         views.EquipmentFetModelDeleteView.as_view(),
         name='fet-delete'),

    # Actions....
    path('<slug:entity_slug>/action/<uuid:fet_pk>/mark-as-draft/',
         views.EquipmentFetMarkAsDraftView.as_view(),
         name='fet-action-mark-as-draft'),
    path('<slug:entity_slug>/action/<uuid:fet_pk>/mark-as-review/',
         views.EquipmentFetMarkAsReviewView.as_view(),
         name='fet-action-mark-as-review'),
    path('<slug:entity_slug>/action/<uuid:fet_pk>/mark-as-approved/',
         views.EquipmentFetMarkAsApprovedView.as_view(),
         name='fet-action-mark-as-approved'),
    path('<slug:entity_slug>/action/<uuid:fet_pk>/mark-as-fulfilled/',
         views.EquipmentFetMarkAsFulfilledView.as_view(),
         name='fet-action-mark-as-fulfilled'),
    path('<slug:entity_slug>/action/<uuid:fet_pk>/mark-as-canceled/',
         views.EquipmentFetMarkAsCanceledView.as_view(),
         name='fet-action-mark-as-canceled'),
    path('<slug:entity_slug>/action/<uuid:fet_pk>/mark-as-void/',
         views.EquipmentFetMarkAsVoidView.as_view(),
         name='fet-action-mark-as-void'),
     
     # reports
     
    path('<slug:entity_slug>/report/<uuid:fet_pk>/',
         views.EquipmentFetReportView.as_view(dwn_report_file=True),
         name='fet-rpt'),
]
