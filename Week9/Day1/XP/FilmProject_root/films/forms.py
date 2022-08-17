
from django import forms
from .models import Director,Film,Category,Country

class AddFilmForm(forms.ModelForm):
    class Meta:
        model=Film
        fields='__all__'

class AddDirectorForm(forms.ModelForm):
    class Meta:
        model=Director
        fields='__all__'