from django.urls import path
from .views import show_family,show_animal,show_all_animals

urlpatterns = [
    path('show_family/<int:id>', show_family, name='show_family'),
    path('show_animal/<int:id>',show_animal,name='show_animal'),
    path('all_animals/',show_all_animals,name='show_all_animals'),

]
