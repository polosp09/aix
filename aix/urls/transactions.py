from django.urls import path

from aix import views

urlpatterns = [
    path('txs/<slug:entity_slug>/<uuid:ledger_pk>/journal-entry/<uuid:je_pk>/',
         views.TXSJournalEntryView.as_view(),
         name='txs-journal-entry'),
]
