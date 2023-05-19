from django.db import models


# Create your models here.

class Menu_Items(models.Model):
    Title = models.CharField(max_length=255, unique=True)
    Price = models.FloatField(default=0.00)
    
    class Meta:
        ordering = ('Title',)
        verbose_name_plural = 'Menu Items'
        
    # def available(self):
    #     return all(X.enough() for X in self.reciperequirement_set.all())
        
    def __str__(self):
       return self.Title
   
   
class Ingredient(models.Model):
    """
    Represents a single ingredient in the restaurant's inventory
    """
    name = models.CharField(max_length=200, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=200)
    price_per_unit = models.FloatField(default=0)
    
    def __str__(self):
        return self.name
        
class RecipeRequirement(models.Model):
    """
    Represents an ingredient required for a recipe for a MenuItem
    """
    menu_item = models.ForeignKey(Menu_Items, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    
    def __str__(self):
        return self.menu_item.__str__()
    
    # def enough(self):
    #     return self.quantity <= self.ingredient.quantity
    
    
class Purchase(models.Model):
    """
    Represents a purchase of a MenuItem
    """
    menu_item = models.ForeignKey(Menu_Items, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}];  time={self.timestamp}"
    
