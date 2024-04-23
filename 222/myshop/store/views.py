from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def buy_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'store/buy.html', {'product': product})


