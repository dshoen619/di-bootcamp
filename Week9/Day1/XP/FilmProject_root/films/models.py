from datetime import datetime
from django.db import models

class Country(models.Model):
    name= models.CharField(max_length=50)

class Category(models.Model):
    name=models.CharField(max_length=50)

class Director(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

class Film(models.Model):
    title=models.CharField(max_length=50)
    released_date=models.DateField(default=datetime.now())
    created_in_country= models.ForeignKey(Country, on_delete=models.CASCADE)
    available_in_countries = models.ManyToManyField(Country, related_name='films')
    category=models.ManyToManyField(Category, related_name='films')
    director=models.ManyToManyField(Director, related_name='films')

