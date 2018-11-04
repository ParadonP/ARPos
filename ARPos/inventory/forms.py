'''Modules to import'''
from django import forms
from .models import Stock

class AddInventoryItem(forms.Form):
    '''Defines the form for adding inventory Items'''
    item = forms.CharField(label='Item', max_length=30)
    item_code = forms.CharField(label='Item Code', max_length=10)
    qty = forms.IntegerField(label='Qty')
    min_qty = forms.IntegerField(label='Minimum')

class UpdateStock(forms.Form):
    ''' Adds stock to an inventory item. '''
    item = forms.ModelChoiceField(queryset=Stock.objects.all())
    qty = forms.IntegerField(label='Qty')

class AddSupplier(forms.Form):
    ''' Defines the form for adding Suppliers '''
    sname = forms.CharField(label='Supplier Name', max_length=30)
