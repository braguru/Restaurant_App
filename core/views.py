from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from .models import Menu_Items, RecipeRequirement, Ingredient, Purchase
from .forms import Add_Menu_Form, RecipeRequirementForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Index(ListView):
    template_name = 'core/dashboard.html'
    context_object_name = 'homes'
    model = Menu_Items
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = Menu_Items.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context
    
    def get_queryset(self):
        return self.model.objects.all()
        
    
    
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request, ("There was an error try again. Try entering the correct credentials"))
            return redirect('login')
    else:
        return render(request, 'core/login.html')
  
    
def logout_user(request):
    logout(request)
    return redirect('login')


class add_menu(LoginRequiredMixin, CreateView):
    """Add Menu"""
    template_name = 'core/Add_menu_Item.html'
    model = Menu_Items
    form_class = Add_Menu_Form
    success_url = '/add_menu/'
   
    
class Menu(ListView):
    template_name = 'core/Menu.html'
    model = Menu_Items  
    context_object_name = 'menus'
    
    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            menus = self.model.objects.filter(
                Q(Title__icontains=query) |
                Q(Price__icontains=query)
            )
        else:
            return self.model.objects.all()
        return menus
    

class Menu_Detail(DetailView):
    template_name = 'core/menu_detail.html'
    model = Menu_Items
    context_object_name = 'menu'
    

class Delete_Menu(LoginRequiredMixin, DeleteView):
    model = Menu_Items
    success_url = '/menu/'
    template_name = 'core/menu_confirm_delete.html'


class Edit_Menu(LoginRequiredMixin, UpdateView):
    model = RecipeRequirement
    template_name = 'core/edit_menu.html'
    success_url = '/menu/'  
    form_class = RecipeRequirementForm  