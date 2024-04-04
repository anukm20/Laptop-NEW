from django.urls import path
from . import views
app_name='cart'
urlpatterns = [
    path('addcart/<int:id>',views.addcart,name='addcart'),
    path('displaycart/',views.displaycart,name='displaycart'),    
    path('cancelcart/<int:id>',views.cancelcart,name='cancelcart'),
    path('fullremove/<int:id>',views.fullremove,name='fullremove'),  
    path('placeorder/',views.placeorder,name='placeorder'),
    path('address/',views.address,name='address'), 
    

]
