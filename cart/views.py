from django.shortcuts import render,redirect
from LaptopApp.models import Product
from.models import Cart,Address
from  django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def addcart(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    print(product)
    try:
        cart=Cart.objects.get(product=product)
        if cart.quantity<cart.product.stock:
            cart.quantity+=1
            cart.save()
            
        
        
    except Cart.DoesNotExist:
        cart=Cart.objects.create(user=user,product=product,quantity=1)
    return redirect('cart:displaycart')


def displaycart(req):
    user=req.session['user']
    cart=Cart.objects.all().filter(user=user)
    total=sum(carts.product.price * carts.quantity for carts in cart) - 1020

    return render(req,'cart.html',{'cart':cart,'total':total})



def cancelcart(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    cart=Cart.objects.get(product=product,user=user)
    if cart.quantity>1:
        cart.quantity-=1
        cart.save()
    return redirect('cart:displaycart')


def fullremove(req,id):
    user=req.session['user']
    product=Product.objects.get(id=id)
    cart=Cart.objects.get(product=product,user=user)
    cart.delete()
    return redirect('cart:displaycart')


def placeorder(req):
    user=req.session['user']
    carts=Cart.objects.filter(user=user)
    for cart in carts:
        prod=Product.objects.get(id=cart.product.id)
        prod.stock-=cart.quantity
        prod.save()
        cart.delete()
      

    return redirect('cart:address')







def address(req):

    cont =Address.objects.all()
    if req.method == "POST":
        name = req.POST.get('name', '')
        email = req.POST.get('email', '')
        number = req.POST.get('number', '')
        address = req.POST.get('address','') 
        pincode = req.POST.get('pincode', '')
        state = req.POST.get('state','')


        enq = Address(name=name, email=email, number=number, address=address, pincode=pincode, state=state)
        enq.save()
   
    return render(req,'address.html',{'cont':cont})
    