from django.contrib import admin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from tracker.models import Category, Transaction

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
