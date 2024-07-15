from django.db import models


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=20)
class Product(models.Model):
    name = models.CharField(max_length=20, default='Product')
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    image = models.ImageField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


