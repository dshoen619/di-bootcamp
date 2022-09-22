from django.db import models
from phone_field import PhoneField

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone_number=PhoneField()
    address= models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    country= models.CharField(max_length=50)

class Vehicle_Type(models.Model):
    name= models.CharField(max_length=50)

class Vehicle_Size(models.Model):
    name=models.CharField(max_length=50)

class Vehicle(models.Model):
    type=models.ForeignKey(Vehicle_Type, related_name='type', on_delete=models.CASCADE)
    date_created= models.DateField()
    real_cost=models.IntegerField()
    size=models.ForeignKey(Vehicle_Size, related_name='size', on_delete=models.CASCADE)

class Rental(models.Model):
    rental_date=models.DateField()
    return_date= models.DateField()
    customer= models.ForeignKey(Customer, related_name='customer',on_delete=models.CASCADE)
    vehicle=models.ForeignKey(Vehicle,related_name='vehicles',on_delete=models.CASCADE)

class Rental_Rate(models.Model):
    daily_rate= models.IntegerField()
    vehicle_type= models.ForeignKey(Vehicle_Type,on_delete=models.CASCADE)
    vehicle_size=models.ForeignKey(Vehicle_Size,on_delete=models.CASCADE)
    