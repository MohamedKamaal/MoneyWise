from django.core.management.base import BaseCommand
from tracker.models import Category, Transaction, Type
from django.contrib.auth import get_user_model 
from datetime import datetime
import random


User = get_user_model()

class Command(BaseCommand):

    help  = "generate fake date for tracker app"
    def handle(self,*args,**options):

        # handle users
        user2 = User.objects.create_user(
            username="nada",
            email="nada@outlook.com",
            password="dzbala21"
        )
        users = User.objects.all()
        
        categories = [  "Rent",
                        "Utilities", 
                        "Groceries", 
                        "Transportation", 
                        "Healthcare", 
                        "Insurance", 
                        "Debt Repayment", 
                        "Dining Out", 
                        "Entertainment", 
                        "Clothing", 
                        "Education", 
                        "Childcare", 
                        "Salary", 
                        "Business Income", 
                        "Investments", 
                        "Rental Income", 
                        "Freelance/Side Hustle", 
                        "Dividends", 
                        "Interest Income", 
                        "Capital Gains", 
                        "Pension", 
                        "Social Security", 
                        "Government Benefits", 
                        "Royalties", 
                        "Grants", 
                        "Bonuses", ]

        # register categories 
        for category in categories:
            Category.objects.get_or_create(
                name=category
            )
        
        # get categories 
        categories = Category.objects.all()
        
        # types 
        types = ["expense","income"] 

        # random dates
        random_datetimes = [
                                datetime(2024, 9, 2, 13, 37, 19),
                                datetime(2024, 3, 2, 6, 40, 30),
                                datetime(2024, 6, 29, 23, 50, 6),
                                datetime(2024, 9, 21, 2, 17, 13),
                                datetime(2024, 9, 18, 18, 31, 56),
                                datetime(2024, 12, 9, 15, 11, 57),
                                datetime(2024, 1, 7, 11, 46, 38),
                                datetime(2024, 10, 6, 0, 43, 35),
                                datetime(2024, 4, 5, 15, 38, 9),
                                datetime(2024, 1, 5, 5, 56, 8),
                                datetime(2024, 5, 22, 15, 25, 36),
                                datetime(2024, 4, 26, 3, 46, 17),
                                datetime(2024, 2, 17, 16, 40, 10),
                                datetime(2024, 4, 22, 6, 37, 31),
                                datetime(2024, 1, 25, 5, 59, 39),
                                datetime(2024, 10, 15, 14, 27, 31),
                                datetime(2024, 8, 14, 6, 25, 29),
                                datetime(2024, 4, 15, 18, 0, 20),
                                datetime(2023, 12, 28, 21, 11, 2),
                                datetime(2024,4, 28, 8, 55, 37),
                                datetime(2022, 10, 15, 14, 27, 31),
                                datetime(2021, 8, 14, 6, 25, 29),
                                datetime(2020, 4, 1, 18, 0, 20),
                                datetime(2023, 10, 2, 21, 11, 2),
                                datetime(2024, 8, 28, 8, 55, 37),
                            ]

        # generate fake transactions
        for i in range(50):
            
            Transaction.objects.get_or_create(
                user = random.choice(users),
                type = random.choice(types),
                category = random.choice(categories),
                created = random.choice(random_datetimes),
                amount = random.uniform(1,2500)

            )