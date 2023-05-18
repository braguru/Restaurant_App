from django.urls import path
from .views import Index
from . import views

urlpatterns = [
    path('dashboard/', Index.as_view(), name='dashboard'),
    path("", views.login_user , name="login"),
    path('logout/', views.logout_user, name="logout")
]