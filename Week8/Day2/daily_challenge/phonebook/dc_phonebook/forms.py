from django import forms
from .models import Person
from phone_field import PhoneField

class PersonForm(forms.Form):
    id = forms.IntegerField()
    name=forms.CharField(max_length=50)
    email=forms.CharField(max_length=50)
    phone_number=forms.CharField()
    address=forms.CharField(max_length=50)





