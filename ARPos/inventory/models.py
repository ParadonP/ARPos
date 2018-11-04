'''Modules to import'''
from django.db import models

# Create your models here.
class Stock(models.Model):
    '''Defines what the stock table looks like'''
    item = models.CharField(max_length=30)
    qty = models.PositiveSmallIntegerField()
    qty_min = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.item
