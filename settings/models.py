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
    
    
    