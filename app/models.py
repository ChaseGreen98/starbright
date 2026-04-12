from django.db import models


class Menu_Item(models.Model):
    class Category(models.TextChoices):
        COFFEE = 'COF', 'Coffee'
        FRAPPE = 'FRA', 'Frappe'
        KIDS = 'KID', 'Starbright Kids'
        FOOD = 'FOO', 'Food'
        SPECIALTY = 'SPE', 'Starbright Specialty Drinks'
        LOTUS = 'LOT', 'Lotus plant Power'
        OTHER = 'OTH', 'Other'

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=3, choices=Category.choices, default=Category.COFFEE)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    is_featured = models.BooleanField(default=False)
    image = models.ImageField()

class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    para_one = models.TextField()
    para_two = models.TextField(null=True)
    para_three = models.TextField(null=True)

class Merch_Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    is_featured = models.BooleanField(default=False)
    image = models.ImageField()