from turtle import home
from django.urls import path
from .views import (
    add_director,
    update_film,
    update_director,
    director_films,
    director_search,
    Homepage,
    AddFilm
)
urlpatterns = [
    path('add-film', AddFilm.as_view(), name="add_film"),
    path('homepage', Homepage.as_view(), name="homepage"),
    path('add-director', add_director, name='add_director'),
    path('update-film/<int:id>', update_film, name='update_film'),
    path('update-director/<int:id>', update_director, name='update_director'),
    path('director-films/<int:id>', director_films, name='director_films'),
    path('search-director', director_search, name = "director_search")
]

