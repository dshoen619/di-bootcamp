
from django.db import models
from datetime import date,datetime
from django.urls import reverse

# Create your models here.

class Gif_model(models.Model):
    title= models.CharField(max_length=50)
    url=models.URLField(max_length=200)
    uploader_name= models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
 

    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse('show_gif', args = [self.id])

class Category_model(models.Model):
    name=models.CharField(max_length=50)
    gif= models.ManyToManyField(Gif_model, related_name='categories',blank=True)

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse('show_category', args = [self.id])

class Likes_two (models.Model):
    gif_model = models.ForeignKey(Gif_model, on_delete=models.CASCADE, related_name='likes')