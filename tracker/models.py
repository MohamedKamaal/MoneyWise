from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Type(models.TextChoices):
    
    EXPENSE = ("expense","Expense")
    INCOME = ("income","Income")
    
class Category(models.Model):
    """ one category for each transaction """
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name_plural = "categories"    
    
    def __str__(self):
        return str(self.name)

class Transaction(models.Model):
    """ transaction can be expense or income , has an amount , related to category, tied to user ,has a date  """
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=Type.choices)
    created = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True , related_name="transactions")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    
    class Meta:
        ordering = ("-created",)
    def __str__(self):
        return f"{self.user} registerd {self.amount} category {self.category} type {self.type} on data {self.created}"