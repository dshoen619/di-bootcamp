from django.shortcuts import render,redirect
from .forms import AddDirectorForm, AddFilmForm
from .models import Film,Director

def homepage(request):
    films = Film.objects.all()
    directors=Director.objects.all()

    context={'films':films,'directors':directors}

    return render(request,'homepage.html',context)

def addFilm(request):
    context={'films':Film.objects.all()}
    context.update({'form': AddFilmForm})

    if request.method=='POST':
        form=AddFilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'add_film.html',context)

def addDirector(request):
    context={'director': Director.objects.all()}
    context.update({'form':AddDirectorForm})

    if request.method =='POST':
        form=AddDirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request,'add_director.html', context)

