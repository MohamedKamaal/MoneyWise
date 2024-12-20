from django.urls import path
from tracker.views import * 
app_name = "tracker"

urlpatterns = [
    path("",transactions_list, name="transactions-list")
]
