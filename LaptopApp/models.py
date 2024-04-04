from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)
    class Meta:
        ordering=('name',)
        
        
    def __str__(self):
        return self.name
    def get_url(self):
        return reverse('lap:product_by_category',args=[self.slug])

class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to='product',blank=True)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    stock=models.IntegerField()
    processor=models.TextField(max_length=100)
    os=models.TextField(max_length=100)
    display=models.TextField(max_length=100)
    gc=models.TextField(max_length=100)
    memory=models.TextField(max_length=100)
    storage=models.TextField(max_length=500)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('name',)
        
        
    def __str__(self):
        return self.name
