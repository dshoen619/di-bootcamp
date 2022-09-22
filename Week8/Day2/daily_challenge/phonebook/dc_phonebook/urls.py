from django.urls import path
from .views import person_by_number, person_by_name, PersonbyForm

urlpatterns = [
    path('number/<int:number>', person_by_number, name='show_person'),
    path('name/<str:name>',person_by_name,name='person_by_name'),
    path('person_form', PersonbyForm, name='person_form')

]