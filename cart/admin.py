from django.contrib import admin
from .models import Address
# Register your models here.


class AddressAdmin(admin.ModelAdmin):
    list_display=['name','email','number','address','pincode','state']
admin.site.register(Address,AddressAdmin)   
