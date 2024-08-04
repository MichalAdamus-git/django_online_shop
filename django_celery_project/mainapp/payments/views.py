from django.shortcuts import render, redirect, HttpResponse
from mainapp.models import Cart
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.conf import settings
from ipware import get_client_ip
from decimal import Decimal
import stripe
from django.conf import settings

def success(request):
    pass

def fail(request):
    pass



def create_payment(request):
    total_price = 0
    product_list = []
    line_items = []
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        items = cart.cartitem_set.all()
        for item in items:
            particular_price = item.product.price * item.quantity
            total_price += particular_price
            product_list.append(item)
    else:
        cart = request.session.get('cart')
        if cart != None:
            items = []
            for i in cart:
                identity = cart[i]['product_id']
                db_product = Product.objects.get(pk=identity)
                items.append(db_product)
                product_list.append(db_product)
            for item in items:
                total_price += item.price
        else:
            total_price = 0

    if request.method == 'POST':
        for product in product_list:
            element = {'price_data':{
                'currency': 'usd',
                'product_data' : {
                    'name': f'{product.product.name}',
                },
                'unit_amount_decimal' : f'{product.product.price}',
            },
            'quantity':1
            }
            line_items.append(element)
        stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
        if len(line_items)>0:
            payment_process = stripe.checkout.Session.create(
                success_url='http://127.0.0.1:8000/payments/success',
                line_items=line_items,
                mode = 'payment',
                cancel_url = 'http://127.0.0.1:8000/payments/fail'
            )
            return redirect(payment_process.url, code='303')
        else:
            return render(request,'dummy.html')
    return render(request, 'payment.html')
def dummy_view(request):
    return render(request, 'dummy.html')