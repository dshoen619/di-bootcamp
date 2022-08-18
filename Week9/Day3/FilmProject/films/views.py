from django.contrib.auth.decorators import login_required, user_passes_test

from django.shortcuts import render, redirect
from .forms import FilmForm, DirectorForm
from django.views import generic
from .models import Director, Film
from django.contrib import messages

from itertools import chain

from django.db.models import Q
from datetime import date
from django import forms


# Create your views here.
class Homepage(generic.ListView):
    template_name = 'homepage.html'
    context_object_name = "films"
    form_class = FilmForm
    model = Film
    
    def get_form(self, form_class):
        form = super(Homepage, self).get_form(form_class)
        form.fields['release_date'].widget = forms.DateInput(attrs={'type':'date'})
        return form


# def add_film(request):
#     context = {'form': FilmForm(initial={'release_date': date.today()})}

#     if request.method == 'POST':
#         form_filled = FilmForm(request.POST)
#         if form_filled.is_valid():
#             form_filled.save()
#             return redirect('homepage')
#         else:
#             print(form_filled.errors)
    
#     return render(request, 'add_film.html', context)

class AddFilm(generic.CreateView):
    model = Film
    fields = "__all__"
    template_name = "add_film.html"
    success_url = 'homepage'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('films.can_add_film'):
            messages.add_message(request, messages.ERROR, "User Doesnt have PERMISSIONS!")     
            return redirect('homepage')   
        return super().dispatch(request, *args, **kwargs)


@user_passes_test(lambda u: u.has_perm('films.add_director'), login_url='signin')
def add_director(request):
    context = {'form': DirectorForm}

    if request.method == 'POST':
        form_filled = DirectorForm(request.POST)
        if form_filled.is_valid():
            form_filled.save()
            return redirect('homepage')
        else:
            print(form_filled.errors)
    
    return render(request, 'add_director.html', context)    

@login_required(login_url='signin')
def update_director(request, id):
    dir = Director.objects.get(id=id)
    form = DirectorForm(request.POST or None, instance=dir)

    context = {'form': form}

    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Director updated successfully")
        return redirect('homepage')

    return render(request, 'update_director.html', context)

@user_passes_test(lambda u: u.has_perm('films.update_film'), login_url='signin')
def update_film(request, id):
    film = Film.objects.get(id=id)
    form = FilmForm(request.POST or None, instance=film)

    context = {'form': form} 

    if form.is_valid():
        form.save()
        return redirect('homepage')
    return render(request, 'update_film.html', context)


def director_films(request, id):
    director = Director.objects.get(id=id)
    films = director.films.all()
    context = {'director': director,'films': films}

    return render(request, 'director_films.html', context)


def director_search(request):
    query_dict = request.GET
    try:
        query = query_dict.get('search')
    except:
        query = None

    if query is not None:
        directors = Director.objects.filter(Q(first_name__icontains = query) | Q(last_name__icontains = query))
        films = Film.objects.filter(Q(title__icontains = query))

    context = {'objects_selected': chain(directors,films)}

    return render(request, 'director_search.html', context)
