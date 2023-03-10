from django.contrib.auth.models import User
from django.db import models

from apps.product.models import Product


class Cart(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, null=True, blank=True)

    def __str__(self):
        return f'{self.customer.email}`s cart'


class Order(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, default='order')
    price = models.IntegerField(default=0, null=False, blank=False)
