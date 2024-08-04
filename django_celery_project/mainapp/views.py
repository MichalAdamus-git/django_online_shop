from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.template.response import TemplateResponse
from django.core import serializers

# Create your views here.

def home(request):
    db_result = Product.objects.all()
    context = {'products_all': db_result}
    return render(request, 'index.html', context)


def product(request, product_id):
    db_result = Product.objects.get(pk=product_id)
    context = {'product': db_result}

    ## function to add to cart
    return render(request, 'product.html', context)

def show_category(request, category_name):
    category = Category.objects.get(category_name=category_name)
    db_result = Product.objects.filter(category = category.id)
    products = db_result.all()
    context = {'products_all': products}
    return render(request,'index.html',context)

# show all products in this category.

def login_page(request):
    form = UserForm()
    context = {'form': form}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password = password)
        if user != None:
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

def logout_page(request):
    logout(request)
    return redirect('home')

def cart_addition(request, product_id):
    product = Product.objects.get(pk=product_id)
    product_data = product.__dict__
    if request.user.is_authenticated:
        user = request.user
        current_cart, completed = Cart.objects.get_or_create(user=user)
        add_to_cart(product, current_cart)
    else:
        cart = request.session.get('cart')
        if cart != None:
           pass
        else:
            request.session['cart'] = {}
        product_ident = str(product_id)
        prod_price = str(product.price)
        request.session['cart'][product_ident] = {'product_id': product_ident, 'price': prod_price}
        request.session.modified = True
        print(request.session['cart'])
    return redirect('home')

def add_to_cart(product: Product, cart: Cart):
    items = cart.cartitem_set.all()
    name = product.name
    quantity_updated = False
    for item in items:
        if item.product.name == name:
            item.quantity += 1
            quantity_updated = True
            item.save()
        else:
            pass
    if quantity_updated:
        pass
    else:
        Cartitem.objects.create(product = product, cart = cart, quantity =1)


@login_required(login_url='login_page')
def add_product(request):
    product_form = ProductForm()
    context = {'form': product_form}
    if request.method == 'POST':
        if product_form.is_valid():
            product_form.save()
    return render(request, 'add_product.html', context)

def cart_view(request):
    items_list = []
    total_price = 0
    logged_in = False
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        items = cart.cartitem_set.all()
        for item in items:
            items_list.append(item)
            particular_price = item.product.price * item.quantity
            total_price += particular_price
        logged_in = True
    else:
        cart = request.session.get('cart')
        if cart != None:
            items = []
            for i in cart:
                identity = cart[i]['product_id']
                db_product = Product.objects.get(pk = identity)
                items.append(db_product)
            for item in items:
                items_list.append(item)
                total_price += item.price
        else:
            request.session['cart'] = {}
            cart = request.session.get('cart')
            items = []
            total_price = 0
    context = {'items': items_list, 'total_price': total_price, 'not_guest_user' : logged_in}
    return render(request, 'cart.html', context)

'''
def payment_details(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)

    try:
        form = payment.get_form(data=request.POST or None)
    except RedirectNeeded as redirect_to:
        return redirect(str(redirect_to))

    return TemplateResponse(
        request,
        'payment.html',
        {'form': form, 'payment': payment}
    )
'''