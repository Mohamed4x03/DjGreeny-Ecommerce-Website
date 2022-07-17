
from pickle import TRUE
from pyexpat import model
from xmlrpc.client import DateTime
from django.db import models
from django.forms import DateField, FloatField
import random
from django.utils.translation import gettext as _
from pytz import timezone
from django.utils import timezone

from products.models import  Product

# Create your models here.

def generated_code(length=8):
    numbers = '0123456789'
    return ' '.join(random.choice(numbers) for _ in range(length))

STATUS_CHOICES=(
    ('Received' , 'Received'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)




class Order(models.Model):
    code = models.CharField(_("Code"), max_length=8,default=generated_code)
    order_status = models.CharField(_("Order status"), max_length=10, choices=STATUS_CHOICES)
    order_time = models.DateTimeField(_("Order time"), default=timezone.now)
    delivery_time = models.DateTimeField(_("Delivery time"), null=TRUE , blank=TRUE)
    
    def __str__(self):
        return self.code
    
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("Order"), related_name='Order_detail',on_delete=models.CASCADE)  
    product = models.ForeignKey(Product, verbose_name=_("Product"), related_name='order_procduct', on_delete=models.SET_NULL ,null=TRUE, blank=TRUE)
    price = models.FloatField(_("Price"),)
    quantity = models.FloatField(_("Quantity"))
    
    def __str__(self) -> str:
        return str(self.order)