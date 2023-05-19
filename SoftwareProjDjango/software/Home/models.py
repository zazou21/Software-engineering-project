from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class childrenproduct(models.Model):
    productID= models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    gender=models.CharField(max_length=100)
    img = models.ImageField(upload_to='home/images')

    def __str__(self)->str:
        return self.name
    

class Color(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color
    

class Size(models.Model):
    size = models.CharField(max_length=100)
    

    def __str__(self):
        return self.size
    
class productAttribute(models.Model):
    product = models.ForeignKey(childrenproduct, on_delete=models.CASCADE,related_name='product_attributes')
    colors = models.ManyToManyField(Color)
    sizes = models.ManyToManyField(Size)

    def __str__(self):
        return self.product.name
    


class Cart(models.Model):
    product = models.ForeignKey(childrenproduct, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product.name
    