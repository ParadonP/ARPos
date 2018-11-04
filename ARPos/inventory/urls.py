'''Modules to import'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_inventory', views.add_inventory_item, name='add_inventory')
]
