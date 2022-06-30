from django.db import models

# Create your models here.

class Manufacture(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacture,on_delete=models.CASCADE,related_name='products')
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    photo = models.ImageField(blank=True,null=True)
    price = models.FloatField()
    shipping_cost = models.FloatField()
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name