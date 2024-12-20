from django.urls import path
from tracker.views import * 
app_name = "tracker"

urlpatterns = [
    path("",transactions_list, name="transactions-list"),
    path("add/",transaction_add_view, name="transaction-add"),
]
