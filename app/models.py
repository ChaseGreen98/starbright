from django.db import models


class Newsletter(models.Model):
    title = models.CharField(max_length=255)
    para_one = models.TextField()
    para_two = models.TextField(null=True)
    para_three = models.TextField(null=True)
