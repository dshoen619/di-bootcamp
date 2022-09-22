from django.shortcuts import render,redirect
from .models import PropertySearch
from .forms import SearchPropertyForm

def homepage(request):

    context=({'form':SearchPropertyForm})

    if request.method=='POST':
            form = SearchPropertyForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('results')
    return render(request, 'homepage.html',context)