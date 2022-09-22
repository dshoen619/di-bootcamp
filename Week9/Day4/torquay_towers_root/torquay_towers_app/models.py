from django.db import models

class Vacancies(models.Model):
    September=models.DateField()
    October=models.DateField()
    November=models.DateField()

class Booking(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    party_size=models.CharField(max_length=50)
    start_date=models.DateField()
    number_nights=models.IntegerField()

class Contact(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    questions=models.TextField()


class Review(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    review=models.TextField()


