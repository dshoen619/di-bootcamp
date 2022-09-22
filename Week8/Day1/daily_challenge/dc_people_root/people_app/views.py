from django.http import HttpResponse
from tkinter.font import families
from django.shortcuts import render
import json

# # Create your views here.
# with open('people_app/data.json', 'r') as f:
#     data = json.load(f)

# peoples_data: list =data['people']


def show_people(request):

    return render(request, 'sort_by_age.html', test1=[1,2,3])