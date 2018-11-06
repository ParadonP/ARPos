'''Modules to import'''
from django.db import models

# Create your models here.
class Stock(models.Model):
    '''Defines what the stock table looks like'''
    item_code = models.CharField(max_length=10, default='', unique=True)
    item = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    qty = models.PositiveSmallIntegerField()
    qty_min = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.item

class Suppliers(models.Model):
    ''' Defines the available Suppliers'''
    sname = models.CharField(max_length=30)
    semail = models.EmailField(max_length=254, default='undef')
    sphone = models.CharField(max_length=10, default='0')

    def __str__(self):
        return self.sname
