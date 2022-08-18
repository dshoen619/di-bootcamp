from dataclasses import fields
from django import forms
from datetime import date
from .models import (
    Director,
    Film
)

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'release_date': forms.DateInput(attrs={'type':'date'})
        }

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'

