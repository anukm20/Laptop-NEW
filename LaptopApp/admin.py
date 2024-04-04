from django.contrib import admin
from .models import Category,Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug','desc']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','stock','available','created','updated','image']
    prepopulated_fields={'slug':('name',)}
    list_editable=['price','stock','available','image']
    list_per_page=15
    list_filter=['category','available']
admin.site.register(Product,ProductAdmin)