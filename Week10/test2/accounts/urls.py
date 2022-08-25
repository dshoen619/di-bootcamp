from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import  login, register,logout,dashboard

urlpatterns = [
    path('login',login, name="login"),
    path('register', register, name="register"),
    path('logout', logout, name="logout"),
    path('dashboard',dashboard,name="dashboard")
]

