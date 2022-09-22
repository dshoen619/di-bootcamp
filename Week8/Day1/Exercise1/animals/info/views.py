from django.http import HttpResponse
from tkinter.font import families
from django.shortcuts import render
import json
# Create your views here.

with open('info/data.json', 'r') as f:
    data = json.load(f)

animals: list = data['animals']
families: list = data['families']

def show_family(request, id: int) -> HttpResponse:

    family_selected = None

    for family in families:
        if family['id'] == id:
            family_selected: dict = family

    return render(request, 'family.html', family_selected)
    

def show_animal(request, id: int) -> HttpResponse:

    animal_selected = None

    for animal in animals:
        if animal['id'] == id:
            animal_selected: dict = animal

    return render(request, 'animal.html', animal_selected)


def show_animals(request) -> HttpResponse:
    return render(request, 'animals.html', {'animals': animals, 'test':[1,2,3]})

def show_all_in_fam(request, id:int):
    
    animal_selected=None

    for animal in animals:
        if animal['id']==id:
            animal_selected:dict=animal

    return render(request,'all_in_the_fam.html',animal_selected)
