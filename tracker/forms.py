from tracker.models import Transaction
from django import forms 


class TransactionForm(forms.ModelForm):
    
    class Meta:
        model = Transaction
        exclude = ["user"]  
        widgets = {
            "created":forms.DateTimeInput(
                attrs={"type":"date"},
            )
        }