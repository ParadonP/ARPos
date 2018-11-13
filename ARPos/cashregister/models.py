from django.db import models

# Create your models here.
class Cart(models.Model):
    ''' Class for defining the Shopping Cart '''
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class CartItems(models.Model):
    ''' Class for defining all the products added to the shopping cart '''
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
