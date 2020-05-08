from django.shortcuts import render
from .models import *
# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'fontend/store.html',context)

def cart(request):
    if request.user.is_authenticated:
        customar = request.user.customar
        order, created = Order.objects.get_or_create(customar=customar)
        item = order.orderitem_set.all()
    else:
        item = []
        order = {'get_card_item' : 0, 'get_cart_total': 0}
    context = {'items':item, 'orders':order }
    return render(request,'fontend/cart.html',context)


def checkout(request):
    if request.user.is_authenticated:
        customar = request.user.customar
        order, created = Order.objects.get_or_create(customar=customar)
        item = order.orderitem_set.all()
    else:
        item = []
        order = {'get_card_item' : 0, 'get_cart_total': 0}
    context = {'items':item, 'orders':order }
    return render(request,'fontend/checkout.html',context)
