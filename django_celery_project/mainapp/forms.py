from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Product

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'image', 'price']



