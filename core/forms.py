from django import forms
from .models import Menu_Items, RecipeRequirement

class Add_Menu_Form(forms.ModelForm):
    class Meta:
        model = Menu_Items
        fields = '__all__'
        
class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"
