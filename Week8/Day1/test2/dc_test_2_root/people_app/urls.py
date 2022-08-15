from django.urls import path
from .views import show_people, show_person_by_id

urlpatterns = [
    path('show_people',show_people,name='show_people'),
    path('show_person/<int:id>', show_person_by_id, name='show_person')
]