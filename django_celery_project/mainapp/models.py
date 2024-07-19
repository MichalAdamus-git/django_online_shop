from django.db import models
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=20)
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
        if self.image != NONE:
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
            



