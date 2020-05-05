from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Customar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    email = models.EmailField(max_length=100, null=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    customar = models.ForeignKey(Customar, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complited = models.BooleanField(default=False, blank=True, null=True)
    transaction_id = models.CharField(max_length=200, null=True)
    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product

class ShippingAddress(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zip_code = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address