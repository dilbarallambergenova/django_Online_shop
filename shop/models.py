from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    name=models.CharField(max_length=100)
    icon = models.CharField(max_length=5, blank=True,null=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Product(models.Model):
    product_name=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to='product/images')
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,
                               null=True)
    discount_price=models.IntegerField(null=True,blank=True)
    description=models.TextField(blank=True,null=True)
    quantity=models.IntegerField(default=0)
    is_popular=models.BooleanField(default=False)
    
    def is_discounted(self):
        return self.discount_price is not None
    def __str__(self):
        return self.product_name


    





    