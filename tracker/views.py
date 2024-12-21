from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from tracker.admin import TransactionResource
from tracker.filters import TransactionFilter
from tracker.forms import TransactionForm
from tracker.models import Category, Transaction
from users.models import User
from tracker.charting import plot_types_bar_chart

@login_required
def transactions_list(request):
    user = request.user
    filter = TransactionFilter(data = request.GET,queryset=Transaction.objects.filter(user=user).select_related("category"))
    paginator = Paginator(filter.qs,settings.PAGE_SIZE)
    transactions = paginator.get_page(1)
    print(transactions)
  
    total_expenses = filter.qs.get_total_expenses()
    total_income = filter.qs.get_total_income()
    net_income = total_income - total_expenses
    context = {"transactions":transactions,"filter":filter, "total_expenses":total_expenses, "total_income":total_income, "net_income":net_income,"page_index":1}
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


@login_required
def get_transctions_view(request):
    
    page = request.GET.get('page',1)
    filter = TransactionFilter(request.GET,Transaction.objects.filter(user=request.user)
                               .select_related("category"))
    paginator = Paginator(filter.qs, settings.PAGE_SIZE)
    transactions = paginator.get_page(page)
    page_index = (int(page)-1)*10+1
    return render(request, "partials/transaction-container.html#transactions-list" ,{"transactions":transactions,"page_index":page_index})
    

@login_required
def export_view(request):
    if request.htmx:
        return HttpResponse(headers={"HX-Redirect":request.get_full_path()})
    filter = TransactionFilter(request.GET,Transaction.objects.filter(user=request.user).select_related("category"))
    data = TransactionResource().export(filter.qs)
    response = HttpResponse(data.csv)
    response['Content-Disposition'] = 'attachment; filename="transactions.csv"'
    return response 


@login_required
def charts_view(request):
    filter = TransactionFilter(request.GET, Transaction.objects.filter(user=request.user).select_related("category"))
    type_bar = plot_types_bar_chart(filter.qs)
    context = {"filter":filter,"type_bar":type_bar.to_html()}
    if request.htmx:
        
        return render(request,"partials/charts-container.html",context)
    return render(request,"tracker/charts.html",context)