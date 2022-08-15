from re import I
from django.http import HttpResponse
from tkinter.font import families
from django.shortcuts import render
import json

with open('people_app/data.json', 'r') as f:
    data = json.load(f)

persons:list= data['people']

people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]


sorted_people= sorted(people, key = lambda x: x['age'])

def show_people(request) -> HttpResponse:

    return render(request, 'sort_by_age.html', {'people':sorted_people})

def show_person_by_id(request,id:int):
    person_selected= None

    for person in persons:
        if person['id']== id:
            person_selected: dict=person

    return render(request, 'single_person.html', person_selected)
