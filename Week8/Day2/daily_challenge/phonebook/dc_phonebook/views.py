from django.shortcuts import render
from.models import Person
from .forms import PersonForm

# Create your views here.

def person_by_number(request, number: int):
    person_selected=Person.objects.get(phone_number=number)
    return render(request, 'show_person.html', {'person':person_selected})

def person_by_name(request, name:str):
    person_selected=Person.objects.get(name=name)
    if len(person_selected)==0:
        person_selected=[None, "No one under this Name",None,None,None]
    return render(request, 'show_person.html',{'person':person_selected} )

def PersonbyForm (request):
    context={'form':PersonForm}

    if request.method=='POST':
        form_filled=PersonForm(request.POST)
        if form_filled.is_valid():
            id = form_filled.cleaned_data['id']
            name=form_filled.cleaned_data['name']
            email=form_filled.cleaned_data['email']
            phone_number=form_filled.cleaned_data['phone_number']
            address=form_filled.cleaned_data['address']

            Person.object.create(id=id, name=name, email=email,
            phone_number=phone_number, address=address )

            PersonForm.save()
            Person.save()

    return render(request, 'person_form.html', context)