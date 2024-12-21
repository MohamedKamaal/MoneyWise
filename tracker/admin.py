from django.contrib import admin
from tracker.models import Category, Transaction
from import_export import resources , fields 
from import_export.widgets import ForeignKeyWidget
# Register your models here.

class TransactionResource(resources.ModelResource):
    category = fields.Field(
        column_name="category",
        attribute= "category",
        widget= ForeignKeyWidget(
            Category,"name"
        )
    )
    class Meta:
        model = Transaction
        fields = ["amount","created","type","category"]

admin.site.register(Category)
admin.site.register(Transaction)
