from http.client import HTTPResponse
from django.shortcuts import render
from .models import Family,Animal
from django.http import HttpResponse

# Create your views here.
def show_family(request, id: int) -> HTTPResponse:
    family_selected = Family.objects.get(id=id)
    return render(request, 'family.html',{'family':family_selected})

def show_animal(request, id:int) -> HTTPResponse:
    animal_selected=Animal.objects.get(id=id)
    return render(request,'animal.html', {'animal': animal_selected})

def show_all_animals(request)-> HTTPResponse:
    animal_selected=Animal.objects.all()
    return render(request,'all_animals.html', {'animals':animal_selected})