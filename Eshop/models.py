from dataclasses import dataclass
from django.db import models

# Create your models here.
# creating tables for storing product data

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, default="")
    pub_date = models.DateField()
    image = models.ImageField(upload_to = "Eshop/images", default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=100, default="")
    phone = models.IntegerField(default=0)
    query = models.CharField(max_length=300, default="")
    

    def __str__(self):
        return self.firstname

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    itemJson = models.CharField(max_length=5000, default="")
    firstname = models.CharField(max_length=100, default="")
    lastname = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default=0)
    zip_code = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=1000, default="")