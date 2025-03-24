from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Brand(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()

class Product(models.Model):
    CHOICES =( 
        ("Trending", "Trending Product"), 
        ("Old", "Old Product"), 
        ("New", "New Product"), 
    ) 
    name = models.CharField(max_length=200)
    description = models.TextField()
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    type = models.CharField(choices=CHOICES, max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.URLField()


