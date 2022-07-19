from itertools import product
from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , ProductImage, Review
# Create your views here.

class ProductList(ListView):
    model = Product
    paginate_by = 1
    
    
    
class ProductDetail(DetailView):
    model = Product
    
    
    def get_context_data(self, **kwargs):
        myproduct = self.get_object()
        context = super().get_context_data(**kwargs)
        context["images"] =ProductImage.objects.filter(product=myproduct) 
        context["Reviews"] =Review.objects.filter(product=myproduct)
        return context
      
    






