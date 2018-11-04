'''Registers modules with the Admin site'''
from django.contrib import admin
from .models import Stock, Suppliers

# Register your models here.
admin.site.register(Stock)
admin.site.register(Suppliers)
