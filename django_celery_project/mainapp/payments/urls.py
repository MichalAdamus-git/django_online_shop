from django.urls import path
from . import views

urlpatterns = [
path('success',views.success, name='success'),
path('fail', views.fail, name='fail'),
path('details/<int:payment_id>', views.payment_details, name='details'),
path('create', views.create_payment, name='create_payment'),
path('dummy', views.dummy_view, name='dummy')
]