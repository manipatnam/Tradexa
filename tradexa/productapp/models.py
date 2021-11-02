from django.db import models


# Create your models here.
class Product(models.Model):
    user = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

