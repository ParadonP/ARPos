'''Modules to import'''
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Stock
from .forms import AddInventory

# Create your views here.
def index(request):
    ''' Default View when getting to inventory app'''
    item_list = Stock.objects.order_by('-item')
    context = {'item_list': item_list, }
    return render(request, 'inventory/index.html', context)

def add_inventory_item(request):
    '''View for adding items to the inventory'''
    if request.method == 'POST':
        form = AddInventory(request.POST)
        if form.is_valid():
            # Save post items into local variable
            item = request.POST['item']
            qty = request.POST['qty']
            min_qty = request.POST['min_qty']

            # Commit to Database
            instance = Stock(item=item, qty=qty, qty_min=min_qty)
            instance.save()
            return HttpResponseRedirect('/inventory')
        else:
            form = AddInventory()
    else:
        form = AddInventory()
    return render(request, 'inventory/add_inventory_item.html', {'form': form})
