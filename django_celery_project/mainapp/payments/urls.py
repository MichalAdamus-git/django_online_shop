from django.urls import path
from . import views

urlpatterns = [
path('payment/success', main_views.success, name='success'),
path('payments/fail', main_views.fail, name='fail')
]