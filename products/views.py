from itertools import product
from django.shortcuts import render
from django.db.models import Count
from django.views.generic import ListView , DetailView
from .models import Brand, Category, Product, ProductImage, Review
# Create your views here.

class ProductList(ListView):
    model = Product
    paginate_by = 1
    
    
    
class ProductDetail(DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproduct = self.get_object()
        context["images"] = ProductImage.objects.filter(product=myproduct)
        context["Reviews"] = Review.objects.filter(product=myproduct)
        return context
      
    
class CategoryList(ListView):
    model = Category
    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(product_count=Count('products_category')) 
        return context
    
    
    
    
class BrandList(ListView):
    model = Brand    
    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.all().annotate(product_count=Count('products_brand')) 
        return context
    
    
class BrandDetail(DetailView):
    model = Brand 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = self.get_object()
        context["brand_products"] = Product.objects.filter(brand=brand)
        return context
        




