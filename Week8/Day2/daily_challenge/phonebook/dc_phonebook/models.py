from django.db import models
from phone_field import PhoneField
# Create your models here.
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name= models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)
    phone_number=PhoneField()
    address= models.CharField(max_length=50)