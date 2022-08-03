from ast import Pass
from distutils.command.upload import upload
from email.mime import image
from email.policy import default
import profile
from pyexpat import model
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from settings.models import City, Country
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.generate_code import generated_code
# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile/', null=True, blank=True)
    code=models.CharField(max_length=50, default=generated_code)
    code_used=models.BooleanField(default=False)
    


    def __str__(self):
        return self.user.username
    

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
        
    
DATA_TYPE=(
        ('Home','Home'),
        ('Office','Office'),
        ('Bussiness','Bussiness'),
        ('Academy','Academy'),
        ( 'Others','Others'),
    )
        
    
class UserPhoneNumber(models.Model):
    user=models.ForeignKey(User, related_name='user_phone', on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=15)
    type=models.CharField(max_length=50, choices=DATA_TYPE)


    def __str__(self):
        return f"{self.user.username}-{self.type}"


class UserAddress(models.Model):
    user=models.ForeignKey(User, related_name='user_address', on_delete=models.CASCADE)
    type=models.CharField(max_length=50, choices=DATA_TYPE)
    country=models.ForeignKey(Country, related_name='user_country', on_delete=models.SET_NULL , null=True)
    city=models.ForeignKey(City, related_name='user_city', on_delete=models.SET_NULL, null=True)
    state=models.CharField(max_length=50)
    region=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    notes=models.TextField(max_length=300, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}-{self.type}"
    
    