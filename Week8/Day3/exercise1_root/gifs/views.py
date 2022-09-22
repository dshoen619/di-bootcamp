from django.shortcuts import render, redirect
from .models import Category_model, Gif_model,Likes_two
from .forms import CategoryForm, Gifform


def create_category(request):

    if request.method == 'POST':
        form_filled = CategoryForm(request.POST)
        if form_filled.is_valid():
            name = form_filled.cleaned_data['name']
            Category_model.objects.create(name = name)

    # method - GET 
    context = {'form': CategoryForm}
    return render(request, 'create_category.html', context)

def create_gif(request):

    if request.method == 'POST':
        form_filled = Gifform(request.POST)
        if form_filled.is_valid():

            title = form_filled.cleaned_data['title']
            url = form_filled.cleaned_data['url']
            uploader = form_filled.cleaned_data['uploader_name']
            categories = form_filled.cleaned_data['category']

            new_gif = Gif_model(title=title, url=url, uploader_name_2=uploader)
            new_gif.save()

            for cat in categories:
                new_gif.categories.add(cat)

            new_gif.save()


    context = {'form': Gifform}
    return render(request, 'create_gif.html', context)

def category_view(request, id):
    category = Category_model.objects.get(id=id)
    gifs = category.gif.all()

    context = {'category': category, 'gifs': gifs}

    return render(request, 'category.html', context)

def homepage(request):
    context = {'gifs': Gif_model.objects.all(),
               'categories': Category_model.objects.all()}
    return render(request, 'homepage.html', context)

def likes(request):
    if "Like" in request.POST:
        Gif_model.objects.all().likes+=1
        Gif_model.objects.all().save()
    context={'gifs': Gif_model.objects.all()}



    return render(request, 'like_page.html', context)

def add_like(request,id):
    gif_select= Gif_model.objects.get(id=id)
    new_like=Likes_two(gif_model=gif_select)
    new_like.save()

    context={'gifs': Gif_model.objects.all()}

    return render(request, 'like_page.html', context) 
