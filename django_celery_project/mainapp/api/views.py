from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from mainapp.models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAdminUser

@api_view(['GET'])
def get_products(request):
    db_result = Product.objects.all()
    context = ProductSerializer(db_result, many = True)
    return Response(context.data)

@api_view(['GET'])
def get_product(request, product_name):
    db_result = Product.objects.get(name = product_name)
    context = ProductSerializer(db_result, many = False)
    return Response(context.data)
#restrict acces
@api_view(['GET', 'DELETE'])
@permission_classes([IsAdminUser])
def delete_product(request, product_name):
    db_result = Preoduct.objects.get(name=product_name)
    db_result.delete()
    return Response({})

@api_view(['GET'])
def categories(request):
    db_result = Category.objects.all()
    context = CategorySerializer(db_result, many = True)
    return Response(context.data)

@api_view(['GET'])
def get_category(request, category_name):
    db_result = Category.objects.get(name = category_name)
    context = CategorySerializer(db_result, many = False)
    return Response(context.data)

@api_view(['GET', 'DELETE'])
@permission_classes([IsAdminUser])
def delete_category(request, category_name):
    db_result = Category.objects.get(name=category_name)
    db_result.delete()
    return Response({})
