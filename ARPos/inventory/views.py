'''Modules to import'''
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Stock, Suppliers
from .forms import AddInventoryItem, UpdateStock, AddSupplier, EditInventoryItem

# Create your views here.
@login_required
def index(request):
    ''' Default View when getting to inventory app'''
    item_list = Stock.objects.order_by('-item')
    suppliers_list = Suppliers.objects.order_by('-sname')
    context = {'item_list': item_list,
               'suppliers_list': suppliers_list,
              }
    return render(request, 'inventory/index.html', context)

@login_required
def add_inventory_item(request):
    ''' View for adding items to the inventory '''
    header2 = "Add Inventory Item"
    if request.method == 'POST':
        form = AddInventoryItem(request.POST)
        if form.is_valid():
            # Save post items into local variable
            item = request.POST['item']
            item_code = request.POST['item_code']
            qty = request.POST['qty']
            qty_min = request.POST['qty_min']
            unit = request.POST['unit']

            # Commit to Database
            instance = Stock(item=item,
                             item_code=item_code,
                             qty=qty,
                             qty_min=qty_min,
                             unit=unit)
            instance.save()
            return HttpResponseRedirect('/inventory')
        form = AddInventoryItem()
    form = AddInventoryItem()
    return render(request, 'inventory/simple_form.html', {'header2': header2,
                                                          'form': form})
@login_required
def edit_inventory_item(request, item_id):
    ''' View to edit existing Inventory Items '''
    header2 = 'Edit Inventory Item'
    #if request.method == 'GET':

    # Here we need to get the object from the request.
    # obj will be a list of dictionaries.
    obj = Stock.objects.filter(id=item_id).values()

    # Now we need convert it just to a dictionary.
    for key in obj:
        item = key


    # Here we are modifiying the initial value of the form fields.
    form = EditInventoryItem(initial={'item': item['item'],
                                      'item_code': item['item_code'],
                                      'cost': item['cost'],
                                      'qty_min': item['qty_min'],
                                      'unit': item['unit']})
    if request.method == 'POST':
        Stock.objects.filter(id=item_id).update(item=request.POST['item'],
                                                item_code=request.POST['item_code'],
                                                cost=request.POST['cost'],
                                                #qty_min=request.POST['qty_min'],
                                                unit=request.POST['unit'])

    return render(request, 'inventory/simple_form.html', {'header2': header2,
                                                          'form': form})
@login_required
def update_stock_item(request):
    ''' View for adding items to stock. '''
    header2 = "Update Stock"
    if request.method == 'POST':
        Stock.objects.filter(id=request.POST['item']).update(qty=request.POST['qty'])
    form = UpdateStock()
    return render(request, 'inventory/simple_form.html', {'header2': header2,
                                                          'form': form})
@login_required
def add_supplier(request):
    ''' View for adding Supplier '''
    header2 = "Add Supplier"
    if request.method == 'POST':
        form = AddSupplier(request.POST)
        if form.is_valid():
            sname = request.POST['sname']
            semail = request.POST['semail']
            sphone = request.POST['sphone']

            # Commit to Database
            supplier = Suppliers(sname=sname, semail=semail, sphone=sphone)
            supplier.save()
            return HttpResponseRedirect('/inventory')
        form = AddSupplier()
    form = AddSupplier()
    return render(request, 'inventory/simple_form.html', {'header2': header2,
                                                          'form': form})
