'''Modules to import'''
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    ''' Default View when getting to Cash Register app'''


    context = {}
    return render(request, 'cashregister/index.html', context)
