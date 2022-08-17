from django import forms
from .models import UserProfile,User

class UserForm(forms.ModelForm):
    class Meta:      
        model = User
        fields = ['username', 'first_name', 'last_name','password', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
        widgets = {
            'birth_date': forms.Textarea(attrs={'class': 'date'}),
            'has_pet': forms.Select(attrs={'class': 'checkbox'})
        }



