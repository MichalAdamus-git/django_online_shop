from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .tasks import async_product_saving
from .models import *
from .forms import *

# Create your views here.

def home(request):
    db_result =Product.objects.all()
    context = {'products_all': db_result}
    return render(request, 'index.html', context)


def product(request, product_id):
    db_result = Product.objects.get(pk=product_id)
    context = {'product': db_result}

    ## function to add to cart
    return render(request, 'product.html', context)

def category(request, category_name):
    pass
# show all products in this category.

def login_page(request):
    form = UserForm()
    context = {'form': form}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)
        if user != NONE:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'There is no such user')
    return render(request, 'login.html', context)

def register_page(request):
    form = UserForm
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'register.html', context)
