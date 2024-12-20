from django.shortcuts import render
from tracker.models import Transaction, Category
from users.models import User 
from django.contrib.auth.decorators import login_required
from tracker.filters import TransactionFilter



@login_required
def transactions_list(request):
    user = request.user
    filter = TransactionFilter(data = request.GET,queryset=Transaction.objects.filter(user=user).select_related("category"))
    context = {"filter":filter}
    if request.htmx:
        return render(request, "partials/transaction-container.html",context)
    return render(request, "tracker/transactions-list.html",context)

