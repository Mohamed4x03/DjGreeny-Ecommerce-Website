from ast import Str
from distutils.command.upload import upload
from django.db import models

# Create your models here.


class Country(models.Model):
    name=models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Countries'
    
    
class City(models.Model):
    country=models.ForeignKey(Country, related_name='country_city', on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Cities'
        

class Company(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to ='company/')        
    about = models.CharField(max_length=300)
    fb_link = models.URLField(null=True, blank=True)
    tw_link = models.URLField(null=True, blank=True)
    ins_link = models.URLField(null=True, blank=True)
    email = models.URLField(max_length=30)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name    
    
    class Meta:
        verbose_name_plural='Companies'
        
        
        
        
        
        
        
        
    
    
    