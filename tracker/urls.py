from django.urls import path
from tracker.views import * 
app_name = "tracker"

urlpatterns = [
    path("",transactions_list, name="transactions-list"),
    path("add/",transaction_add_view, name="transaction-add"),
    path("<pk>/update/",transaction_update_view, name="transaction-update"),
    path("<pk>/delete/",transaction_delete_view, name="transaction-delete"),
    path("export/",export_view, name="export"),
    path("get-transactions/",get_transctions_view, name="get-transactions"),
]
