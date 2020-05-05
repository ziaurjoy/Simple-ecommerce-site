from django.shortcuts import render
from .models import Product
# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'fontend/store.html',context)

def cart(request):
    context = {}
    return render(request,'fontend/cart.html',context)


def checkout(request):
    context = {}
    return render(request,'fontend/checkout.html',context)
