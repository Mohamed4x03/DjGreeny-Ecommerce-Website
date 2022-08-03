from cProfile import Profile
from dataclasses import field, fields
from django.shortcuts import render
from django.urls import is_valid_path
from .forms import SignupForm
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings



def signup(request):
    
    if request.method == 'POST':
        form=SignupForm(request.POST)
        
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            myform=form.save(commit=False)
            myform.active = False
            myform.save()
            profile=Profile.objects.get(user__username=username)
            print(profile)
            print(profile.code)
            
            send_mail(
                'Activate Your Account',
                f"use this code {profile.code} to activate your account",
                settings.EMAIL_HOST_USER,
                [email,],
                fail_silently=False,
            )
            
        
    else:
        form=SignupForm()
        
    return render(request, 'regestration/signup.html', {'form':form})


        