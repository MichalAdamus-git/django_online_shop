from django.shortcuts import render, redirect, HttpResponse
from .tasks import home_converting
from .models import *

# Create your views here.

def home(request):
    return render(request, 'index.html')

def product(request, product_id):
    db_result = Product.objects.get(id=product_id)
    context = {product: db_result}

    ## function to add to cart
    return render(request, 'product.html', context)

def category(request, category_name):
    pass
# show all products in this category.

def login(request):
    pass

def register(request):
    pass

