from pydoc import describe
from django.db import models

# Create your models here.

class Items(models.Model):
    itmIMG = models.ImageField(null = True, upload_to = "0_ShopIems/")
    price= models.IntegerField(max_length=50,null=True)
    describe=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.describe


class Subscribe(models.Model):
    people = models.EmailField(max_length=250,null=True)
    def __str__(self):
        return self.people

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message  = models.CharField(max_length=500)
    phone=models.CharField(max_length=100)
    subject=models.CharField(max_length=30)

    def __str__(self):
        return self.name