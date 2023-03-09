import requests
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=255)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    category = models.ForeignKey('minisite.Category', on_delete=models.CASCADE, related_name='products')

    name = models.CharField(max_length=255)
    price = models.DecimalField(null=True, max_digits=4, decimal_places=2)
    stock = models.IntegerField(null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name