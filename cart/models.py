from django.db import models
from LaptopApp.models import Product
# Create your models here.

class Cart(models.Model):
    user=models.CharField(max_length=200)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    
    class Meta:
        db_table='cart'
        
        

    
class Address(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    number=models.CharField(max_length=11)
    address=models.CharField(max_length=200)
    pincode=models.IntegerField()
    state=models.CharField(max_length=15)
    
    def __str__(self):
        return self.name
