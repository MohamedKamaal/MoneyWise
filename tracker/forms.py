from django import forms

from tracker.models import Transaction


class TransactionForm(forms.ModelForm):
    
    def clean_amount(self):
        amount =self.cleaned_data.get("amount")
        if amount <=0:
            raise forms.ValidationError("Amount can't be negative or zero")
        return amount
    
    class Meta:
        model = Transaction
        exclude = ["user"]  
        widgets = {
            "created":forms.DateTimeInput(
                attrs={"type":"date"},
            )
        }