from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>', views.product, name='product'),
    path('login_page', views.login_page, name='login_page'),
    path('register_page', views.register_page, name='register_page'),
    path('logout_page', views.logout_page, name='logout_page'),
    path('add_to_my_cart/<int:product_id>', views.cart_addition, name='cart_adding')

]
