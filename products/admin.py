from django.contrib import admin
from .models import Product , Review , Category , Brand , ProductImage

# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
   

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline] 
    

admin.site.register(Product,ProductAdmin)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductImage)