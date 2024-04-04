from .models import Cart
def cart_items_count(req):

    if req.user.is_authenticated:
        user=req.user
        cart_items_count=Cart.objects.filter(user=user).count()
    else:
        cart_items_count=0
    return{"cart_items_count":cart_items_count}