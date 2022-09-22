
from django import forms
from .models import Rental, Customer, Vehicle
from phone_field import PhoneField

class Add_Rental(forms.Form):
    customer=forms.IntegerField()
    vehicle=forms.IntegerField()

class Add_Customer(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        widgets={
            'first_name':forms.Textarea(),
            'last_name': forms.Textarea(),
            'email':forms.Textarea(),
            'phone_number': PhoneField(),
            'address': forms.Textarea(),
            'city': forms.Textarea(),
            'country':forms.Textarea()
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields = '__all__'

