'''Modules to import'''
from django.urls import path

from . import views

urlpatterns = [
    # URL, View, Ref
    path('', views.index, name='index'),
    path('add_inventory', views.add_inventory_item, name='add_inventory'),
    path('edit_inventory_item/<int:item_id>', views.edit_inventory_item, name='edit_inventory'),
    path('update_stock', views.update_stock_item, name='update_stock'),
    path('add_supplier', views.add_supplier, name='add_supplier')
]
