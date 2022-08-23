from itertools import product
from django.shortcuts import render
from django.db.models import Count
from django.views.generic import ListView , DetailView
from .models import Brand, Category, Product, ProductImage, Review
from django.db.models import Q , F , Func , Value
from django.db.models.aggregates import Count, Max, Min, Sum, Avg
from django.db.models.functions import Concat
from django.db.models import CharField

# Create your views here.


def product_list(request):
    
    #  queryset = Product.objects.filter(
    #                                    Q(name__endswith='martin') |   # or
    #                                    Q(price__gt=99)
    #                                   )  
    # queryset = Product.objects.filter(
    #                                     Q(name__endswith='martin') &   # telda should be with (AND) or (OR)
    #                                     ~Q(price__gt=99)  
    #                                   )
    # queryset = Product.objects.filter(
    #                                     Q(name__endswith='martin') &   # AND
    #                                     Q(price__gt=99)
    #                                   )
    
    
    # queryset = Product.objects.filter(id=F('category__id'))   # if category = id
    # queryset = Product.objects.filter(id=F('category__id')).order_by('name')  #can apply two object in same time
    
    # queryset = Product.objects.order_by('name')   # order by what you need
    # queryset = Product.objects.order_by('-name')  # order by reverse
    # queryset = Product.objects.order_by('name', 'price')  #order by two field  
    # queryset = Product.objects.order_by('name','-price')   
    # queryset = Product.objects.order_by('name').reverse() # reverse everything
    
    # queryset = Product.objects.order_by('name')[0]        # use list to get 1st result
    # queryset = Product.objects.order_by('name')[:5]       # 1st 5 only
    # queryset = Product.objects.order_by('name')[10:20]    # from 10 to 20

    # queryset = Product.objects.earliest('name')           # easy than list to get 1st result
    # queryset = Product.objects.latest('name')            # easy than list to get last result
    
    # queryset = Product.objects.values('id','name')        # choose result of fields with dictionary
    # queryset = Product.objects.values('id','name','category__name')        # 
    # queryset = Product.objects.values_list('id','name','category__name')   # result in list
    # queryset = Product.objects.values('id','name','category__name').distinct()    # to cancel repeated result
    # queryset = Product.objects.only('id','name','category__name')    # get those only --in html if u call onther field that ll take long time to query for appear data
    # queryset = Product.objects.only('id','name','category__name','price')   # here we called price and still in html the query ll back so fast
    # queryset = Product.objects.defer('price')       # all field appear  except 'price'
    # queryset = Product.objects.all()    # (not used) and in html you call {{product.category.price}} that take long time cuz of condition
    # queryset = Product.objects.select_related('category').select_related('brand').all() # this useful in foreignkey relation (fast query)
    #                                                                                     # prefetch_related use in many-to-many
    
    
    
    # queryset = Product.objects.aggregate(myavg=Avg('price'),mysum=Sum('price'))    #result of avg or sum and more....
      
    # queryset = Product.objects.annotate(is_new=Value(True)) #
    
    # queryset = Product.objects.annotate(price_tax=F('price')* .8) 
    
    # queryset = Product.objects.annotate(                                           # make new field here not in database 
    #            full_name=Concat('name','sku' , output_field=CharField())           # put this 2 fields side by side
    # ) 
    
    
    
    queryset = Product.objects.price_greater_than(60)

    list(queryset)
    
    list(queryset)


    print(queryset)
     
    return render(request, 'products/list.html', {'data':queryset})







class ProductList(ListView):
    model = Product
    paginate_by = 50
    
    
    
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
        




