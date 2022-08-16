from datetime import date
from email.policy import default
from django import forms
from .models import Category
from .validators import check_splcharacter

class add_task(forms.Form):
    title= forms.CharField()
    details=forms.CharField(widget=forms.Textarea(attrs={'rows':2,'class':'details'}))
    deadline_date=forms.DateTimeField(widget=forms.DateInput)
    category=forms.ModelChoiceField(queryset=Category.objects.all())
    
