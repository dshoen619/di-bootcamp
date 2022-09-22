from django.db import models

class PropertySearch(models.Model):
    keyword=models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    bedrooms=models.IntegerField()
    max_price=models.IntegerField()

