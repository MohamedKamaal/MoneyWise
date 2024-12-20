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
    class Meta:
        model = Transaction
        fields = ["transaction_type"]
        
        