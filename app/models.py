from django.db import models


class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    para_one = models.TextField()
    para_two = models.TextField(blank=True, default=None)
    para_three = models.TextField(blank=True, default=None)
