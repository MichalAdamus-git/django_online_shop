from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>', views.product, name='product'),
    path('login', views.login_page, name='login_page'),
    path('register', views.register_page, name='register_page'),

]
