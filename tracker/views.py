from django.shortcuts import render, redirect, get_object_or_404
from tracker.models import Transaction, Category
from users.models import User 
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from tracker.filters import TransactionFilter
from tracker.forms import TransactionForm
from django.contrib import messages



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

@login_required
def transaction_add_view(request):
    user = request.user 
    form = TransactionForm()
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = user 
            transaction.save()
            messages.success(request,"transaction added")

            return render(request, "partials/transaction-success.html")
    context = {"form":form}
    return render(request, "partials/transaction-add.html",context)


@login_required
def transaction_update_view(request,pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    form = TransactionForm(instance = transaction)
    if request.method == "POST":
        form = TransactionForm(instance=transaction, data=request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user 
            transaction.save()
            messages.success(request,"transaction updated")

            return render(request, "partials/transaction-success.html",{"transaction":transaction,"form":form})
    return render(request, "partials/transaction-update.html",{"transaction":transaction,"form":form})


@login_required
@require_http_methods(["DELETE"])
def transaction_delete_view(request,pk):
    transaction = get_object_or_404(Transaction,pk=pk, user = request.user)
    transaction.delete()
    messages.success(request,"transaction deleted")
    return render(request, "partials/transaction-success.html")