from audioop import add
from django.urls import path
from .views import add_todo,display_todos

urlpatterns= [
    path("add_todo", add_todo,name="add_todo"),
    path("display_todos", display_todos, name="display")
]