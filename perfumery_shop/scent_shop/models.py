from django.contrib.auth.models import models
from django.utils import timezone
from django.contrib.auth.models import User


class Pics(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=80)


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)


class Product(models.Model):
    name = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    description = models.TextField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    year = models.CharField(max_length=4)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    email = models.CharField(max_length=100)


class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_total = models.DecimalField(max_digits=9, decimal_places=0)












