from django import forms
from .models import Menu_Items, RecipeRequirement, Ingredient

class Add_Menu_Form(forms.ModelForm):
    class Meta:
        model = Menu_Items
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(Add_Menu_Form, self).__init__(*args, **kwargs)
        
        self.fields['Title'].widget.attrs['class'] = "form-control p-2 mb-5"
        self.fields['Price'].widget.attrs['class'] = "form-control p-2"

        
class RecipeRequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(RecipeRequirementForm, self).__init__(*args, **kwargs)
        
        self.fields['menu_item'].widget.attrs['class'] = "form-control p-2 mb-3"
        self.fields['ingredient'].widget.attrs['class'] = "form-control p-2 mb-3"
        self.fields['quantity'].widget.attrs['class'] = "form-control p-2 mb-3"


class Add_Ingredient_form(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(Add_Ingredient_form, self).__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs['class'] = "form-control p-2 mb-3"
        self.fields['quantity'].widget.attrs['class'] = "form-control p-2 mb-3"
        self.fields['unit'].widget.attrs['class'] = "form-control p-2 mb-3"
        self.fields['price_per_unit'].widget.attrs['class'] = "form-control p-2"
        