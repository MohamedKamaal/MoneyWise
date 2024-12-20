import django_filters
from tracker.models import Category, Transaction, Type
from users.models import User
from django import forms 


# filters 
# type filter

class TransactionFilter(django_filters.FilterSet):
    transaction_type = django_filters.ChoiceFilter(
        field_name = "type",
        choices = Type.choices,
        lookup_expr = "iexact",
        empty_label = "Any"
    )
    transaction_date_from = django_filters.DateTimeFilter(
        field_name="created",
        lookup_expr= "gte",
        widget = forms.DateTimeInput(attrs={"type":"date"}),
        label = "from"
    )
    
    transaction_date_to = django_filters.DateTimeFilter(
        field_name="created",
        lookup_expr= "lte",
        widget = forms.DateTimeInput(attrs={"type":"date"}),
        label = "to"
    )
    category = django_filters.ModelMultipleChoiceFilter(
        queryset = Category.objects.all(),
    )
    class Meta:
        model = Transaction
        fields = ["transaction_type","transaction_date_from","transaction_date_to"]
        
        