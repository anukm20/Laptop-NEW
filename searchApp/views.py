from django.shortcuts import render
from LaptopApp.models import Product
from django.db.models import Q

# Create your views here.
def Search(req):
    products=None
    query=None
    if 'q' in req.GET:
        query=req.GET.get('q')
        print(req.GET.get('q'))
        products=Product.objects.all().filter(Q(name__contains=query))
    return render(req,'searchproduct.html',{'query':query,'products':products})
        