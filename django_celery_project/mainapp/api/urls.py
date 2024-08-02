from django.urls import path, include
from . import views
urlpatterns = [
    path('products', views.get_products, name='get_products'),
    path('products/<str:product_name>', views.get_product, name ='get_product'),
    path('delete_product/<str:product_name>', views.delete_product, name='delete_product')
]
