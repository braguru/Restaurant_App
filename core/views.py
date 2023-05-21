from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from .models import Menu_Items, RecipeRequirement, Ingredient, Purchase
from .forms import Add_Menu_Form, RecipeRequirementForm, Add_Ingredient_form
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Index(ListView):
    template_name = 'core/dashboard.html'
    model = Menu_Items
    context_object_name = 'homes'
    
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
    success_url = '/menu/'
    
    
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
    form_class = RecipeRequirementForm  
    success_url = '/menu/' 
    context_object_name = 'recipes' 

    
class Ingredient_View(ListView):
    template_name = 'core/Ingredient.html'
    model = Ingredient  
    context_object_name = 'ingredients'
    
    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            ingredients = self.model.objects.filter(
                Q(name__icontains=query) |
                Q(quantity__icontains=query) |
                Q(unit__icontains=query) |
                Q(price_per_unit__icontains=query)
            )
        else:
            return self.model.objects.all()
        return ingredients
    
    
class Ingredient_Detail(DetailView):
    template_name = 'core/ingredient_detail.html'
    model = Ingredient
    context_object_name = 'ingredient'
    
    
class Add_Ingredient(LoginRequiredMixin, CreateView):
    template_name = 'core/Add_ingredient.html'
    model = Ingredient
    context_object_name = 'ingredients'
    form_class = Add_Ingredient_form
    success_url = '/ingredient/'
    

class Delete_Ingredient(LoginRequiredMixin, DeleteView):
    model = Ingredient
    success_url = '/ingredient/'
    template_name = 'core/ingredient_confirm_delete.html'


class Edit_Ingredient(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = 'core/edit_ingredient.html'
    form_class = Add_Ingredient_form  
    success_url = '/ingredient/' 
    context_object_name = 'ingredients' 