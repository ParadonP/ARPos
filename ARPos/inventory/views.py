'''Modules to import'''
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Stock
from .forms import AddInventoryItem, UpdateStock

# Create your views here.
def index(request):
    ''' Default View when getting to inventory app'''
    item_list = Stock.objects.order_by('-item')
    context = {'item_list': item_list, }
    return render(request, 'inventory/index.html', context)

def add_inventory_item(request):
    '''View for adding items to the inventory'''
    header2 = "Add Inventory Item"
    if request.method == 'POST':
        form = AddInventoryItem(request.POST)
        if form.is_valid():
            # Save post items into local variable
            item = request.POST['item']
            item_code = request.POST['item_code']
            qty = request.POST['qty']
            min_qty = request.POST['min_qty']

            # Commit to Database
            instance = Stock(item=item, item_code=item_code, qty=qty, qty_min=min_qty)
            instance.save()
            return HttpResponseRedirect('/inventory')
        form = AddInventoryItem()
    form = AddInventoryItem()
    return render(request, 'inventory/simple_form.html', {'header2': header2,
                                                          'form': form})

def update_stock_item(request):
    ''' View for adding items to stock. '''
    header2 = "Update Stock"
    if request.method == 'POST':
        Stock.objects.filter(id=request.POST['item']).update(qty=request.POST['qty'])
    form = UpdateStock()
    return render(request, 'inventory/simple_form.html', {'header2': header2,
                                                          'form': form})
