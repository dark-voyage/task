from operator import mod
from statistics import mode
from django.db import models

class Advertisement(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    main_image = models.URLField(max_length=200)

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class Images(models.Model):
    ad = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    link = models.URLField(max_length=200)
