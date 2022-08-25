from django.urls import path
from .views import index, about
from listings.views import search
from accounts.views import register,login, dashboard

urlpatterns=[
    path('', index, name='index'),
    path('about/',about, name='about'),
    path('search.html', search, name="search"),
    path('register.html',register, name='register'),
    path('login.html', login, name='login'),
    path('dashboard', dashboard, name='dashboard'),
]