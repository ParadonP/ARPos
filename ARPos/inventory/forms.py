'''Modules to import'''
from django import forms
from .models import Stock

UNIT_TYPES = (
    ('---', '---'),
    ('box', 'Box'),
    ('boltle', 'Bottle'),
    ('bag', 'Bag'),
    ('container', 'Container')
)

class AddInventoryItem(forms.Form):
    '''Defines the form for adding inventory Items'''
    item = forms.CharField(label='Item', max_length=30)
    item_code = forms.CharField(label='Item Code', max_length=10)
    cost = forms.DecimalField(label='Cost')
    qty = forms.IntegerField(label='Qty')
    qty_min = forms.IntegerField(label='Minimum')
    unit = forms.ChoiceField(choices=UNIT_TYPES, required=True)

class EditInventoryItem(forms.Form):
    ''' Defines the form to use when editing an inventory item '''

    item = forms.CharField(label='Item', max_length=30)
    item_code = forms.CharField(label='Item Code', max_length=10)
    cost = forms.DecimalField(label='Cost')
    qty_min = forms.IntegerField(label='Minimum')
    unit = forms.ChoiceField(choices=UNIT_TYPES, required=True)

class UpdateStock(forms.Form):
    ''' Adds stock to an inventory item. '''
    item = forms.ModelChoiceField(queryset=Stock.objects.all())
    qty = forms.IntegerField(label='Qty')

class AddSupplier(forms.Form):
    ''' Defines the form for adding Suppliers '''
    sname = forms.CharField(label='Supplier Name', max_length=30)
    semail = forms.EmailField(label='Email', max_length=254)
    sphone = forms.CharField(label='Phone', max_length=10)
