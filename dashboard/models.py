from operator import mod
from re import T
from statistics import mode
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY = (
    ('stationary', 'stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
    ('Snacks', 'Snacks'),
    )

class Product(models.Model):
    name=models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity=models.PositiveIntegerField(null=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return f'{self.name} - {self.quantity}'

class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    staff=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity=models.PositiveBigIntegerField(null=True)
    dateOrdered = models.DateField(auto_now_add=True)

    class Meta:
        db_table='orders'

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'
