from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    para_one = models.TextField()
    para_two = models.TextField(null=True)
    para_three = models.TextField(null=True)

class Review(models.Model):
    poster = models.CharField(max_length=20)
    content = models.TextField(max_length=255)
    rating = models.IntegerField()