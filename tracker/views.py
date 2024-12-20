from django.shortcuts import render
from tracker.models import Transaction, Category
from users.models import User 
from django.contrib.auth.decorators import login_required
from tracker.filters import TransactionFilter



@login_required
def transactions_list(request):
    user = request.user
    filter = TransactionFilter(data = request.GET,queryset=Transaction.objects.filter(user=user).select_related("category"))
    total_expenses = filter.qs.get_total_expenses()
    total_income = filter.qs.get_total_income()
    net_income = total_income - total_expenses
    context = {"filter":filter, "total_expenses":total_expenses, "total_income":total_income, "net_income":net_income}
    if request.htmx:
        return render(request, "partials/transaction-container.html",context)
    return render(request, "tracker/transactions-list.html",context)

