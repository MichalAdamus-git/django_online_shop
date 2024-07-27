from django.db import models
from PIL import Image
from django.contrib.auth.models import User
#from payments import PurchasedItem
#from payments.models import BasePayment

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=20)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    completed = models.BooleanField(default=False)


class Product(models.Model):
    name = models.CharField(max_length=20, default='Product')
    description = models.TextField(null=True)
    height = models.PositiveIntegerField(null=True)
    width = models.PositiveIntegerField(null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    image = models.ImageField(height_field='height', width_field='width')
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def save(self):
        max_height = 500
        max_width = 600
        if self.image != None:
            super().save()
            if self.height > max_height:
                image_to_process = PIL.Image.open(self.image)
                coeff = max_height/self.image.height
                target_width = self.image.width * coeff
                image_to_process.resize(int(target_width), int(tmax_height), PIL.Image.ANTIALIAS) 
                image_to_process.save(self.image.path, quelity = 100)
                img.close()
                self.image.close()
            elif self.width > max_width:
                image_to_process = PIL.Image.open(self.image)
                coeff = max_width/self.image.width
                target_height = self.image.height * coeff
                image_to_process.resize(int(max_width), int(target_height), PIL.Image.ANTIALIAS) 
                image_to_process.save(self.image.path, quelity = 100)
                img.close()
                self.image.close()
            else:
                super().save()
        else:
            super().save()

    def __str__(self):
        return self.id
class Cartitem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
'''
class Payment(BasePayment):

    def get_failure_url(self) -> str:
        # Return a URL where users are redirected after
        # they fail to complete a payment:
        return f"http://example.com/payments/{self.pk}/failure"

    def get_success_url(self) -> str:
        # Return a URL where users are redirected after
        # they successfully complete a payment:
        return f"http://example.com/payments/{self.pk}/success"

    def get_purchased_items(self) -> Iterable[PurchasedItem]:
        # Return items that will be included in this payment.
        yield PurchasedItem(
            name='The Hound of the Baskervilles',
            sku='BSKV',
            quantity=9,
            price=Decimal(10),
            currency='USD',
        )
'''
            



