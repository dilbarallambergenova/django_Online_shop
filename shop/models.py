from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)
    icon = models.CharField(max_length=5, blank=True,null=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Smartfon(models.Model):
    product_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='shop')
    price=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,
                               null=True)
    
    def __str__(self):
        return self.product_name


    
class Popular_product(models.Model):
    product_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='shop')
    price=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,
                               null=True)
    
    def __str__(self):
        return self.product_name
    
    
class Discounted_product(models.Model):
    product_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='discounted_product')
    price=models.CharField(max_length=100)
    old_price=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,
                               null=True)
    def __str__(self):
        return self.product_name
    
