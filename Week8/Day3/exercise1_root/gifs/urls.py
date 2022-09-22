from django.urls import path
from .views import (homepage,create_category,create_gif,category_view,likes,add_like)

urlpatterns =[
    path("homepage",homepage,name="homepage"),
    path("create_gif", create_gif, name='create_gif'),
    path("create_category", create_category, name='create_category'),
    path("category/<int:id>", category_view, name="show_category"),
    path("likes",likes,name="likes"),
    path("add_like/<int:id>", add_like ,name="add_like")
    
]