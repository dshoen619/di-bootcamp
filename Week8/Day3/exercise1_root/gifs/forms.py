
from django import forms 
from .models import Category_model


class Gifform(forms.Form):
    uploader_name= forms.CharField()
    title=forms.CharField()
    url = forms.URLField()
    categories= forms.ModelMultipleChoiceField(queryset=Category_model.objects.all())

class CategoryForm(forms.Form):
    name=forms.CharField()
