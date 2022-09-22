from django import forms
from .models import PropertySearch

class SearchPropertyForm(forms.ModelForm):
    class Meta:
        model=PropertySearch
        fields='__all__'