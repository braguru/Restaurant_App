from django.contrib import admin
from .models import Menu_Items, Ingredient, RecipeRequirement, Purchase

# Register your models here.

admin.site.register(Menu_Items)
admin.site.register(Ingredient)
admin.site.register(RecipeRequirement)
admin.site.register(Purchase)