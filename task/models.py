from operator import mod
from statistics import mode
from django.db import models

class Advertisement(models.Model):
    name = models.CharField(max_length=200)
    descriptiom = models.TextField(max_length=1000)

class Images(models.Model):
    ad = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    link = models.URLField(max_length=200)
