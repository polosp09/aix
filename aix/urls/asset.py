from django.urls import path
from aix import views

urlpatterns = [
    path('<slug:entity_slug>/list/', views.AssetModelListView.as_view(), name='asset-list'),
    path('<slug:entity_slug>/create/', views.AssetModelCreateView.as_view(), name='asset-create'),
    path('<slug:entity_slug>/update/<uuid:asset_pk>/', views.AssetModelUpdateView.as_view(), name='asset-update'),
    path('<slug:entity_slug>/assets/', views.PullFleetioAssetsView.as_view(), name='asset-pull'),
    path('<slug:entity_slug>/detail/<uuid:asset_pk>', views.AssetModelDetailView.as_view(), name='asset-details'),
    path('<slug:entity_slug>/report/<uuid:asset_pk>', views.AssetModelDetailView.as_view(dwn_report_file=True), name='asset-rpt'),
]
