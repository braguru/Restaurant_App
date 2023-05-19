from django.urls import path
from .views import Index, add_menu, Menu, Menu_Detail, Delete_Menu, Edit_Menu
from . import views

urlpatterns = [
    path('dashboard/', Index.as_view(), name='dashboard'),
    path("", views.login_user , name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('add_menu/', add_menu.as_view(), name="add_menu"),
    path('menu/', Menu.as_view(), name="menu" ),
    path('<slug:pk>/', Menu_Detail.as_view(), name="menu_detail"),
    path('delete_menu/<slug:pk>/', Delete_Menu.as_view(), name="delete_menu"),
    path('edit_menu/<slug:pk>/', Edit_Menu.as_view(), name="edit_menu"),   
]