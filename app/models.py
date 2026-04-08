from django.db import models

class Menu_Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=4)
    featured = models.BooleanField(default=False)
    image = models.ImageField()

class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    para_one = models.TextField()
    para_two = models.TextField(null=True)
    para_three = models.TextField(null=True)

class Merch_Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=4)
    featured = models.BooleanField(default=False)
    image = models.ImageField()