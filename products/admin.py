from django.contrib import admin
from .models import Product , Review , Category , Brand , ProductImage
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
   

class ProductAdmin(SummernoteModelAdmin):
    inlines = [ProductImageInline] 
    summernote_fields = '__all__'
    

admin.site.register(Product,ProductAdmin)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductImage)