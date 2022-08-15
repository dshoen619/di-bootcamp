from django.urls import path
from .views import show_all_in_fam, show_family, show_animal, show_animals

urlpatterns = [
    path('family/', show_family, name='show_family'),
    path('animal/<int:id>', show_animal, name='show_animal'),
    path('animals', show_animals, name='show_animals'),
    path('all_in_the_fam/<int:id>', show_all_in_fam, name= 'show_fam'),
]
