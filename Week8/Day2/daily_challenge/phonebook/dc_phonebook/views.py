from django.shortcuts import render
from.models import Person

# Create your views here.

def person_by_number(request, number: int):
    person_selected=Person.objects.get(phone_number=number)
    return render(request, 'show_person.html', {'person':person_selected})

def person_by_name(request, name:str):
    person_selected=Person.objects.get(name=name)
    if len(person_selected)==0:
        person_selected=[None, "No one under this Name",None,None,None]
    return render(request, 'show_person.html',{'person':person_selected} )