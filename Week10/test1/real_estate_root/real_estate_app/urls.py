from django.contrib import admin
from django.urls import path
from .views import homepage

urlpatterns = [
    path('home', homepage, name='homepage'),


]