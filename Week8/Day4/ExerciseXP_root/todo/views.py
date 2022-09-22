from django.shortcuts import render,redirect
from .forms import add_task
from .models import Category, Todo
from datetime import date

def add_todo(request):

    context={'form': add_task}

    if request.method == 'POST':
        form_filled=add_task(request.POST)
        if form_filled.is_valid():
            title= form_filled.cleaned_data['data']
            details =form_filled.cleaned_data['details']
            deadline_date= form_filled.cleaned_data['deadline_date']
            category = form_filled.cleaned_data['category']

            Todo.objects.create(title=title, details=details, 
            deadline_date=deadline_date, category=category)

            Todo.objects.save()

    return render(request, 'add_todo.html', context)

def display_todos(request):

    all_todos= Todo.objects.all()
    context= {'to_dos':all_todos}
    return render(request, 'display_todos.html',context)




    