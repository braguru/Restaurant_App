from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import models

# Create your views here.

class Index(TemplateView):
    template_name = 'core/dashboard.html'
    
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request, ("There was an error try again"))
            return redirect('login')
    else:
        return render(request, 'core/login.html')
  
    
def logout_user(request):
    logout(request)
    return redirect('login')



    