'''Modules to import'''
from django import forms

class AddInventory(forms.Form):
    '''Defines the form for adding inventory Items'''
    item = forms.CharField(label='Item', max_length=30)
    qty = forms.IntegerField(label='Qty')
    min_qty = forms.IntegerField(label='Minimum')
