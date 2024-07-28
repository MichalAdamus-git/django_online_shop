from django.shortcuts import render, redirect, HttpResponse
from mainapp.models import Payment
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from payments import get_payment_model, RedirectNeeded

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
    return render(request, 'mainapp/payment.html',context)