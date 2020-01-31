from django.db import models
from datetime import datetime
# Create your models here.
class Price(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=4)
    objects = objects = models.Manager()