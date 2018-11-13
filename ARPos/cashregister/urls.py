'''Modules to import'''
from django.urls import path
from . import views

urlpatterns = [
    # URL, View, Ref
    path('', views.index, name='index'),
]
