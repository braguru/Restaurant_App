from django.urls import path
from .views import (Index, add_menu, Menu, 
                    Menu_Detail, Delete_Menu, Edit_Menu, 
                    Ingredient_View, Ingredient_Detail,
                    Add_Ingredient, Delete_Ingredient,
                    Edit_Ingredient)
from . import views

urlpatterns = [
    path('dashboard/', Index.as_view(), name='dashboard'),
    path("", views.login_user , name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('add_menu/', add_menu.as_view(), name="add_menu"),
    path('menu/', Menu.as_view(), name="menu" ),
    path('menu_detail/<slug:pk>/', Menu_Detail.as_view(), name="menu_detail"),
    path('delete_menu/<slug:pk>/', Delete_Menu.as_view(), name="delete_menu"),
    path('edit_menu/<slug:pk>/', Edit_Menu.as_view(), name="edit_menu"), 
    path('ingredient/', Ingredient_View.as_view(), name="ingredient"),
    path('ingredient_detail/<slug:pk>/', Ingredient_Detail.as_view(), name="ingredient_detail" ),
    path('add_ingredient/', Add_Ingredient.as_view(), name="add_ingredient" ),
    path('delete_ingredient/<slug:pk>/', Delete_Ingredient.as_view(), name="delete_ingredient"),
    path('edit_ingredient/<slug:pk>/', Edit_Ingredient.as_view(), name="edit_ingredient"),
]