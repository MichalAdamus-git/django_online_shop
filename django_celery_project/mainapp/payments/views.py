from django.shortcuts import render, redirect, HttpResponse
from mainapp.models import Payment
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from payments import get_payment_model, RedirectNeeded
from ipware import get_client_ip
from decimal import Decimal

def success(request):
    pass

def fail(request):
    pass

def payment_details(request, payment_id):
    payment = get_object_or_404(get_payment_model(), id=payment_id)

    try:
        form = payment.get_form(data=request.POST or None)
    except RedirectNeeded as redirect_to:
        return redirect(str(redirect_to))
    context = {'form': form,'payment': payment}
    return render(request, 'payment.html',context)

def create_payment(request):
    total_price = 0
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        items = cart.cartitem_set.all()
        for item in items:
            particular_price = item.product.price * item.quantity
            total_price += particular_price
    else:
        cart = request.session.get('cart')
        if cart != None:
            items = []
            for i in cart:
                identity = cart[i]['product_id']
                db_product = Product.objects.get(pk=identity)
                items.append(db_product)
            for item in items:
                total_price += item.price
        else:
            total_price = 0
# get total price of products in cart. Get cart for logged in from db and for not logged in from session.
    Payment = get_payment_model()
    payment = Payment.objects.create(
        variant='stripe',  # this is the variant from PAYMENT_VARIANTS
        description='Checkout_purchase',
        total=Decimal(total_price),
        tax=Decimal(20),
        currency='USD',
        delivery=Decimal(10),
        billing_first_name='Sherlock',
        billing_last_name='Holmes',
        billing_address_1='221B Baker Street',
        billing_address_2='',
        billing_city='London',
        billing_postcode='NW1 6XE',
        billing_country_code='GB',
        billing_country_area='Greater London',
        customer_ip_address=f'{get_client_ip(request)}',
    )
    return redirect('details', payment_id = payment.id)

def dummy_view(request):
    return render(request, 'dummy.html')