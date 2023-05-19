from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class childrenproduct(models.Model):
    productID= models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    gender=models.CharField(max_length=100)
    img = models.ImageField(upload_to='Home/images')

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
    user=models.ForeignKey(User,on_delete=models.CASCADE,db_constraint=False)
    product = models.ForeignKey(childrenproduct, on_delete=models.CASCADE)
    product_qty=models.ImageField(null=False,blank=False)
    def __str__(self):
        return self.product.name
    


class babyproduct(models.Model):
    productID= models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    gender=models.CharField(max_length=100)
    img = models.ImageField(upload_to='Home/images')

    def __str__(self)->str:
        return self.name
    

class babyAttribute(models.Model):
    product = models.ForeignKey(babyproduct, on_delete=models.CASCADE,related_name='baby_attributes')
    colors = models.ManyToManyField(Color)
    sizes = models.ManyToManyField(Size)

    def __str__(self):
        return self.product.name
    

class accessoriesproduct(models.Model):
    productID= models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    gender=models.CharField(max_length=100)
    img = models.ImageField(upload_to='Home/images')

    def __str__(self)->str:
        return self.name
    

class accessoriesAttribute(models.Model):
    product = models.ForeignKey(accessoriesproduct, on_delete=models.CASCADE,related_name='accessories_attributes')
    colors = models.ManyToManyField(Color)
    sizes = models.ManyToManyField(Size)

    def __str__(self):
        return self.product.name
    

class toddlerproduct(models.Model):
    productID= models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    gender=models.CharField(max_length=100)
    img = models.ImageField(upload_to='Home/images')

    def __str__(self)->str:
        return self.name
    

class toddlerAttribute(models.Model):
    product = models.ForeignKey(toddlerproduct, on_delete=models.CASCADE,related_name='toddler_attributes')
    colors = models.ManyToManyField(Color)
    sizes = models.ManyToManyField(Size)

    def __str__(self):
        return self.product.name
    
class wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,db_constraint=False) 
    product=models.ForeignKey(childrenproduct,on_delete=models.CASCADE)