from celery import shared_task
from .models import Product

@shared_task(bind=True)
def home_converting(self):
    pass

@shared_task(bind=True)
def async_product_saving(id):
    product = Product.objects.get(pk = id)
    product.save()